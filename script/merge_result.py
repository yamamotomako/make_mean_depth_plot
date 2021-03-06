#! /usr/bin/env python
# -*- coding: utf-8 -*-


import sys
import os
import re
from collections import OrderedDict


outdir = sys.argv[1]
result_file = outdir + "/table.txt"

sample_list = []

ref_dict = OrderedDict()
ref_dict_header = ["bait"]  #header


with open(outdir + "/sample_list.txt", "r") as f:
    for line in f:
        sample_list.append(line.strip())


with open(outdir + "/bait_annotated.bed", "r") as f:
    for line in f:
        arr = line.rstrip().split("\t")
        chrm = "chr"+arr[0]
        start = arr[1]
        end = arr[2]
        refgene_id = arr[6]
        gene_symbol = arr[7]
        exon_num = arr[8]
        #making empty hash 
        ref_dict[chrm+":"+start+"-"+end] = [refgene_id, gene_symbol, exon_num, []]


for sample_name in sample_list:
    calc_file_dict = {}
    try:
        with open(outdir + "/calc_depth_result/" + sample_name, "r") as f:
            ref_dict_header.append(sample_name)
            for line in f:
                arr = line.rstrip().split("\t")
                calc_file_dict[arr[0]] = arr[1]

    except:
        print sample_name + " doesn't exist."
        continue

    for key in ref_dict:
        if key in calc_file_dict:
            ref_dict[key][3].append(calc_file_dict[key])
        else:
            ref_dict[key][3].append("0")


g = open(result_file, "w")
g.write("\t".join(ref_dict_header) + "\n")


for key, value in ref_dict.items():
    str = "\t".join(value[3])
    g.write(key + " " + value[0] + " " + value[1] + " " + value[2] + "\t"+ str + "\n")

g.close()


