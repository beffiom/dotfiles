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

import typing

from jmatrix import rule


class JMatrixParserError(ValueError):
	pass

def _rule_converter(d: str, r: str, rules: rule.Rules) -> None:
	split_rules = r.split()
	if not (2 <= len(split_rules) <= 4):
		raise JMatrixParserError("Incorrect number of rules to: {}.".format(r))
	if len(split_rules) < 3:
		split_rules.append('*')
	if len(split_rules) < 4:
		split_rules.append('allow')
	source_hostname, dest_hostname, rq_type, action = split_rules
	action_value = rule.Action.from_str(action)
	if action_value is None:
		raise JMatrixParserError("Incorrect action values to {}.".format(r))
	request_type = rule.Type.from_str(rq_type)
	if request_type is None:
		raise JMatrixParserError("Incorrect request type value to {}.".format(r))
	rules.matrix_rules[source_hostname][dest_hostname][request_type] = action_value

def _matrix_flag_converter(d: str, r: str, rules: rule.Rules) -> None:
	split_rules = r.split()
	if len(split_rules) != 2:
		raise JMatrixParserError("Incorrect number of rules to {}.".format(r))
	source_hostname, state = split_rules
	flag_val = rule.Flag.from_str(d)
	if flag_val is None:
		raise JMatrixParserError("Incorrect flag type to {}.".format(r))
	state_bool = state.lower() == "true"
	rules.matrix_flags[source_hostname][flag_val] = state_bool


# A mapping from uMatrix rule directives to converter functions
RULE_TO_CONVERTER = {
	"rule": _rule_converter,
	"matrix-off": _matrix_flag_converter,
	"https-strict": _matrix_flag_converter,
}


def rules_to_map(rule_lines: typing.Iterable[str], rules: rule.Rules, *,
				 collate_errors: bool=False) -> typing.Iterable[JMatrixParserError]:
	"""Convert uMatrix rules into jmatrix lists.
	rule_lines: The string to parse into rules
	rules: The rule object to update
	collate_errors: Instead of throwing errors on a bad entry, eat the error
and keep going. Then return all errors in a list. This option is dangerous if
the return value is ignored!
	"""
	errors = []
	for r in rule_lines:
		# Remove comments
		r = r.split('#', 1)[0].strip()
		if not r:
			continue
		r_list = r.split(":", 1)
		if len(r_list) > 1:
			directive = r_list[0]
			line = r_list[1]
		else:
			directive = "rule"
			line = r
		directive = directive.lower().strip()
		line = line.strip()
		if directive not in RULE_TO_CONVERTER:
			# TODO come up with better way to output this if needed.
			# print("[jmatrix]: rule '{}' ignored!".format(directive))
			pass
		else:
			try:
				RULE_TO_CONVERTER[directive](directive, line.strip(), rules)
			except JMatrixParserError as e:
				if collate_errors:
					errors.append(e)
				else:
					raise e
	return errors

def map_to_rules(rules: rule.Rules) -> str:
	"""Convert jmatrix rules to uMatrix compatible text."""
	lines = []
	for host, flags in rules.matrix_flags.items():
		for flag, state_b in flags.items():
			flag_s = flag.name.lower().replace('_', '-')
			state = str(state_b).lower()
			lines.append("{}: {} {}".format(
				flag_s, host, state,
			))

	for origin in rules.matrix_rules:
		for dest in rules.matrix_rules[origin]:
			for res_type in rules.matrix_rules[origin][dest]:
				action = rules.matrix_rules[origin][dest][res_type]
				res_type_s = str(res_type)

				lines.append("{} {} {} {}".format(
						origin, dest, res_type_s, action.name.lower()
				))

	return "\n".join(lines)
