#!/usr/bin/env python3

#if the 3rd column is 3R/2L etc is one of those, count it
#if it has an @, skip, don't count it
#to find perfect alignments find NM:i:0 's in the list
import sys

if len(sys.argv) > 1:
    f = open( sys.argv[1] )
else:
    f = sys.stdin
num_perfect_alignments = 0

for line in f:
    if "NH:i:1" in line:
        num_perfect_alignments += 1
print(num_perfect_alignments)