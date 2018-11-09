#!/usr/bin/env python3

import sys
from scipy.cluster.hierarchy import ward, dendrogram, linkage, leaves_list
import numpy as np
from matplotlib import pyplot as plt
from scipy.spatial.distance import pdist
import pandas as pd
import seaborn as sns
from sklearn.cluster import KMeans

data = []

for line in open(sys.argv[1]):
	fields = line.rstrip("\r\n").split()
	gene = fields[0]
	cfu =  fields[1]
	poly = fields[2]
	data.append([cfu, poly])
	
d = pd.read_csv('hema_data.txt', sep="\t", index_col='gene')
df = pd.DataFrame(data=d)

kmeans = KMeans(n_clusters = 7)
kmeans.fit(df)
y_kmeans = kmeans.predict(df)


fig = plt.figure()
plt.title("")
plt.scatter(df["CFU"], df["poly"], c=y_kmeans, s=5, cmap = "viridis")

plt.xlabel("CFU")
plt.ylabel("POLY")
plt.savefig("kmeans.png")
plt.close(fig)