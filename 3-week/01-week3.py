#!/usr/bin/env python3
"""
Usage: 01-week3.py multi panel plot for identifying varians 
./01-week3.py <ann_calls.vcf> <snpEff_genes.txt>
"""

import sys
import matplotlib.pyplot as plt
from statsmodels.stats import weightstats as stests
import numpy as np
import math

annotated = open(sys.argv[1])
read_depth = []

for i in annotated:
	if i.startswith("#"):
		pass
	else:
		fields = i.rstrip("\r\n").split("\t")
		info = fields[7]
		depth = info.split(";")[7].lstrip("DP=")
		if "," in depth:
			depth2 = depth.split(",")
			read_depth.append(float(depth2[0]))
			read_depth.append(float(depth2[1]))
		else:
			read_depth.append(float(depth))

annotated = open(sys.argv[1])
all_quality = []

for i in annotated:
	if i.startswith("#"):
		pass
	else:
		fields = i.rstrip("\r\n").split("\t")
		quals = "".join(fields[5])
		all_quality.append(float(quals))

annotated = open(sys.argv[1])
all_freq = []
blank_freq = []

for i in annotated:
	if i.startswith("#"):
		pass
	else:
		fields = i.rstrip("\r\n").split("\t")
		info = fields[7]
		allele = info.split(";")[4][3:]
		if "AN" in allele:
			if allele not in blank_freq:
				blank_freq[float(allele)] = 1
				all_freq.append(float(allele))
			else:
				blank_freq[float(allele)] += 1
				all_freq.append(float(allele))
				
				if "," in allele:
					allele_spl = allele.split(",")
					all_freq.append(float(allele_spl[0]))
					all_freq.append(float(allele_spl[1]))
				else:
					all_freq.append(float(allele))

conservative_inframe_deletion = []
conservative_inframe_insertion = []
disruptive_inframe_deletion = []
disruptive_inframe_insertion = []
downstream_gene_variant = []
frameshift = []
initiator_codon_variant = []
intron = []
missense = []
noncoding_transcript_exon = []
splice_deceptor = []
splice_donor = []
splice_region = []
start_lost = []
stop_gained = []
stop_lost = []
stop_retained = []
synonymous = []
upstream_gene_variant = []

conservative_inframe_deletion = 0
conservative_inframe_insertion = 0
disruptive_inframe_deletion = 0
disruptive_inframe_insertion = 0
downstream_gene_variant = 0
frameshift = 0
initiator_codon_variant = 0
intron = 0
missense = 0
noncoding_transcript_exon = 0
splice_deceptor = 0
splice_donor = 0
splice_region = 0
start_lost = 0
stop_gained = 0
stop_lost = 0
stop_retained = 0
synonymous = 0
upstream_gene_variant = 0

for line in open(sys.argv[2]):
	fields = line.rstrip('\r\n').split('\t')
	if line.startswith("#"):
		pass
	else:
		 conservative_inframe_deletion += int(fields[8])
		 conservative_inframe_insertion += int(fields[9])
		 disruptive_inframe_deletion += int(fields[10])
		 disruptive_inframe_insertion += int(fields[11])
		 downstream_gene_variant += int(fields[12])
		 frameshift += int(fields[13])
		 initiator_codon_variant += int(fields[14])
		 intron += int(fields[15])
		 missense += int(fields[16])
		 noncoding_transcript_exon += int(fields[17])
		 splice_deceptor += int(fields[18])
		 splice_donor += int(fields[19])
		 splice_region += int(fields[20])
		 start_lost += int(fields[21])
		 stop_gained += int(fields[22])
		 stop_lost += int(fields[23])
		 stop_retained += int(fields[24])
		 synonymous += int(fields[25])
		 upstream_gene_variant += int(fields[26])
labels=["conservative_inframe_deletion", "conservative_inframe_insertion", "disruptive_inframe_deletion", "disruptive_inframe_insertion", "dowstream_gene_variant", "frameshift", "initiator_codon_variant", "intron", "missense", "noncoding_transcript_exon", "splice_deceptor", "splice_donor", "splice_region", "start_lost", "stop_gained", "stop_lost", "stop_retained", "synonymous", "upstream_gene_variant"]

quant_mut_types=[conservative_inframe_deletion, conservative_inframe_insertion, disruptive_inframe_deletion, disruptive_inframe_insertion, downstream_gene_variant, frameshift, initiator_codon_variant, intron, missense, noncoding_transcript_exon, splice_deceptor, splice_donor, splice_region, start_lost, stop_gained, stop_lost, stop_retained, synonymous, upstream_gene_variant]

index=np.arange(len(labels))

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2, constrained_layout=True, figsize=(40,40))
ax1.hist(read_depth, bins=1000)
ax1.set(title="variant read depths", xlabel="depth", ylabel="count")
ax1.set_xlim(0,140)
ax2.hist(all_quality, bins=1000)
ax2.set(title = "genotype quality distribution", xlabel="quality", ylabel="count")
ax2.set_xlim(0,2500)
ax3.hist(all_freq)
ax3.set(title="variant allele frequency", xlabel="frequency", ylabel="variants")
ax3.set_xlim(0,20)
ax4.bar(index, quant_mut_types)
ax4.set(title = "snpEff effect", xlabel="effects", ylabel="mutation")
ax4.set_xticklabels(labels)
fig.savefig("multi-panel.png")
plt.close(fig)
