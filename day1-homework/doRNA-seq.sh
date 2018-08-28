#!/bin/bash

GENOME=../genomes/BDGP6
ANNOTATION=../genomes/BDGP6.Ensembl.81.gtf

for SAMPLE in SRR072893 SRR072903 SRR072905 SRR072915
do
  mkdir $SAMPLE
  fastqc ~/data/rawdata/$SAMPLE.fastq
  hisat2 -x $GENOME -U ~/data/rawdata/$SAMPLE.fastq -S $SAMPLE.sam
  samtools view -b $SAMPLE.sam > $SAMPLE.bam
  samtools sort $SAMPLE.bam > $SAMPLE.bam
  stringtie $SAMPLE.bam -G $ANNOTATION -p 8 -e -B -o $SAMPLE.abund.gtf
done
