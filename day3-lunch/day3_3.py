#!/usr/bin/env python3

import sys

PC = {}
NPC = {}

my_dist = 0
gene_start = 0
gene_end = 0
find_pos = int(21378950)

for i, line in enumerate(open(sys.argv[1])):
	if i <= 5:
		continue
	fields = line.rstrip("\r\n").split("\t")
	read_type = fields[2] 
	chromosome = fields[0]
	#gene_names = fields[9]
	gene_start = int(fields[3])
	gene_end = int(fields[4])
	gene_name = fields[8]
	
	if read_type == "gene" and chromosome == "3R":
		
		if "protein_coding" in fields[8]:
			fields = line.rstrip("\r\n").split()
			gene_biotypes = fields[17]
	
			if find_pos < gene_start:
				my_dist = gene_start - find_pos
			elif find_pos > gene_end:
				my_dist = find_pos - gene_end
				PC[gene_name] = my_dist
				
		else:
			fields = line.rstrip("\r\n").split()
			gene_biotypes = fields[17]
			#non protein coding genes distance from interest
			if find_pos < gene_start:
				my_dist = gene_start - find_pos
			elif find_pos > gene_end:
				my_dist = find_pos - gene_end
				NPC[gene_name] = my_dist
			
#this prints our whole dictionaries
# for name, value in PC.items():
# 	print(name[9:19], value)
# for name, value in NPC.items():
# 	print(name[9:19], value)

# minimum = min(PC, gene_name=PC.get)
# print(minimum, PC[minimum])

# d = {a:1, b:2, c:3}
# d.items() --> [(a,1), (b,2), (c,3)]

##this prints our 
sorted_PC = sorted(PC.items(), key=lambda x:x[1])
min_line, min_dist = sorted_PC[0]
print(min_line[9:19], min_dist)
sorted_NPC = sorted(NPC.items(), key=lambda x:x[1])
min_line, min_dist = sorted_NPC[0]
print(min_line[9:19], min_dist)

#print(sorted_NPC[0])

# lambda x:x[1]
#
# def lambda(x):
# 	return x[1]