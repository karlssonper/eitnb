#!/usr/bin/env python
import sys
import argparse

parser = argparse.ArgumentParser(description="Eighty is the new black")
parser.add_argument("textfile", help = "Input textfile to check")
parser.add_argument("-kws","--killwhitespaces", action="store_true",
                    help="Kill all whitespaces at the end of a line")
parser.add_argument("-kbl","--killblanklines", action="store_true",
                    help="Kill consecutive blank new lines")
parser.add_argument("-ns", "--nostats", action="store_true",
                    help="Print stats after run")
parser.add_argument("-v", "--verbose", action="store_true",
                    help="Output every line larger than specified width")
parser.add_argument("-w", "--width", default = "80", type=int,
                    help="Allowed width")
args = parser.parse_args()

w = args.width
nw, nws, nbl = 0,0,0
f = open(args.textfile)
lines = f.read().split("\n")
f.close()
rw = len(str(len(lines))) # row width
removeLines = []
for row,line in enumerate(lines):
    if not len(line):
        continue
    rowStr ="%3i" % (row + 1) if rw >= 3 else "%2i" % (row + 1)
    if len(line) > w:
        nw += 1
        if args.verbose:
            # Print everything > width as red
            print "%s:%s\033[91m%s\033[0m" % (rowStr,line[:w],line[w:])
    if line[-1] == " ":
        nws += 1
        N = 1
        while len(line) > N and line[-N] == " ":
            N+=1
        lines[row] = line[:-N] if N == len(line) else line[:-N+1]

        if args.verbose:
            # Print ending whitespaces as yellow
            print "%s:%s\033[93m%s\033[0m" %(rowStr,lines[row],"_"*(N-1))

if args.killblanklines or args.killwhitespaces:
    f = open(args.textfile, "w")

prevBlank = False
for line in lines:
    if (not prevBlank) or len(line):
        if args.killblanklines:
            f.write(line + "\n")
    else:
        nbl += 1
    prevBlank = not len(line)

if not args.killblanklines and args.killwhitespaces:
    for line in lines:
        f.write(line + "\n")

if not args.nostats:
    print "Number of lines with witdh > %i: %i/%i (%.2f%%)" \
        % (w, nw, len(lines), 100*nw/float(len(lines)))
    print "Number of lines with ending whitespaces: %i/%i (%.2f%%)" \
        % (nws, len(lines), 100*nws/float(len(lines)))
    print "Number of consecutive blank lines: %i/%i (%.2f%%)" \
        % (nbl, len(lines), 100*nbl/float(len(lines)))

