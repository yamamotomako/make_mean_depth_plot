#! /usr/bin/env python
# -*- coding: utf-8 -*-


import sys

refgenefile = sys.argv[1]
outdir = sys.argv[2]

resultfile = outdir + "/refGene.nonmerge.bed"
result = ""

with open(refgenefile, "r") as f:
    for line in f:
        arr = line.strip().split("\t")
        exome_id= arr[1]
        chrm = arr[2]
        strand = arr[3]
        exome_number = arr[8]
        start_list = arr[9].split(",")
        end_list = arr[10].split(",")
        exome_name = arr[12]
        tmp_str = ""

        for i in range(int(exome_number)):
            tmp_str += chrm + "\t" + start_list[i] + "\t" + end_list[i] + "\t" + str(i+1) + "\t" + strand + "\t" + exome_id + "\t" + exome_name + "\n"

        result += tmp_str



with open(resultfile, "w") as f:
    f.write(result.rstrip("\n"))


