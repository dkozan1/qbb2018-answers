#!/usr/bin/env python3

import sys

#create dictionary to print key (FBGN) and ctab line corresponding
fly_dict = {}

##This function finds the last two columns in the fly.txt document
def fun_dict1(fname):
	##opent the file provided
	for line in open(fname):
		if "DROME" and "FBgn" in line:
			fields = line.rstrip("\r\n").split()
			#these two fields are the last two columns containing FlyBAse and UniProt 
			fly_dict[fields[3]] = fields[2]
			
			
##This function takes the gene name column in c-tab file to match to our dictionary containing the key FBGN and assigned Uniprot value
def fun_dict2(fname):
	##open file provided
	for line in open(fname):
		##FBGn designated gene name so we cut for that
		if "FBgn" in line:
			fields = line.rstrip("\r\n").split()
			if fields[8] in fly_dict.keys():
				print(fly_dict[fields[8]], "\t" ,line)
				##if the two documents do not correspond a FlyBase and genename together, then no Uniprot ID can be matched and "No match" prints out in the first column for reference. 
			else:
				print("No match")

##these commands are so important!!! They take the files you reference in the command line and reference them to your function via dictionary created
Output1 = fun_dict1(sys.argv[1])
Output2 = fun_dict2(sys.argv[2])