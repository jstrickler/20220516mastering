import sys
import re
import fileinput
from argparse import ArgumentParser

description = """
Prints lines containing a regular expression
pattern.
"""


parser = ArgumentParser(description=description)

parser.add_argument('-i', dest="ignore_case", action="store_true", help="ignore case")
parser.add_argument('-f', action="store_true", dest="show_files", help="show file name")
parser.add_argument('pattern', help="pattern (regex) to find")
parser.add_argument('files', nargs="+", help="files to search")

args = parser.parse_args()  # parse sys.argv[1:]
# print(args)


regex = re.compile(args.pattern, re.I if args.ignore_case else 0)

for raw_line in fileinput.input(args.files):
    if regex.search(raw_line):
        line = raw_line.rstrip()
        if args.show_files:
            print(fileinput.filename(), end=" ")
        print(line)
