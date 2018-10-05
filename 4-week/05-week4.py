#!/usr/bin/env python3
"""
Usage: ./05-week4.py <plink.X.qassoc> <phenotype>
"""
import sys
import csv
import numpy as np
import matplotlib.pyplot as plt
        
pval = []
pos = []
chrom = []
x = []
y = []

count = 0

name = sys.argv[1].split('.')[-2]

for line in open(sys.argv[1]):
	if ("NA" in line) or ("BETA" in line):
		continue
	fields = line.split()
	chrom = fields[0]
	pos = int(fields[2])
	p = float(fields[-1])
	logp = -np.log10(p)
	pval = -np.log(float(fields[8]))
	pos = float(fields[2])
	chrom = fields[0]
	count += 1
	x.append(chrom)
	y.append(pval)
		
print(len(x), len(y))
        
fig, ax = plt.subplots()
ax.scatter(x, y, color = "green", alpha = 0.5)
plt.axhline(y=-np.log(10e-5), lw = 0.5, color = "black")
ax.set_ylabel('Pval')
ax.set_xlabel('Genomic Position')
ax.set_title(sys.argv[2])
fig.savefig(name + '.png')
plt.close()