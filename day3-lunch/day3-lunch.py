#!/usr/bin/env python3

import sys

protein_coding = 0

for i, line in enumerate(open(sys.argv[1])):
	if i <= 5:
		continue
	fields = line.rstrip("\r\n").split("\t")
	if "protein_coding" in fields[8]: 
			
	 		if "gene" in fields[2]: 
	 	  		protein_coding += 1
				
print(protein_coding)
	