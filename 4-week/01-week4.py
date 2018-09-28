#!/usr/bin/env python3
"""
Usage: 01-week4.py plot pcd file
./01-week4.py <plink.eigenvec>
"""

import sys
import matplotlib.pyplot as plt
from statsmodels.stats import weightstats as stests
import numpy as np
import math


component_1 = []
component_2 = []

for line in open(sys.argv[1]):
	fields = line.rstrip("\r\n").split(" ")
	component_1_x = fields[2]
	component_2_y = fields[3]
	component_1.append(float(component_1_x))
	component_2.append(float(component_2_y))

fig, ax = plt.subplots()
plt.scatter(component_1, component_2)
plt.ylabel("relatedness")        
plt.xlabel("individual")   
ax.set_title("principal component analysis")  
plt.tight_layout()    
#plt.xlim(0, 100000)
#plt.ylim(0, 120000)
fig.savefig("PCA.png")
plt.close(fig)