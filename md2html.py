#!/usr/bin/python3

import argparse
import re
#import pathlib
#import os.path


def parse_args():
	parser = argparse.ArgumentParser(description='Simple markdown to HTML converter')
	parser.add_argument('-v', '--verbose', action='store_true', help='Verbose mode')
	parser.add_argument('-i', '--input', nargs='+', required=True, help='Input files or directory')
	parser.add_argument('-o', '--output', nargs=1, default=('./',), help='Output directory')
	parser.add_argument('-t', '--template', nargs=1, help='HTML template file')
	parser.add_argument('-r', '--recursive', action='store_true', help='Acess directories recursively')
	parser.add_argument('-m', '--multiline-emphasis', action='store_const', const='S', default='M', help='Allow multiline emphasis (bold & italic)')

	for inp in args.input:
		if not os.path.exists(inp):
			print('ERROR : '+inp+' does not exist')
			exit(1)
	if not os.path.exists(args.output) or not os.path.isdir(args.output):
		print('ERROR : '+args.output+' does not exist or in not a directory')
		exit(1)
	if args.template:
		if not os.path.exists(args.template) or not os.path.isfile(args.template):
			print('ERROR : '+args.template+' does not exist or in not a file')
			exit(1)

	args.output = re.sub(r'^(.*)/?$', r'\g<1>/', args.output, flags=re.M)
	return parser.parse_args()


def md2html_preserve_escaped(in_text):
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
	return in_text


def md2html_code(in_text):
	def re_code_lang(matchobj):
		if matchobj.group(1):
			return r'<pre><code class="language-'+matchobj.group(1)+'">'+matchobj.group(2)+'</code></pre>'
		else:
			return r'<pre><code>'+matchobj.group(2)+'</code></pre>'

	in_text = re.sub(r'```([^\n]*)?\n(.*?)\n```', re_code_lang, in_text, flags=re.S)
	in_text = re.sub(r'``?(.*?)``?', r'<pre><code>\g<1></code></pre>', in_text, flags=re.S)
	# code -> MD2HTMLxPROTECTED ; dictionnaire x - code


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


#lists
#(?<=\n)[-*+] ?(.*?)\n
#(?<=\n)(\t|    )?[-*+] ?(.*?)\n
#(?<=\n)((\t|    )?[-*+] ?.*?)\n?(?=\n(\t|    )?[^-*+])
#https://regex101.com/r/x2pj7O/1

#paragraphs
#(?=(?:^|\n\n)(.*?)(?=$|\n\n))(?:.*?)(?=$|\n\n)
#https://regex101.com/r/x2pj7O/2
#(?:(?<=^)|(?<=\n\n))(.*?)(?=$|\n\n)
def md2html_paragraphs(in_text):
	in_text = re.sub(r'(?:(?<=^)|(?<=\n\n))((?!<h.*?>|MD2HTML.*?PROTECTED).*?)(?=$|\n\n)', r'<p>\g<1></p>', in_text, flags=re.S)
	return in_text


def md2html_separators(in_text):
	in_text = re.sub(r'^-{3,}$|^_{3,}$|^\*{3,}$', r'<hr>', in_text, flags=re.M)
	in_text = re.sub(r' {2,}$', r'<br>', in_text, flags=re.M)


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
#		in_text = md2html_code(in_text)
		in_text = md2html_headings(in_text)
		in_text = md2html_emphasis(in_text, args.multiline_emphasis)
		in_text = md2html_serapators(in_text)
		in_text = md2html_restore_escaped(in_text)

		if args.verbose:
			print(in_text)

		if args.template:
			with open(args.template, encoding='utf-8') as temp_file:
				in_text, n_match = re.subn(r'MD2HTMLTEMPLATE', in_text, temp_file.read(), flags=re.M)
				if n_match != 1:
					print("ERROR : "+args.template+" seems to be invalid.\n"
						+"\tPlease ensure the template contain ONE time the string \"MD2HTMLTEMPLETE\".")
					exit(1)

#^/.*/(.*)(\.md)?$|^[^/](.*)(\.md)?$
		out_name = re.sub(r'', args.output+r'\g<1>.html', in_name, flags=re.M)
		with open(out_name, 'w', encoding='utf-8') as out_file:
			out_file.write(in_text)


if __name__ == "__main__":
	main()
