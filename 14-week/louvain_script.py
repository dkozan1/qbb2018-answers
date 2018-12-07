#!/usr/bin/env python3

import scanpy.api as sc

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
sc.pp.recipe_zheng17(adata, n_top_genes=1000, log=True, plot=False, copy=False)

sc.pp.neighbors(adata, n_neighbors=15)

sc.tl.louvain(adata, resolution=None)
sc.tl.tsne(adata, n_pcs=None, use_rep=None, perplexity=30, early_exaggeration=12, learning_rate=1000, random_state=0, use_fast_tsne=True, n_jobs=None, copy=False)
sc.pl.tsne(adata, color = "louvain", save = ("tsne"))

