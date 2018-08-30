#!/usr/bin/env python3

import sys
import fasta

#reader = fasta.FASTAReader(sys.stdin)
target = fasta.FASTAReader(sys.stdin)
query = fasta.FASTAReader(open(sys.argv[1]))
k = int(sys.argv[2])

kmers = {}
kmer = 0
kmers[kmer] = []
#target_kmers = {}
#sequence_kmers = {}

for ident, sequence in query:
	for i, v in enumerate(range(0, len(sequence) - k)):
		kmer = sequence[i:i+k]
		if kmer not in kmers:
			kmers[kmer] = [i]
		else:
			kmers[kmer].append(i)
			
for ident, sequence in target:
	for i, v in enumerate(range(0, len(sequence) - k)):
			kmer_targ = sequence[i:i+k]
			if kmer_targ in kmers:
				print(ident, i, kmers[kmer_targ], kmer_targ)