#!/usr/bin/env python3

import sys
import numpy as np
from statsmodels.stats import weightstats as stests
import matplotlib.pyplot as plt
import math
import pandas as pd

gained = []
lost = []

for line in open(sys.argv[1]):
    fields = line.rstrip("\t").split()
    if fields[5] == "1" and fields[6] == "0":
        gained += str(1)
    elif fields[5] == "0" and fields[6] == "1":
        lost += str(1)
    else:
        continue

objects = ("gained", "lost")
y_pos = np.arange(len(objects))
values = (len(gained), len(lost))

category = {}

for line in open(sys.argv[2]):
    fields = line.rstrip("\t").split()
    begin_type = int(fields[1])
    end_type = int(fields[2])
    type = fields[3]
    for bases in range(begin_type, end_type):
    	category[bases] = type

mutation_cat = []

for i, line in enumerate(open(sys.argv[3])):
	fields = line.rstrip("\t").split()
	mut_start = int(fields[1])
	mut_end = int(fields[2])
	for bases in range(mut_start, mut_end):
		if bases in category:
			mutation_cat.append(category[bases])
			
introns = []
exons = []
promoters = []

for cat in mutation_cat:
	if cat == "intron":
		introns += str(1)
	elif cat == "exon":
		exons += str(1)
	elif cat == "promoter":
		promoters += str(1)

objects2 = ("introns", "exons", "promoters")
y_pos2 = np.arange(len(objects2))
values2 = (len(introns), len(exons), len(promoters))

fig, (ax1, ax2)=plt.subplots(ncols=2)
ax1.bar(y_pos, values)
ax1.set_xticklabels(objects)
ax1.set_xticks(y_pos)
ax1.set_xlabel("gained v lost")
ax1.set_ylabel("count")
ax1.set_title("sites lost/gained")
ax2.bar(y_pos2, values2,)
ax2.set_xticklabels(objects2)
ax2.set_xticks(y_pos2)
ax2.set_xlabel("mutation")
ax2.set_ylabel("#")
ax2.set_title("mutation number")
fig.savefig("chipplot.png")
plt.close()