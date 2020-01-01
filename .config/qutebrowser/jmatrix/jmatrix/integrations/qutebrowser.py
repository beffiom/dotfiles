# Copyright (C) 2019  Jay Kamat <jaygkamat@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


## TODO FIXME make config-source not be super painful

import sys, os, time

import jmatrix.rule, jmatrix.umatrix_parser, jmatrix.interceptor
from jmatrix.vendor.fpdomain import fpdomain

from qutebrowser.api import interceptor, cmdutils, message, apitypes
from qutebrowser.completion.models import completionmodel, listcategory
from qutebrowser.utils import objreg

from qutebrowser.config.configfiles import ConfigAPI  # noqa: F401
from qutebrowser.config.config import ConfigContainer # noqa: F401

from qutebrowser.misc import editor

config = config  # type: ConfigAPI # noqa: F821 pylint: disable=E0602,C0103
c = c  # type: ConfigContainer # noqa: F821 pylint: disable=E0602,C0103

MYPY = False
if MYPY:
	from qutebrowser.config import configcommands

# If false, disable blocking. Usually changed via the jmatrix-toggle command
JMATRIX_ENABLED = True

# Used to actually decide if we should block a rule or not
JMATRIX_RULES = jmatrix.rule.Rules()

# Used to track requests that we have seen for purposes of completion
SEEN_REQUESTS = jmatrix.rule.Rules()

# Used to handle first party domains
PSL = None

JMATRIX_CONFIG = config.configdir / "jmatrix-rules"
PSL_FILE = config.datadir / "psl"

if not JMATRIX_CONFIG.exists():
	# Create the file with the default config
	with open(JMATRIX_CONFIG, "w", encoding="utf-8") as f:
		f.write(jmatrix.rule.JMATRIX_HEADER + jmatrix.rule.DEFAULT_RULES)

@cmdutils.register()
def jmatrix_read_config() -> None:
	"""Overwrite internal config with the one in the jmatrix config file."""
	global JMATRIX_RULES
	global SEEN_REQUESTS
	global PSL
	JMATRIX_RULES = jmatrix.rule.Rules()
	SEEN_REQUESTS = jmatrix.rule.Rules()
	with open(JMATRIX_CONFIG, "r", encoding="utf-8") as f:
		errors = jmatrix.umatrix_parser.rules_to_map(f, JMATRIX_RULES, collate_errors=True)
		tuple(map(message.error, map("!!!!!!!!! Error parsing umatrix rule: {} !!!!!!!".format, errors)))
	PSL = fpdomain.PSL(PSL_FILE)

@cmdutils.register()
def jmatrix_write_config() -> None:
	"""Write out current rules."""
	# This will strip out the "ignored" values in the default config.
	text = jmatrix.umatrix_parser.map_to_rules(JMATRIX_RULES)
	with open(JMATRIX_CONFIG, "w", encoding="utf-8") as f:
		f.write(jmatrix.rule.JMATRIX_HEADER + text)

@cmdutils.register(instance='config-commands')
def jmatrix_edit_config(self: 'configcommands.ConfigCommands', no_source: bool = False) -> None:
	"""Open the jmatrix-rules file in the editor.

	Args:
		no_source: Don't re-source the rules file after editing.
	"""
	def on_file_updated() -> None:
		"""Source the new config when editing finished.

		"""
		try:
			jmatrix_read_config()
		except:
			message.error("Unexpected error while reloading rules file. Check syntax?")

	ed = editor.ExternalEditor(watch=True, parent=self._config)
	if not no_source:
		ed.file_updated.connect(on_file_updated)

	filename = os.path.join(config.configdir, 'jmatrix-rules')
	ed.edit_file(filename)


# Read back config
jmatrix_read_config()

# Unsupported matrix rules:
# - cookie
QUTEBROWSER_JMATRIX_MAPPING = {
	interceptor.ResourceType.stylesheet: jmatrix.rule.Type.CSS,
	interceptor.ResourceType.image: jmatrix.rule.Type.IMAGE,
	interceptor.ResourceType.media: jmatrix.rule.Type.MEDIA,
	interceptor.ResourceType.script: jmatrix.rule.Type.SCRIPT,
	interceptor.ResourceType.xhr: jmatrix.rule.Type.XHR,
	interceptor.ResourceType.sub_frame: jmatrix.rule.Type.FRAME,
}

QUTEBROWSER_JMATRIX_RESOURCE_WHITELIST = frozenset({
	# Never blacklist main navigation (should this be changed?)
	interceptor.ResourceType.main_frame,
	# Never blacklist favicons (uMatrix configures this via images, but this
	# causes favicons to break when tabs.favicons.show is set)
	# http://www.gitlab.com/jgkamat/jmatrix/issues/2#note_204792112
	interceptor.ResourceType.favicon})

def _jmatrix_intercept_request(info: interceptor.Request) -> None:
	request_type = info.resource_type
	# If we are already blocked or whitelisted, don't waste our time here.
	if (not JMATRIX_ENABLED or
		info.is_blocked or
		request_type in QUTEBROWSER_JMATRIX_RESOURCE_WHITELIST): return
	first_party_url = info.first_party_url
	if first_party_url.isEmpty():
		# This case occurs when downloading URLs. Ideally we would hard-block
		# these kinds of urls to block malformed requests, but in order to fix
		# download, we'll pretend this is first-party for now.
		first_party_url = info.request_url

	context_host = first_party_url.host()
	context_scheme = first_party_url.scheme()
	request_scheme = info.request_url.scheme()
	# TODO sometimes the context url as well is a data url. This seems like a bug. We can't handle this case very well
	# though, as we will most likely end up blocking this case. If there's a way to work-around this, we should.
	if request_scheme in {"blob", "data"} or context_scheme in {"blob", "data"}:
		# These 'blob' urls don't seem to be actual requests, but internal chrome stuff
		# Let them pass, since they aren't real requests and break things if we block them.
		return
	request_host = info.request_url.host()

	jmatrix_type = QUTEBROWSER_JMATRIX_MAPPING.get(request_type, jmatrix.rule.Type.OTHER)
	block = jmatrix.interceptor.should_block(
		context_host, context_scheme,
		request_host, request_scheme,
		jmatrix_type, PSL.fp_domain, JMATRIX_RULES)
	if block:
		info.block()

	SEEN_REQUESTS.matrix_rules[context_host][request_host][jmatrix_type] = \
		jmatrix.rule.Action.BLOCK if block else jmatrix.rule.Action.ALLOW

interceptor.register(_jmatrix_intercept_request)

def _get_rules_completion(*args, info):
	tab = objreg.get('tab', scope='tab', window=info.win_id, tab='current')
	model = completionmodel.CompletionModel(column_widths=(100,))
	entries = [
		("{:10}{:10}{}".format(action.name, res_type.name.lower(), dest),) for
		dest, types in SEEN_REQUESTS.matrix_rules[tab.url().host()].items() for
		res_type, action in types.items()
	]
	cat = listcategory.ListCategory("Requests", entries)
	model.add_category(cat)
	return model

@cmdutils.register()
@cmdutils.argument("rule", completion=_get_rules_completion)
@cmdutils.argument("tab", value=cmdutils.Value.cur_tab)
def jmatrix_toggle_rule(tab: apitypes.Tab, rule: str):
	"""View request types made on this host and block/allow them.

	Requests are collated based on the host of the URL, so you may see requests from other pages on the same host.

	"""
	try:
		action, res_type, dest = rule.split()
	except ValueError:
		raise cmdutils.CommandError(
			"Expected input of the form \"block/allow request_type "
			"destination_host\""
		)
	if action.upper() == "BLOCK":
		action = jmatrix.rule.Action.ALLOW
	else:
		action = jmatrix.rule.Action.BLOCK
	if res_type == '*':
		res_type = "ALL"
	try:
		res_type = jmatrix.rule.Type[res_type.upper()]
	except KeyError:
		message.error("Type '{}' not recognized".format(res_type))
	origin = tab.url().host()
	JMATRIX_RULES.matrix_rules[origin][dest][res_type] = action
	# Change our seen requests to match so it'll show up in the completion
	# without having to reload the page.
	SEEN_REQUESTS.matrix_rules[origin][dest][res_type] = action

@cmdutils.register()
def jmatrix_toggle(quiet=False):
	global JMATRIX_ENABLED
	JMATRIX_ENABLED = not JMATRIX_ENABLED
	enabled_str = "enabled" if JMATRIX_ENABLED else "disabled"
	if not quiet:
		message.info("jmatrix has been " + enabled_str)
