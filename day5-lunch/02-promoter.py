#!/usr/bin/env python3

"""
Usage: ./02-promoter.py <~/data/results/stringtie/SRR072893/ctab
Find start site promoter region transcripts in ctab file. 
"""

import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

promoter_start = []
promoter_end = []

coi = ["chr", "start", "end", "t_name"]
ctab_file = open(sys.argv[1])

for i, line in enumerate(ctab_file):
	if i == 0:
		continue
	fields = line.rstrip("\r\n").split("\t")
	chrom = fields[1]
	start = fields[3]
	end = fields[4]
	strand = fields[2]
	t_name = fields[5]
	if "+" in strand:
		if int(start) > 500:
			promoter_start = int(start) - 500
			promoter_end =  int(start) + 500

	elif "-" in strand:
		if int(end) > 500:
			promoter_start = int(end) - 500
			promoter_end = int(end) + 500
		
	bed_order = [chrom, str(promoter_start), str(promoter_end), t_name]
	print("\t".join(bed_order))