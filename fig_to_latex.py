#!/usr/bin/env python
import csv
import argparse
import os
import re
from distutils.util import strtobool

FDIR = os.path.split(__file__)[0]
DEFOUTF = os.path.join(FDIR, "out.txt")
DEFINF = os.path.join(FDIR, "in.png")
parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("-i", "--input", type=str, default=DEFINF, help="input file")
parser.add_argument("-s", "--save", type=strtobool, default=False, help="to save")
parser.add_argument("-sf", "--subfigure", type=strtobool, default=False, help="is a subfigure")

parser.add_argument("-sz", "--size", type=float, default=5., help="size in cm")
parser.add_argument("-rsz", "--relsize", type=float, default=0.4, help="relative size for subfigure")
parser.add_argument("-a", "--as_width", type=strtobool, default=True, help="specify size as width (else height)")

parser.add_argument("-c", "--center", type=strtobool, default=True, help="center figure")
parser.add_argument("--capheader", type=strtobool, default=True, help="capitalize header")


args = parser.parse_args()
infile = args.input
fname = os.path.splitext(infile)[0]
outfile = fname + ".txt"
fname_p = re.sub(r'_', ' ', fname).title()
rstr = ""
if args.subfigure == True:
    rstr += "\\begin{figure*}[ht!]\n"
    if args.center == True:
        rstr += "\\captionsetup[subfigure]{justification=centering,position=bottom,font=scriptsize}\n"
        rstr += "\\caption{{{fname_p}}}\n"
        rstr += "\\centering\n"
    else:
        rstr += "\\captionsetup[subfigure]{position=bottom,font=scriptsize}\n"
    rstr += f"\\begin{{subfigure}}[t]{{  {args.relsize} \\textwidth}}\n"
else:
    rstr += "\\begin{figure}[ht]\n"
if args.center == True:
    rstr += "\\centering\n"
orientation_str = "width"
if args.as_width == False:
    orientation_str = "height"
if args.subfigure == True:
    rstr += f"\\includegraphics[ width=\\textwidth ]{{{args.input}}}\n"
else:
    rstr += f"\\includegraphics[{orientation_str}={args.size}cm]{{{args.input}}}\n"
    rstr += "\\captionsetup{font=scriptsize}\n"
rstr += f"\\caption{{{fname_p}}}\n"
rstr += f"\\label{{{fname}}}\n"
if args.subfigure == True:
    rstr += "\\end{subfigure}\n"
    rstr += "\\end{figure*}"
else:
    rstr += "\\end{figure}"
print("")
print(rstr)
print("")
