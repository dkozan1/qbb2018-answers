#!/usr/bin/env python3

"""
Usage: ./day4HW.py <samples.csv> <ctab_file> <sex>
compilation of FPKMS from each gene in each sex
"""

import sys
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#dataframe reads out all samples
df = pd.read_csv(sys.argv[1])

compiled = {}

for index, sample, sex, stage in df.itertuples():
	filename = os.path.join(sys.argv[2], sample, "t_data.ctab")
	ctab_df = pd.read_table(filename, index_col = "t_name")
	#join stringtie files and format the headers
	#keys of dictionary sex and stage, values FPKM
	#concatenated to one key based on column names
	compiled[sex + "_" + stage] = ctab_df.loc[:, "FPKM"]

#put dictionary into data frame
dfcompiled = pd.DataFrame(compiled)


print(dfcompiled)