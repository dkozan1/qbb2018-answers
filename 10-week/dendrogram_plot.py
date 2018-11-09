#!/usr/bin/env python3

import sys
from scipy.cluster.hierarchy import ward, dendrogram, linkage, leaves_list
import numpy as np
from matplotlib import pyplot as plt
from scipy.spatial.distance import pdist

data = []

for line in open(sys.argv[1]):
	fields = line.rstrip("\r\n").split()
	gene = fields[0]
	cfu =  fields[1]
	poly = fields[2]
	data.append([cfu, poly])
#print(data)

z = ward(pdist(data))
y = leaves_list(z)
fig = plt.figure(figsize=(20, 10))
dn = dendrogram(z)
plt.tight_layout()
plt.ylabel("")        
plt.xlabel("")   
#plt.set_title("")
fig.savefig("dendro.png")
plt.close(fig)