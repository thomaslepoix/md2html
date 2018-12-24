#!/usr/bin/python3

import argparse
import re


def parse_args():
	parser = argparse.ArgumentParser(description='Simple markdown to HTML converter')
	parser.add_argument('-v', '--verbose', action='store_true', help='Verbose mode')
	parser.add_argument('-i', '--input', nargs='+', required=True, help='Input files or directory')
	parser.add_argument('-o', '--output', nargs=1, default='./', help='Output directory')
	parser.add_argument('-t', '--template', nargs=1, help='HTML template file')
	parser.add_argument('-m', '--multiline-emphasis', action='store_const', const='S', default='M', help='Allow multiline emphasis (bold & italic)')
	return parser.parse_args()


def md2html_preserve_escaped(in_text):
#	print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n'
#		+'preserve_escaped input : '+in_text+'\n'
#		+'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
	in_text = re.sub(r'\\\\', r'MD2HTMLBACKSLASH', in_text, flags=re.M)
	in_text = re.sub(r'\\`', r'MD2HTMLTICK', in_text, flags=re.M)
	in_text = re.sub(r'\\\*', r'MD2HTMLASTERISK', in_text, flags=re.M)
	in_text = re.sub(r'\\_', r'MD2HTMLUNDERSCORE', in_text, flags=re.M)
	in_text = re.sub(r'\\{', r'MD2HTMLLCURLYBRACE', in_text, flags=re.M)
	in_text = re.sub(r'\\}', r'MD2HTMLRCURLYBRACE', in_text, flags=re.M)
	in_text = re.sub(r'\\\[', r'MD2HTMLLBRACKET', in_text, flags=re.M)
	in_text = re.sub(r'\\\]', r'MD2HTMLRBRACKET', in_text, flags=re.M)
	in_text = re.sub(r'\\\(', r'MD2HTMLLPARENTHESE', in_text, flags=re.M)
	in_text = re.sub(r'\\\)', r'MD2HTMLRPARENTHESE', in_text, flags=re.M)
	in_text = re.sub(r'\\#', r'MD2HTMLPOUND', in_text, flags=re.M)
	in_text = re.sub(r'\\\+', r'MD2HTMLPLUS', in_text, flags=re.M)
	in_text = re.sub(r'\\\-', r'MD2HTMLMINUS', in_text, flags=re.M)
	in_text = re.sub(r'\\\.', r'MD2HTMLDOT', in_text, flags=re.M)
	in_text = re.sub(r'\\!', r'MD2HTMLEXCLAMATION', in_text, flags=re.M)
#	print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n'
#		+'preserve_escaped output : '+in_text+'\n'
#		+'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
	return in_text


#code


def md2html_headings(in_text):
	in_text = re.sub(r'^([^\n#].*)\n(=+)$', r'<h1>\g<1></h1>', in_text, flags=re.M)
	in_text = re.sub(r'^([^\n#].*)\n(-+)$', r'<h2>\g<1></h2>', in_text, flags=re.M)
	in_text = re.sub(r'^# ?([^#].*)$', r'<h1>\g<1></h1>', in_text, flags=re.M)
	in_text = re.sub(r'^## ?([^#].*)$', r'<h2>\g<1></h2>', in_text, flags=re.M)
	in_text = re.sub(r'^### ?([^#].*)$', r'<h3>\g<1></h3>', in_text, flags=re.M)
	in_text = re.sub(r'^#### ?([^#].*)$', r'<h4>\g<1></h4>', in_text, flags=re.M)
	in_text = re.sub(r'^##### ?([^#].*)$', r'<h5>\g<1></h5>', in_text, flags=re.M)
	in_text = re.sub(r'^###### ?([^#].*)$', r'<h6>\g<1></h6>', in_text, flags=re.M)
	return in_text


def md2html_emphasis(in_text, multiline):
	in_text = re.sub(r'__(.*?)__|\*\*(.*?)\*\*', r'<strong>\g<1>\g<2></strong>', in_text, flags=eval('re.'+multiline))
	in_text = re.sub(r'_(.*?)_|\*(.*?)\*', r'<em>\g<1>\g<2></em>', in_text, flags=eval('re.'+multiline))
	return in_text


def md2html_restore_escaped(in_text):
	in_text = re.sub(r'MD2HTMLBACKSLASH', r'\\', in_text, flags=re.M)
	in_text = re.sub(r'MD2HTMLTICK', r'`', in_text, flags=re.M)
	in_text = re.sub(r'MD2HTMLASTERISK', r'*', in_text, flags=re.M)
	in_text = re.sub(r'MD2HTMLUNDERSCORE', r'_', in_text, flags=re.M)
	in_text = re.sub(r'MD2HTMLLCURLYBRACE', r'{', in_text, flags=re.M)
	in_text = re.sub(r'MD2HTMLRCURLYBRACE', r'}', in_text, flags=re.M)
	in_text = re.sub(r'MD2HTMLLBRACKET', r'[', in_text, flags=re.M)
	in_text = re.sub(r'MD2HTMLRBRACKET', r']', in_text, flags=re.M)
	in_text = re.sub(r'MD2HTMLLPARENTHESE', r'(', in_text, flags=re.M)
	in_text = re.sub(r'MD2HTMLRPARENTHESE', r')', in_text, flags=re.M)
	in_text = re.sub(r'MD2HTMLPOUND', r'#', in_text, flags=re.M)
	in_text = re.sub(r'MD2HTMLPLUS', r'+', in_text, flags=re.M)
	in_text = re.sub(r'MD2HTMLMINUS', r'-', in_text, flags=re.M)
	in_text = re.sub(r'MD2HTMLDOT', r'.', in_text, flags=re.M)
	in_text = re.sub(r'MD2HTMLEXCLAMATION', r'!', in_text, flags=re.M)
	return in_text


def main():
	args = parse_args()

	in_files = args.input
	for in_name in in_files:
		with open(in_name, encoding='utf-8') as in_file:
			in_text = in_file.read()

		if args.verbose:
			print(in_text)
			print('================================================================================')

		in_text = md2html_preserve_escaped(in_text)
	#	in_text = md2html_code(in_text)
		in_text = md2html_headings(in_text)
		in_text = md2html_emphasis(in_text, args.multiline_emphasis)
		in_text = md2html_restore_escaped(in_text)

		if args.verbose:
			print(in_text)

	#	out_name = 
		with open(args.output+'test.html', 'w', encoding='utf-8') as out_file:
			out_file.write(in_text)


if __name__ == "__main__":
	main()
