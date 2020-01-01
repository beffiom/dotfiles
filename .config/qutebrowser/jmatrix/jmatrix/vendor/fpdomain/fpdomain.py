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

# The upstream for this package is currently https://gitlab.com/jgkamat/fpdomain

"""A simple utility that uses the public suffix list for obtaining first party URLs"""

import pathlib, tempfile, os, functools, typing, operator, itertools, re
import urllib.request

class PSL:
	"""Represents a PSL Database"""
	PSL_URL = "https://publicsuffix.org/list/public_suffix_list.dat"

	__slots__ = ['psl']  # type: typing.List[str]

	@staticmethod
	def update_psl(
			path: pathlib.Path, url:
			typing.Optional[str] = PSL_URL) -> None:
		"""Update the PSL at path. Overwrites current contents."""
		r = urllib.request.Request(
			PSL.PSL_URL,
			headers={'User-Agent': 'Mozilla/5.0'})
		raw_psl = urllib.request.urlopen(r).read().decode('utf-8')
		with open(path, "w") as f:
			f.write(raw_psl)

	@staticmethod
	def _parse_psl(path: pathlib.Path) -> typing.FrozenSet[str]:
		if not path.exists():
			# Error writing path
			raise FileNotFoundError("Error reading from the PSL!")
		with open(path, "r") as f:
			return frozenset(
				itertools.filterfalse(
					operator.methodcaller('startswith', '//'),
					filter(None, map(operator.methodcaller('strip'), f))))

	def __init__(self, path: typing.Optional[pathlib.Path] = None):
		"""Create a PSL Database from PATH."""
		if path is None:
			path = pathlib.Path(tempfile.gettempdir()) / "python-psl"

		if not path.exists():
			# Populate PSL path
			PSL.update_psl(path)

		self.psl = PSL._parse_psl(path)

	def update(self, path: pathlib.Path) -> None:
		"""Update the PSL stored internally from the internet, given a PATH."""
		PSL.update_psl(path)
		self.psl = PSL._parse_psl(path)
		self.fp_domain.cache_clear()


	IP_ADDR_NAIVE = re.compile(r'^\d+\.\d+\.\d+\.\d+$|^\[[\da-zA-Z:]+\]$')
	@functools.lru_cache(maxsize=2**10)
	def fp_domain(self, host: str) -> str:
		"""Get a first party domain for a given HOST.

		DOES NOT ACCEPT URLs, ONLY PLAIN HOSTS."""
		if self.IP_ADDR_NAIVE.search(host):
			return host

		tld, first_part = host, ''
		while tld:
			wildcard_tld, exception_tld = '*.' + tld, '!' + tld
			if exception_tld in self.psl:
				return tld
			if tld in self.psl:
				if first_part:
					return first_part + '.' + tld
				return tld
			if wildcard_tld in self.psl:
				if first_part:
					return first_part + '.' + tld
				return tld
			first_part, _, tld = tld.partition('.')
		# We have no idea what's going on, fallback to assuming last block is TLD
		return ".".join(host.rsplit('.', 2)[-2:])
