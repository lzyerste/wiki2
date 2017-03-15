import re
import os
import sys


def handle_file(filename):
    filename = filename.strip()
    if not os.path.exists(filename): return
    fin = open(filename)
    lines = [line.strip() for line in fin.read().split("\n") if line.strip() != ""]
    fin.close()
    fout = open(filename, "w")
    title = lines[0]
    title = re.sub(r'^[# ]*', '', title).strip()
    print("# " + title + "\n", file=fout)
    for line in lines[1:]:
        line = re.sub(r"^([a-zA-Z].*?:)", "**\\1**", line)
        print(line + "\n", file=fout)
    fout.close()


for line in sys.stdin:
    handle_file(line)
