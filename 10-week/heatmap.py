#!/usr/bin/env python3

import sys
from scipy.cluster.hierarchy import ward, dendrogram, linkage, leaves_list
import numpy as np
from matplotlib import pyplot as plt
from scipy.spatial.distance import pdist
import pandas as pd
import seaborn as sns

data = []

for line in open(sys.argv[1]):
	fields = line.rstrip("\r\n").split()
	gene = fields[0]
	cfu =  fields[1]
	poly = fields[2]
	unk = fields[3]
	int_cell = fields[4]
	mys = fields[5]
	mid = fields[6]
	data.append([cfu, poly])
#print(data)


d = pd.read_csv('hema_data.txt', sep="\t", index_col='gene')
df = pd.DataFrame(data=d)
# df_array = np.array(df)
# data.columns = ["CFU", "poly", "unk", "int", "mys", ""]
# print(df["CFU"])
# print(df.iloc[[0]])
cmap = sns.diverging_palette(220, 20, sep=20, as_cmap=True)

plt = sns.clustermap(df, cmap=cmap)
#plt.show()
#plt.tight_layout()
plt.savefig("heatmap.png")
plt.close(fig)
