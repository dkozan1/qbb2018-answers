#!/usr/bin/env python3

import sys

if len(sys.argv) > 1:
    f = open( sys.argv[1] )
else:
    f = sys.stdin


for line in f:
	fields = line.rstrip("\r\n").split()
	if "DROME" in line:
		if len(fields) == 4:
		
			print(fields[3] + "    " + fields[2])