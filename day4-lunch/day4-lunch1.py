#!/usr/bin/env python3

"""
Usage: ./day4-lunch1.py <ctab file> <ctabfile>
"""

import sys
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

fpkm_1 = pd.read_csv(sys.argv[1], sep = "\t", index_col = "t_name").loc[:, "FPKM"]
#in order to get the axes to scale without losing transcripts we had to adjust the original FPKM values by a variable number 
x_scale = fpkm_1 + 0.5
fpkm_name_1 = sys.argv[1].split(os.sep)[-2]
fpkm_2 = pd.read_csv(sys.argv[2], sep = "\t", index_col = "t_name").loc[:, "FPKM"]
y_scale = fpkm_2 + 0.5
fpkm_name_2 = sys.argv[2].split(os.sep)[-2]

#to find best fit line
fit = np.polyfit(fpkm_1, fpkm_2, 1)
fit_fn = np.poly1d(fit)
xfit = np.linspace(0, 10000, 50)

#Build plot and set how you want it to look
fig, ax = plt.subplots()
ax.scatter(x_scale, y_scale, alpha = 0.75)
plt.plot(xfit, fit_fn(xfit), '-', color='r')
ax.set_title("FPKM Comparison (modified by 0.5)")
ax.set_xlabel(fpkm_name_1)
ax.set_ylabel(fpkm_name_2)
plt.xscale("log")
plt.yscale("log")



fig.savefig("FPKM.png")
plt.close(fig)