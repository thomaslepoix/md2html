#!/usr/bin/python3

import argparse

#example
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--flag', action='store_true', default=False)  # can 'store_false' for no-xxx flags
    parser.add_argument('-r', '--reqd', required=True)
    parser.add_argument('-o', '--opt', default='fallback')
    parser.add_argument('arg', nargs='*') # use '+' for 1 or more args (instead of 0 or more)
    parsed = parser.parse_args()
    # NOTE: args with '-' have it replaced with '_'
    print('Result:',  vars(parsed))
    print('parsed.reqd:', parsed.reqd)

def main():
	parser = argparse.ArgumentParser(description='Simple markdown to html converter')
	parser.add_argument('-v', '--verbose', action='store_true', help='Verbose mode')
	parser.add_argument('-i', '--input', nargs='+', required=True, help='Input files or directory')
	parser.add_argument('-o', '--output', nargs=1, default='./', help='Output directory')
	parser.add_argument('-m', '--multiline-emphasis', action='store_true', help='Allow multiline emphasis (bold & italic)')

	args = parser.parse_args()

	if args.multiline_emphasis == True:
		print('-m ok')
	else:
		print('-m ko')
	if args.input:
		print(args.input)
	else:
		print('-i ko')

if __name__ == "__main__":
    main()
