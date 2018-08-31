#!/usr/bin/env python3

"""
Usage: ./day4HW1.py <t_name> <samples.csv> <ctab_file> <replicatesfile>
Plot of comparision between for females and males in the Sxl gene
"""

import sys
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

transcript_id = sys.argv[1]

def sex_abundance(gender):
	df1 = pd.read_csv(sys.argv[2])
	df2 = pd.read_csv(sys.argv[4])
	df = pd.concat([df1, df2])
	#replicates = pd.read_csv(sys.argv[4])
	compiled = {}
	soi = df.loc[:, "sex"] == gender
	df = df.loc[soi,:]
	
	for index, sample, sex, stage in df.itertuples():
		name = (stage)
		filename = os.path.join(sys.argv[3], sample, "t_data.ctab")
		ctab_df = pd.read_table(filename, index_col = "t_name")
		##transcriptID
		roi = ctab_df.index == sys.argv[1]
		compiled[name] = ctab_df.loc[roi, "FPKM"]
		
	dfcompiled = pd.DataFrame(compiled)
	return(dfcompiled)

females = sex_abundance("female")
males = sex_abundance("male")

fig, ax = plt.subplots()
ax.plot(list(females), females.loc[transcript_id,:], color = "red")
ax.plot(list(males), males.loc[transcript_id,:], color = "blue")
ax.set_title("Sxl")
plt.xlabel("developmental stage", fontsize = 8)
plt.ylabel("mRNA Abundance (FPKM)", fontsize = 8)

plt.legend(bbox_to_anchor = (1.05, 0.5), loc = 2, borderaxespad = 0., labels = ["Female", "Male"])
plt.xticks(rotation=90)
plt.tight_layout()
fig.savefig("Sxl.png")
plt.close(fig)