#!/usr/bin/env python3
"""
Usage: 01-week4.py plot pcd file
./02-week4.py <vsf file>
"""

import sys
import matplotlib.pyplot as plt
from statsmodels.stats import weightstats as stests
import numpy as np
import math

allele_frequency = []

for line in open(sys.argv[1]):
	if line.startswith("#"):
		continue
	else:
		fields = line.rstrip("\r\n").split("\t")
		frequency = fields[7]
		allele = frequency.split("=")[1]
		allele_want = allele.split(",")[0]
		allele_frequency.append(float(allele_want))

fig, ax = plt.subplots()
plt.hist(allele_frequency)
plt.ylabel("frequency")        
plt.xlabel("allele")   
ax.set_title("Allele Frequency spectrum")  
plt.tight_layout()
fig.savefig("allele_freq.png")
plt.close(fig)