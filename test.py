#!/usr/bin/python3

import unittest

from md2html import md2html_preserve_escaped
from md2html import md2html_restore_escaped


class TestPreserveEscaped(unittest.TestCase):
	def test_backslash(self):
		self.assertEqual(md2html_preserve_escaped(r'\\'), r'MD2HTMLBACKSLASH')
	def test_tick(self):
		self.assertEqual(md2html_preserve_escaped(r'\`'), r'MD2HTMLTICK')
	def test_asterisk(self):
		self.assertEqual(md2html_preserve_escaped(r'\*'), r'MD2HTMLASTERISK')
	def test_underscore(self):
		self.assertEqual(md2html_preserve_escaped(r'\_'), r'MD2HTMLUNDERSCORE')
	def test_lcurlybrace(self):
		self.assertEqual(md2html_preserve_escaped(r'\{'), r'MD2HTMLLCURLYBRACE')
	def test_rcurlybrace(self):
		self.assertEqual(md2html_preserve_escaped(r'\}'), r'MD2HTMLRCURLYBRACE')
	def test_lbracket(self):
		self.assertEqual(md2html_preserve_escaped(r'\['), r'MD2HTMLLBRACKET')
	def test_rbracket(self):
		self.assertEqual(md2html_preserve_escaped(r'\]'), r'MD2HTMLRBRACKET')
	def test_lparenthese(self):
		self.assertEqual(md2html_preserve_escaped(r'\('), r'MD2HTMLLPARENTHESE')
	def test_rparenthese(self):
		self.assertEqual(md2html_preserve_escaped(r'\)'), r'MD2HTMLRPARENTHESE')
	def test_pound(self):
		self.assertEqual(md2html_preserve_escaped(r'\#'), r'MD2HTMLPOUND')
	def test_plus(self):
		self.assertEqual(md2html_preserve_escaped(r'\+'), r'MD2HTMLPLUS')
	def test_minus(self):
		self.assertEqual(md2html_preserve_escaped(r'\-'), r'MD2HTMLMINUS')
	def test_dot(self):
		self.assertEqual(md2html_preserve_escaped(r'\.'), r'MD2HTMLDOT')
	def test_exclamation(self):
		self.assertEqual(md2html_preserve_escaped(r'\!'), r'MD2HTMLEXCLAMATION')
	def test_all(self):
		self.assertEqual(md2html_preserve_escaped(r'\\\`\*\_\{\}\[\]\(\)\#\+\-\.\!'), r'MD2HTMLBACKSLASHMD2HTMLTICKMD2HTMLASTERISKMD2HTMLUNDERSCOREMD2HTMLLCURLYBRACEMD2HTMLRCURLYBRACEMD2HTMLLBRACKETMD2HTMLRBRACKETMD2HTMLLPARENTHESEMD2HTMLRPARENTHESEMD2HTMLPOUNDMD2HTMLPLUSMD2HTMLMINUSMD2HTMLDOTMD2HTMLEXCLAMATION')


class TestRestoreEscaped(unittest.TestCase):
	def test_backslash(self):
		self.assertEqual(md2html_restore_escaped(r'MD2HTMLBACKSLASH'), '\\')
	def test_tick(self):
		self.assertEqual(md2html_restore_escaped(r'MD2HTMLTICK'), r'`')
	def test_asterisk(self):
		self.assertEqual(md2html_restore_escaped(r'MD2HTMLASTERISK'), r'*')
	def test_underscore(self):
		self.assertEqual(md2html_restore_escaped(r'MD2HTMLUNDERSCORE'), r'_')
	def test_lcurlybrace(self):
		self.assertEqual(md2html_restore_escaped(r'MD2HTMLLCURLYBRACE'), r'{')
	def test_rcurlybrace(self):
		self.assertEqual(md2html_restore_escaped(r'MD2HTMLRCURLYBRACE'), r'}')
	def test_lbracket(self):
		self.assertEqual(md2html_restore_escaped(r'MD2HTMLLBRACKET'), r'[')
	def test_rbracket(self):
		self.assertEqual(md2html_restore_escaped(r'MD2HTMLRBRACKET'), r']')
	def test_lparenthese(self):
		self.assertEqual(md2html_restore_escaped(r'MD2HTMLLPARENTHESE'), r'(')
	def test_rparenthese(self):
		self.assertEqual(md2html_restore_escaped(r'MD2HTMLRPARENTHESE'), r')')
	def test_pound(self):
		self.assertEqual(md2html_restore_escaped(r'MD2HTMLPOUND'), r'#')
	def test_plus(self):
		self.assertEqual(md2html_restore_escaped(r'MD2HTMLPLUS'), r'+')
	def test_minus(self):
		self.assertEqual(md2html_restore_escaped(r'MD2HTMLMINUS'), r'-')
	def test_dot(self):
		self.assertEqual(md2html_restore_escaped(r'MD2HTMLDOT'), r'.')
	def test_exclamation(self):
		self.assertEqual(md2html_restore_escaped(r'MD2HTMLEXCLAMATION'), r'!')
	def test_all(self):
		self.assertEqual(md2html_restore_escaped(r'MD2HTMLBACKSLASHMD2HTMLTICKMD2HTMLASTERISKMD2HTMLUNDERSCOREMD2HTMLLCURLYBRACEMD2HTMLRCURLYBRACEMD2HTMLLBRACKETMD2HTMLRBRACKETMD2HTMLLPARENTHESEMD2HTMLRPARENTHESEMD2HTMLPOUNDMD2HTMLPLUSMD2HTMLMINUSMD2HTMLDOTMD2HTMLEXCLAMATION'), r'\`*_{}[]()#+-.!')

if __name__ == "__main__":
	unittest.main(verbosity=2)

