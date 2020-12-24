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

import enum
import typing
import collections
import functools

JMATRIX_HEADER = """# WARNING: This file can be overwritten easily with the :jmatrix-write-rules command
# When data is overwritten, formatting and comments will be lost.
# Please exercise caution when editing this file directly, and make sure to keep backups.


"""

DEFAULT_RULES = """
https-strict: behind-the-scene false
matrix-off: about-scheme true
matrix-off: behind-the-scene true
matrix-off: chrome-extension-scheme true
matrix-off: chrome-scheme true
matrix-off: moz-extension-scheme true
matrix-off: opera-scheme true
matrix-off: vivaldi-scheme true
matrix-off: wyciwyg-scheme true
matrix-off: qute-scheme true
noscript-spoof: * true
referrer-spoof: * true
referrer-spoof: behind-the-scene false
* * * block
* * css allow
* * frame block
* * image allow
* 1st-party * allow
* 1st-party frame allow
"""

class Action(enum.Enum):
	"""A uMatrix action.

Defined formally in the uMatrix rule documentation.

https://github.com/gorhill/uMatrix/wiki/Rules-syntax

	"""
	BLOCK = 1
	ALLOW = 2
	INHERIT = 3

	def __str__(self) -> str:
		return self.name.lower()

	@staticmethod
	def from_str(s: str) -> typing.Optional['Action']:
		"""Convert s to an Action.

		Return None if s is not a valid Action"""
		s = s.upper()
		return Action.__members__.get(s, None)

class Type(enum.Enum):
	"""A uMatrix request type.

Defined formally in the uMatrix rule documentation.

https://github.com/gorhill/uMatrix/wiki/Rules-syntax
	"""
	ALL = 1  # The fallback 'star' (*) rule
	COOKIE = 2
	CSS = 3
	IMAGE = 4
	MEDIA = 5
	SCRIPT = 6
	XHR = 7
	FRAME = 8
	OTHER = 9

	def __str__(self) -> str:
		if self == Type.ALL:
			return '*'
		return self.name.lower()

	@staticmethod
	def from_str(s: str) -> typing.Optional['Type']:
		"""Convert s to a Type.

		Return None if s is not a valid Type"""
		s = s.upper()
		if s == '*':
			return Type.ALL
		# https://github.com/gorhill/uMatrix/issues/759
		elif s == 'PLUGIN':
			return Type.MEDIA
		return Type.__members__.get(s, None)

class Flag(enum.Enum):
	"""A uMatrix flag type (for matrix-off, https-strict, etc).

Defined formally in the uMatrix rule documentation.

https://github.com/gorhill/uMatrix/wiki/Rules-syntax

	"""
	MATRIX_OFF = 1
	HTTPS_STRICT = 2

	def __str__(self) -> str:
		return self.name.lower().replace('_', '-')

	@staticmethod
	def from_str(s: str) -> typing.Optional['Flag']:
		"""Convert s to a Flag.

		Return None if s is not a valid Flag"""
		s = s.upper().replace('-', '_')
		return Flag.__members__.get(s, None)

RULE_MATRIX_TYPE = typing.Dict[str, typing.Dict[str, typing.Dict[Type, Action]]]
RULE_MATRIX_FLAGS_TYPE = typing.Dict[str, typing.Dict[Flag, bool]]

class Rules():

	"""All rules for the interceptor."""

	def __init__(self) -> None:
		#: Flags which apply to first party domains.
		self.matrix_flags = collections.defaultdict(dict)  # type: RULE_MATRIX_FLAGS_TYPE
		# buckle up, we're going on a ride.
		#: Rules for which resources to block/allow.
		#: Nested dicts that look like {origin: {dest: {Type: Action}}}
		self.matrix_rules = (
			collections.defaultdict(
				functools.partial( # type: ignore
					collections.defaultdict,
					functools.partial(
						collections.defaultdict,
						functools.partial(
							# Inherit by default
							Action, 3)))))  # type: RULE_MATRIX_TYPE
