#!/usr/bin/env python3

"""
Usage: ./day4-hw-gene.py <gene_name> <samples.csv> <ctab_file>
Finding variable gene name and pulling out mean fpkm values

"""

import sys
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

gene_name = sys.argv[1]

df = pd.read_csv(sys.argv[2])
compiled = {}
fpkms = []

for index, sample, sex, stage in df.itertuples():
	#name = (stage)
	filename = os.path.join(sys.argv[3], sample, "t_data.ctab")
	ctab_df = pd.read_table(filename, index_col = "t_name")

	roi = ctab_df.loc[:, "gene_name"] == gene_name
	compiled = ctab_df.loc[roi, "FPKM"]
	dfcompiled = pd.DataFrame(compiled)
##transcrip vs FPKMS avg of FPKMS
average = dfcompiled.mean(axis = 1)

#print(average)

fig, ax = plt.subplots()
ax.plot(list(dfcompiled.index), list(average), alpha = 0.75, color = "red")
#ax.plot(list(males), males.loc[transcript_id,:], color = "blue")
ax.set_title(gene_name)
#plt.xlabel("developmental stage", fontsize = 8)
#plt.ylabel("mRNA Abundance (FPKM)", fontsize = 8)
#plt.legend(bbox_to_anchor = (1.05, 0.5), loc = 2, borderaxespad = 0., labels = ["Female", "Male"])
plt.xticks(rotation=90)
plt.tight_layout()
fig.savefig("gene.png")
plt.close(fig)