#!/usr/bin/env python3

"""
Usage: ./06-transform.py <<tab> <tab> <tab> <tab> <tab>> <original ctab file>
Transform your response variable (gene expression) into units of log(FPKM + 1).
Refit the linear model and report the output (R2, p-value, coefficients, etc.)
Plot the residuals to evaluate the normality assumption.
"""

import sys
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm


#X = []# Avg histone marks. from the tab files
#Y = []# FPKMs from original ctab file

histone_marks = {}
	
name_hist1 = sys.argv[1].split(os.sep)[-1]
mean_hist1 = pd.read_csv(sys.argv[1], sep = "\t", index_col = 0).iloc[:,4]

name_hist2 = sys.argv[2].split(os.sep)[-1]
mean_hist2 = pd.read_csv(sys.argv[2], sep = "\t", index_col = 0).iloc[:,4]

name_hist3 = sys.argv[3].split(os.sep)[-1]
mean_hist3 = pd.read_csv(sys.argv[3], sep = "\t", index_col = 0).iloc[:,4]

name_hist4 = sys.argv[4].split(os.sep)[-1]
mean_hist4 = pd.read_csv(sys.argv[4], sep = "\t", index_col = 0).iloc[:,4]

name_hist5 = sys.argv[5].split(os.sep)[-1]
mean_hist5 = pd.read_csv(sys.argv[5], sep = "\t", index_col = 0).iloc[:,4]

fpkm = sys.argv[6].split(os.sep)[-1]
fpkm_transcript = pd.read_csv(sys.argv[6], sep = "\t", index_col = "t_name").loc[:, "FPKM"]

histone_marks = {name_hist1 : mean_hist1, name_hist2 : mean_hist2, name_hist3 
						: mean_hist3, name_hist4 : mean_hist4, name_hist5 : mean_hist5, fpkm : fpkm_transcript}
						
histone_marks_df = pd.DataFrame(histone_marks)
histone_marks_df = histone_marks_df.dropna()

#print(histone_marks_df)
y = histone_marks_df.loc[:, fpkm]
x = histone_marks_df.loc[:, [name_hist1, name_hist2, name_hist3, name_hist4, name_hist5,]]
model = sm.OLS(y, x)
x = sm.add_constant(x)

#logtransform = np.log(fpkm)

results = model.fit()
#histone_marks_df['yhat'] = results.fittedvalues
#histone_marks_df['resid'] = results.resid(histone_marks_df)
#print(results.summary())
#fit_results = results.fittedvalues
residual_results = results.resid

x_axis = residual_results
y_axis = y

fig, ax = plt.subplots()
plt.hist(residual_results, bins = 5000)
plt.yscale('log')
ax.set_ylabel("Num")        
ax.set_xlabel("Residuals")   
ax.set_title("Residuals of Linear Regression Model Predicting Gene Expression")  
ax.set_xlim(left = -100, right = 500)
plt.tight_layout()    
fig.savefig("hist_resid_log.png")
plt.close(fig)  