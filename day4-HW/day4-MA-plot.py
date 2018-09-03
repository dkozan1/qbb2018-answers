#!/usr/bin/env python3

"""
Usage: ./day4HW2.py <ctab_file>
MA plot of one ctab file
"""

import sys
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#transcript_id = sys.argv[1]

#function technically isn't necessary to create MA plot 
#don't need to cycle through two bc you're only interested in
#one file
def sex_abundance(gender):
	df1 = pd.read_csv(sys.argv[1])
	df2 = pd.read_csv(sys.argv[2])
	df = pd.concat([df1, df2])
	
	compiled = {}
	
	soi = df.loc[:, "sex"] == gender
	df = df.loc[soi,:]
	
	for index, sample, sex, stage in df.itertuples():
		name = (stage)
		filename = os.path.join(sys.argv[3], sample, "t_data.ctab")
		ctab_df = pd.read_table(filename, index_col = "t_name")
		##transcriptID
		compiled[name] = ctab_df.loc[:, "FPKM"]
		
	dfcompiled = pd.DataFrame(compiled)
	return(dfcompiled)

females = sex_abundance("female")
subset_females = females.iloc[:,2]
subset_females = subset_females + 1
males = sex_abundance("male")
subset_males = males.iloc[:,2]
subset_males = subset_males + 1


#MA plot functions
x_axis = np.log2(np.sqrt(subset_females * subset_males))

y_axis = np.log2(subset_females/subset_males)

#setting up MA plot
fig, ax = plt.subplots()
ax.scatter(x_axis, y_axis, color = "red", alpha = 0.5)
ax.set_title("MA Plot")
plt.xlabel("A: avg  intesity of transcript abundance (FPKM)", fontsize = 8)
plt.ylabel("M: female to male ratio", fontsize = 8)
plt.tight_layout()
fig.savefig("MA-plot.png")
plt.close(fig)