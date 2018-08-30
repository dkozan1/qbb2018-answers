#!/usr/bin/env python3

"""
Usage: ./day4-lunch.py <threshold> <ctab_file1> <ctab_file2> ... <ctab_filen> 
"""

import sys
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

threshold = int(sys.argv[1])
ctab_variable = len(sys.argv)
d_fpkm = {}

for i in range(2,(ctab_variable)):
	
	name1 = sys.argv[i].split(os.sep)[-2]
	fpkm = pd.read_csv(sys.argv[i], sep = "\t", index_col = "t_name").loc[:, "FPKM"]
	d_fpkm[name1] = fpkm

fpkms_df = pd.DataFrame(d_fpkm)
fpkms_df.to_csv(sys.stdout) 

sum_fpkms = fpkms_df.sum(axis = 1)
with_threshold = sum_fpkms > threshold
results = sum_fpkms.index[with_threshold == True]

print(sum_fpkms)
print(with_threshold)
print(results)
