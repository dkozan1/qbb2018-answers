#!/usr/bin/env python3
"""
Usage: 01-week2.py <velvet fasta file> | 01-week2.py <Spades fasta>
***run spades file one time and velvet file second time
Making a consensus sequence out of contigs based
on Illumina sequence reads
To match kmers from BOTH SPAdes and velvet """

import fasta
import sys
import matplotlib.pyplot as plt
from statsmodels.stats import weightstats as stests
import numpy as np

reader = fasta.FASTAReader(open(sys.argv[1]))

idents = []
min_contig = []
max_contig = []
avg_contig = []
length = []

for ident, sequence in reader:
	idents.append(ident)
	
#print(idents)

for i in range(len(idents)):
	idents[i].split("_")
	total_contig = idents[-1].split("_")[1]
	min_contig.append(int(idents[i].split("_")[3]))
	max_contig.append(int(idents[i].split("_")[3]))
	avg_contig.append(int(idents[i].split("_")[3]))
	length.append(int(idents[i].split("_")[3]))

print("Total number contigs " + str(total_contig))
print("Min length contigs " + str(np.min(min_contig)))
print("Max length contigs " + str(np.max(max_contig)))
print("Average length contigs " + str(np.mean(avg_contig)))

halfway_mark = np.sum(length)/2
#print(halfway_mark)

sort_contigs = sorted(length)
n = 0

for x in range(len(sorted(length))):
	if n < halfway_mark:
		n = n + length[x]
	else:
		print("Length of N50 is " + str(length[x + 1]))
		break