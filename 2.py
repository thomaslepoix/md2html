#!/usr/bin/python3

import re

with open('test.md', encoding='utf-8') as in_file:
	in_text = in_file.read()

print(in_text)
print('================================================================================')

# Headings
in_text = re.sub(r'^([^\n#].*)\n(=+)$', r'<h1>\g<1></h1>', in_text, flags=re.M)
in_text = re.sub(r'^([^\n#].*)\n(-+)$', r'<h2>\g<1></h2>', in_text, flags=re.M)
in_text = re.sub(r'^# ?([^#].*)$', r'<h1>\g<1></h1>', in_text, flags=re.M)
in_text = re.sub(r'^## ?([^#].*)$', r'<h2>\g<1></h2>', in_text, flags=re.M)
in_text = re.sub(r'^### ?([^#].*)$', r'<h3>\g<1></h3>', in_text, flags=re.M)
in_text = re.sub(r'^#### ?([^#].*)$', r'<h4>\g<1></h4>', in_text, flags=re.M)
in_text = re.sub(r'^##### ?([^#].*)$', r'<h5>\g<1></h5>', in_text, flags=re.M)
in_text = re.sub(r'^###### ?([^#].*)$', r'<h6>\g<1></h6>', in_text, flags=re.M)

# Enphasis
in_text = re.sub(r'__(.*?)__|\*\*(.*?)\*\*', r'<strong>\g<1>\g<2></strong>', in_text, flags=re.S)
in_text = re.sub(r'_(.*?)_|\*(.*?)\*', r'<em>\g<1>\g<2></em>', in_text, flags=re.S)

# Paragraphs
#in_text = re.sub(r'(?:^|\n\n)(\<.*?\>|(.*?))(?=\n\n|$)', r'\n<p>\g<2></p>\n', in_text, flags=re.S)

# Line Breaks
#in_text = re.sub(r' {2,}$', r'<br>', in_text, flags=re.M)



with open('test.html', 'w', encoding='utf-8') as out_file:
	out_file.write(in_text)
	print(in_text)
