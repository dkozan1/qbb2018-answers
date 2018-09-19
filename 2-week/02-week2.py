#!/usr/bin/env python3
"""
Usage: 02-week2.py dot plot of contigs vs reference fa file
./02-week2.py <lastz.out> """

import fasta
import sys
import matplotlib.pyplot as plt
from statsmodels.stats import weightstats as stests
import numpy as np
import math

site = 0
fig, ax = plt.subplots()
for i in open(sys.argv[1]):
	field = i.split("\t")
	reference_start = field[0]
	reference_end = field[1]
	contig_name = field[2]
	contig_strand = field[3]
	contig_start = field[4]
	contig_end = field[5]
	contig_length = field[6]
	plt.plot([int(reference_start), int(reference_end)], [site, site + int(contig_length)])
	site += int(contig_length)

#plt.hist(x, y)
plt.ylabel("Contigs")        
plt.xlabel("Reference")   
ax.set_title("Contig position compared to reference sequence")  
plt.tight_layout()    
plt.xlim(0, 100000)
plt.ylim(0, 120000)
fig.savefig("dotplot1.png")
plt.close(fig)
