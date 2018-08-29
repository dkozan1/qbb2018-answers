#!/usr/bin/env python3

import sys

protein_coding = 0
gene_types = {}

for i, line in enumerate( open( sys.argv[1])):
	if i <= 5:
		continue
	fields = line.rstrip("\r\n").split("\t")
	read_type = fields[2] 
	if read_type == "gene":
		fields = line.rstrip("\r\n").split()
		gene_biotypes = fields[17]
		
		if gene_biotypes in gene_types:
			gene_types[gene_biotypes] += 1
				
		else:
			gene_types[gene_biotypes] = 1

for name, value in gene_types.items():
	print(name, value)