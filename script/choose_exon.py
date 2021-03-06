#! /usr/bin/env python
# -*- coding: utf-8 -*-


import sys

outdir = sys.argv[1]

refgenefile = outdir + "/refGene.txt"
resultfile = outdir + "/refGene.nonmerge.bed"


g = open(resultfile, "w")

with open(refgenefile, "r") as f:
    for line in f:
        arr = line.strip().split("\t")
        refgene_id= arr[1]
        chrm = arr[2]
        strand = arr[3]
        exon_count = arr[8]
        start_list = arr[9].split(",")
        end_list = arr[10].split(",")
        gene_symbol = arr[12]
        tmp_str = ""
        

        for i in range(int(exon_count)):
            if strand == "+":
                count = i + 1
            else:
                count = int(exon_count) - i

            tmp_str = chrm + "\t" + start_list[i] + "\t" + end_list[i] + "\t" + str(count) + "\t" + strand + "\t" + refgene_id + "\t" + gene_symbol + "\n"

            g.write(tmp_str)

g.close()




