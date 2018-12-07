#!/usr/bin/env python3

import sys
import numpy as np
import csv
import matplotlib.pyplot as plt
import scanpy.api as sc
sc.settings.autoshow = False
import matplotlib
matplotlib.use("Agg")

# Read 10x dataset
adata = sc.read_10x_h5("neuron_10k_v3_filtered_feature_bc_matrix.h5")
# Make variable names (in this case the genes)
adata.var_names_make_unique()
# Filter like Zheng paper
#sc.pp.recipe_zheng17(adata, n_top_genes=1000, log=True, plot=False, copy=False)
# Make PCA
sc.tl.pca(adata, n_comps=50, zero_center=True, svd_solver='auto', random_state=0, return_info=False, use_highly_variable=None, dtype='float32', copy=False, chunked=False, chunk_size=None)
sc.pl.pca(adata, save=True)
