#!/usr/bin/env python3

#if the 3rd column is 3R/2L etc is one of those, count it
#if it has an @, skip, don't count it
import sys

if len(sys.argv) > 1:
    f = open( sys.argv[1] )
else:
    f = sys.stdin
num_alignments = 0

for line in f:
    if line.startswith("@"):
        continue
    fields = line.rstrip("\r\n").split("\t")
    if fields[2] != "*":
        num_alignments += 1
        if num_alignments < 11:
            print(fields[2])
    else:
        break