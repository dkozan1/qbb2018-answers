#!/usr/bin/env python3
"""
Usage: 01-week1.py 2 fasta files: <dna_file blast> <aa maffta align file>
Plot synonymous and non synonymous mutations to account for
selection. Compare the nucleotides at the specific positions
in the different sequences. """

import fasta
import sys
import matplotlib.pyplot as plt
from statsmodels.stats import weightstats as stests

dna_reader = fasta.FASTAReader(open(sys.argv[1]))
aa_reader = fasta.FASTAReader(open(sys.argv[2]))
#i will be for each alignment
#j will be for each position in the alignment
n_seq = []
master_aa_seq =[]

for (dna_id, dna), (aa_id, aa) in zip(dna_reader, aa_reader):
	new_dna = []
	new_aa = []
	j = 0
	for i in range(len(aa)):
		a = aa[i]
		n = dna[j: j + 3]
		
		if a == '-':
			n = "---"
			new_dna.append(n)
			new_aa.append(a)
		else:
			j+=3
			new_dna.append(n)
			new_aa.append(a)
	
	n_seq.append(new_dna)
	master_aa_seq.append(new_aa)

Qamino_list = master_aa_seq[0]
Qdna_list = n_seq[0]

dN = [0] * len(Qamino_list)
dS = [0] * len(Qdna_list)


for i in range(1, len(master_aa_seq[1:])):
	list_align = master_aa_seq[i]
	
	for j in range(len(list_align)):
		if list_align[j] != Qamino_list[j]:
			dN[j] += 1
		else:
			dS[j] += 1
			
# print(dN)
# print(dS)
ratio_list = []
for i in range(len(dS)):
	dSN = dN[i] / (dS[i] + 1)
	ratio_list.append(dSN)

#print(ratio_list)
# x = range(0, len(ratio)
# y = ratio_list

ztest = stests.ztest(dN, dS)
print(ztest)

fig, ax = plt.subplots()
plt.scatter(range(0, len(ratio_list)), ratio_list, alpha = 0.5, s = 3, color ='green')
#plt.yscale('log')
ax.set_ylabel("ratio dN/dS")
ax.set_xlabel("amino acid postion")
ax.set_title("Ratio of synonymous nonsynonymous nt changes based on amino acid position")
#ax.set_xlim(left = -100, right = 500)
plt.tight_layout()
fig.savefig("selection.png")
plt.close(fig)