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

import pytest
import functools

from jmatrix import interceptor, rule, umatrix_parser
from jmatrix.vendor.fpdomain import fpdomain


WIDEN_TESTS = {
	"a.b.com": ("a.b.com", "b.com", "com", "*"),
	"start.duckduckgo.com": ("start.duckduckgo.com", "duckduckgo.com", "com", "*"),
	"": ("*",),
	"a.b.c.d.e.f": ("a.b.c.d.e.f", "b.c.d.e.f",
					"c.d.e.f", "d.e.f", "e.f", "f", "*"),
}


@pytest.mark.parametrize(('r', 'result'), WIDEN_TESTS.items())
def test_matrix_rule(r, result):
	assert interceptor._hostname_widen_list(r) == result

@pytest.mark.parametrize(('r', 'result'), WIDEN_TESTS.items())
def test_matrix_rule_benchmark(r, result, benchmark):
	benchmark(functools.partial(interceptor._hostname_widen_list, r))


# 'e2e' Tests for overall interceptor

OVERALL_TESTS = {
	("matrix-off: * true",): {"allow": [
		("gitlab.com", "http", "gitlab.com", "http", rule.Type.IMAGE),
		("git.gitlab.com", "http", "gitlab.com", "http", rule.Type.IMAGE),]},

	("* * * block",
	 "* * css allow",):
	{"allow": [
		("gitlab.com", "http", "gitlab.com", "http", rule.Type.CSS),],
	 "block": [
		 ("gitlab.com", "http", "gitlab.com", "http", rule.Type.XHR),],},

	("* * * block",
	 "* * css allow",):
	{"allow": [
		("gitlab.com", "http", "gitlab.com", "http", rule.Type.CSS),],
	 "block": [
		 ("gitlab.com", "http", "gitlab.com", "http", rule.Type.XHR),],},

	("* qutebrowser.bad * block",
	 "qutebrowser.org qutebrowser.bad * allow",):
	{"allow": [
		("qutebrowser.org", "http", "qutebrowser.bad", "http", rule.Type.CSS),
		("sub.qutebrowser.org", "http", "qutebrowser.bad", "http", rule.Type.CSS),
		("www.sub.qutebrowser.org", "http", "www.qutebrowser.bad", "http", rule.Type.CSS),],
	 "block": [
		 ("non-qutebrowser.org", "http", "qutebrowser.bad", "http", rule.Type.CSS),
		 ("non-qutebrowser.org", "http", "www.qutebrowser.bad", "http", rule.Type.CSS),],},

	("* * frame block",
	 "github.com githubassets.com * allow",):
	{"allow": [
		("github.com", "http", "githubassets.com", "http", rule.Type.CSS),
		("github.com", "http", "super.githubassets.com", "http", rule.Type.CSS),
		("super.github.com", "http", "super.githubassets.com", "http", rule.Type.CSS),
		("super.github.com", "http", "githubassets.com", "http", rule.Type.CSS),

	],
	 "block": [
		 ("github.com", "http", "qutebrowser.org", "http", rule.Type.CSS),
		 ("qutebrowser.org", "http", "githubassets.com", "http", rule.Type.CSS),
		 # TODO how should we block this
		 ("github.com", "http", "githubassets.com", "http", rule.Type.FRAME),
		 ("github.com", "http", "super.githubassets.com", "http", rule.Type.FRAME),
		 ("super.github.com", "http", "super.githubassets.com", "http", rule.Type.FRAME),
		 ],},

	("com * frame block",
	 "github.com githubassets.com * allow",):
	{"allow": [
		("github.com", "http", "githubassets.com", "http", rule.Type.CSS),
		("github.com", "http", "super.githubassets.com", "http", rule.Type.CSS),
		("super.github.com", "http", "super.githubassets.com", "http", rule.Type.CSS),
		("super.github.com", "http", "githubassets.com", "http", rule.Type.CSS),

	],
	 "block": [
		 ("github.com", "http", "qutebrowser.org", "http", rule.Type.CSS),
		 ("qutebrowser.org", "http", "githubassets.com", "http", rule.Type.CSS),
		 # TODO how should we block this
		 ("github.com", "http", "githubassets.com", "http", rule.Type.FRAME),
		 ("github.com", "http", "super.githubassets.com", "http", rule.Type.FRAME),
		 ("super.github.com", "http", "super.githubassets.com", "http", rule.Type.FRAME),
		 ],},

	("* * xhr allow",
	 "github.com githubassets.com * block",):
	{"allow": [
		("qutebrowser.org", "http", "qutebrowser.org", "http", rule.Type.XHR),
		("github.com", "http", "github.com", "http", rule.Type.XHR),
		("super.github.com", "http", "github.com", "http", rule.Type.XHR),
		("github.com", "http", "super.github.com", "http", rule.Type.XHR),
		("super.github.com", "http", "super.github.com", "http", rule.Type.XHR),
		("qutebrowser.org", "http", "qutebrowser.org", "http", rule.Type.XHR),],
	 "block": [
		 ("github.com", "http", "githubassets.org", "http", rule.Type.CSS),
		 ("super.github.com", "http", "super.githubassets.org", "http", rule.Type.CSS),
		 ("qutebrowser.org", "http", "githubassets.com", "http", rule.Type.CSS),
		 # TODO how should we block this
		 ("github.com", "http", "githubassets.com", "http", rule.Type.XHR),
		 ("super.github.com", "http", "githubassets.com", "http", rule.Type.XHR),
		 ("github.com", "http", "super.githubassets.com", "http", rule.Type.XHR),
		 ("super.github.com", "http", "super.githubassets.com", "http", rule.Type.XHR),],},

	("* * * block",
	 "* 1st-party * allow",):
	{"allow": [
		("qutebrowser.org", "http", "qutebrowser.org", "http", rule.Type.XHR),
		("github.com", "http", "github.com", "http", rule.Type.XHR),
		("qutebrowser.org", "http", "qutebrowser.org", "http", rule.Type.XHR),
		("github.com", "http", "super.github.com", "http", rule.Type.XHR),
		("super.github.com", "http", "super.github.com", "http", rule.Type.XHR),
		("qutebrowser.org", "http", "qutebrowser.org", "http", rule.Type.XHR),
		("twitch.tv", "http", "twitch.tv", "http", rule.Type.OTHER),],
	 "block": [
		("qutebrowser.org", "http", "gitlab.com", "http", rule.Type.XHR),],},

	("* * * block",
	 "matrix-off: qute-scheme true",):
	{"allow": [
		("version", "qute", "version", "qute", rule.Type.XHR),],
	 "block": [("qutebrowser.org", "http", "qutebrowser.org", "http", rule.Type.XHR),],},

	("* * * block",
	 "matrix-off: qute-scheme true",):
	{"allow": [
		("version", "qute", "version", "qute", rule.Type.XHR),],
	 "block": [("qutebrowser.org", "http", "qutebrowser.org", "http", rule.Type.XHR),],},


	# HTTPS-Strict Test
	("* 1st-party * allow",
	 "https-strict: qutebrowser.org true",):
	{"allow": [
		("qutebrowser.org", "https", "qutebrowser.org", "https", rule.Type.CSS),
		("super.qutebrowser.org", "https", "qutebrowser.org", "https", rule.Type.CSS),
		("qutebrowser.org", "https", "super.qutebrowser.org", "https", rule.Type.CSS),
		("super.qutebrowser.org", "https", "super.qutebrowser.org", "https", rule.Type.CSS),

		("qutebrowser.org", "http", "qutebrowser.org", "https", rule.Type.CSS),
	],
	 "block": [
		("qutebrowser.org", "https", "qutebrowser.org", "http", rule.Type.CSS),
		("super.qutebrowser.org", "https", "qutebrowser.org", "http", rule.Type.CSS),
		("qutebrowser.org", "https", "super.qutebrowser.org", "http", rule.Type.CSS),
		("super.qutebrowser.org", "https", "super.qutebrowser.org", "http", rule.Type.CSS),],},
}

PSL = None
@pytest.fixture(scope="session")
def psl():
	global PSL
	PSL = fpdomain.PSL()
	return PSL.fp_domain

@pytest.mark.parametrize(('r_text', 'result'), OVERALL_TESTS.items())
def test_matrix_overall(r_text, result, psl):
	rule_obj = rule.Rules()
	umatrix_parser.rules_to_map(r_text, rule_obj)
	for blocked_rule in result.get('block', []):
		args = blocked_rule + (psl, rule_obj)
		assert interceptor.should_block(*args)
	for passed_rule in result.get('allow', []):
		args = passed_rule + (psl, rule_obj,)
		assert not interceptor.should_block(*args)


def test_benchmark_null_match(psl, benchmark):
	"""Benchmarks the most complicated (ironically) match, the null match."""
	rule_obj = rule.Rules()
	umatrix_parser.rules_to_map(["* * * block"], rule_obj)
	benchmark(functools.partial(
		interceptor.should_block,
		"a.b.c.d.e.f.g", "http", "cdn.a.b.c.d.e.f.g", "http",
		rule.Type.FRAME, psl, rule_obj))

@pytest.fixture(scope="session")
def stock_rules():
	with open("tests/data/stock-rules") as f:
		lines = f.readlines()
	return lines

def test_benchmark_complex_null_match(stock_rules, psl, benchmark):
	"""Benchmarks the null match with lots of extra rules."""
	rule_obj = rule.Rules()
	umatrix_parser.rules_to_map(stock_rules, rule_obj)
	benchmark(functools.partial(
		interceptor.should_block,
		"a.b.c.d.e.f.g", "http", "cdn.a.b.c.d.e.f.g", "http",
		rule.Type.FRAME, psl, rule_obj))

def test_benchmark_complex_block(stock_rules, psl, benchmark):
	"""Benchmarks a particularly slow match I found."""
	rule_obj = rule.Rules()
	umatrix_parser.rules_to_map(stock_rules, rule_obj)
	# http://www.redditstatic.com/desktop2x/fonts/IBMPlexSans/Regular-e6bbcdd30d3bd4d6b170bcb6d3552cab.woff
	benchmark(functools.partial(
		interceptor.should_block,
		"www.redditstatic.com", "http", "www.reddit.com", "http",
		rule.Type.OTHER, psl, rule_obj))
