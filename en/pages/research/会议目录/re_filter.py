# code: UTF-8

import sys
import re
import pprint

argv = sys.argv

if len(argv) < 2:
    print("need filename")
    sys.exit(1)

fname = argv[1]

f = open(fname, "r")
lines = f.readlines()
f.close()

for index, line in enumerate(lines[:]):
    # print(index, line)
    new_s = re.sub(r'^[ ]*-.*!.*\n', "", line)
    if new_s == "":
        lines.remove(line)

for index, line in enumerate(lines[:]):
    new_s = re.sub(r'^[ ]+\[', "- [", line)
    lines[index] = new_s


f = open(fname, "w")

mul_newline = False
for line in lines:
    if line.strip() == "":
        if mul_newline:
            continue
        mul_newline = True
    else:
        mul_newline = False
    print(line, file=f, end='')

f.close()
