#!/usr/bin/python3

import unittest

from md2html import md2html_preserve_escaped
from md2html import md2html_restore_escaped
from md2html import md2html_headings


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
		self.assertEqual(md2html_restore_escaped('MD2HTMLBACKSLASH'), '\\')
	def test_tick(self):
		self.assertEqual(md2html_restore_escaped('MD2HTMLTICK'), '`')
	def test_asterisk(self):
		self.assertEqual(md2html_restore_escaped('MD2HTMLASTERISK'), '*')
	def test_underscore(self):
		self.assertEqual(md2html_restore_escaped('MD2HTMLUNDERSCORE'), '_')
	def test_lcurlybrace(self):
		self.assertEqual(md2html_restore_escaped('MD2HTMLLCURLYBRACE'), '{')
	def test_rcurlybrace(self):
		self.assertEqual(md2html_restore_escaped('MD2HTMLRCURLYBRACE'), '}')
	def test_lbracket(self):
		self.assertEqual(md2html_restore_escaped('MD2HTMLLBRACKET'), '[')
	def test_rbracket(self):
		self.assertEqual(md2html_restore_escaped('MD2HTMLRBRACKET'), ']')
	def test_lparenthese(self):
		self.assertEqual(md2html_restore_escaped('MD2HTMLLPARENTHESE'), '(')
	def test_rparenthese(self):
		self.assertEqual(md2html_restore_escaped('MD2HTMLRPARENTHESE'), ')')
	def test_pound(self):
		self.assertEqual(md2html_restore_escaped('MD2HTMLPOUND'), '#')
	def test_plus(self):
		self.assertEqual(md2html_restore_escaped('MD2HTMLPLUS'), '+')
	def test_minus(self):
		self.assertEqual(md2html_restore_escaped('MD2HTMLMINUS'), '-')
	def test_dot(self):
		self.assertEqual(md2html_restore_escaped('MD2HTMLDOT'), '.')
	def test_exclamation(self):
		self.assertEqual(md2html_restore_escaped('MD2HTMLEXCLAMATION'), '!')
	def test_all(self):
		self.assertEqual(md2html_restore_escaped('MD2HTMLBACKSLASHMD2HTMLTICKMD2HTMLASTERISKMD2HTMLUNDERSCOREMD2HTMLLCURLYBRACEMD2HTMLRCURLYBRACEMD2HTMLLBRACKETMD2HTMLRBRACKETMD2HTMLLPARENTHESEMD2HTMLRPARENTHESEMD2HTMLPOUNDMD2HTMLPLUSMD2HTMLMINUSMD2HTMLDOTMD2HTMLEXCLAMATION'), '\`*_{}[]()#+-.!')


class TestHeadings(unittest.TestCase):
	def test_heading1(self):
		self.assertEqual(md2html_headings('# HEADING 1'), '<h1>HEADING 1</h1>')
		self.assertEqual(md2html_headings('HEADING 1\n===='), '<h1>HEADING 1</h1>')
	def test_heading2(self):
		self.assertEqual(md2html_headings('## HEADING 2'), '<h2>HEADING 2</h2>')
		self.assertEqual(md2html_headings('HEADING 2\n----'), '<h2>HEADING 2</h2>')
	def test_heading3(self):
		self.assertEqual(md2html_headings('### HEADING 3'), '<h3>HEADING 3</h3>')
	def test_heading4(self):
		self.assertEqual(md2html_headings('#### HEADING 4'), '<h4>HEADING 4</h4>')
	def test_heading5(self):
		self.assertEqual(md2html_headings('##### HEADING 5'), '<h5>HEADING 5</h5>')
	def test_heading6(self):
		self.assertEqual(md2html_headings('###### HEADING 6'), '<h6>HEADING 6</h6>')


if __name__ == "__main__":
	unittest.main(verbosity=2)

