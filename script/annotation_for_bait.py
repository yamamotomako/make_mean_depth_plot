#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import re
import pybedtools
from collections import OrderedDict


bait_file = sys.argv[1]
outdir = sys.argv[2]
refgene_file = outdir + "/refGene.nonmerge.bed"
ref_dict = OrderedDict()


#should aquire the end of col number of bait file, then use in defining the start col of intersect file.


#intersect exome with bait
a = pybedtools.BedTool(bait_file)
b = pybedtools.BedTool(refgene_file)
result = a.intersect(b, bed=True, wao=True).saveas(outdir + "/bait_refgene_ints.bed")


#add exome info into bait file.
with open(outdir + "/bait_refgene_ints.bed", "r") as f:
    for line in f:
        arr = line.strip().split("\t")
        chrm = arr[0]
        bait_start = arr[1]
        bait_end = arr[2]
        exome_start = arr[8]
        exome_num = arr[9]
        exome_strand = arr[10]
        exome_id = arr[11]
        exome_name = arr[12]
        key = chrm + ":" + bait_start + "-" + bait_end

        if not key in ref_dict:
            ref_dict[key] = [[exome_id], [exome_name], [exome_num], [exome_strand]]
        else:
            ref_dict[key][0].append(exome_id)
            ref_dict[key][1].append(exome_name)
            ref_dict[key][2].append(exome_num)
            ref_dict[key][3].append(exome_strand)



#find representavie exome by sort and renew ref_dict
new_ref_dict = OrderedDict()
for key, value in ref_dict.items():
    exome_id = value[0]
    exome_name = value[1]
    exome_num = value[2]
    exome_strand = value[3]
    exome_id_num = []

    for e_id in exome_id:
        num = re.findall(r"\d.+", e_id)
        if len(num) == 0:
            num = None
        else:
            num = int(num[0])
        exome_id_num.append(num)

    if exome_strand[0] == "+":
        exome_id_num.sort()
    else:
        exome_id_num.sort(reverse=True)

    index = 0
    new_ref_dict[key] = [exome_id[index], exome_name[index], exome_num[index], exome_strand[index], exome_id]



result_str = ""
with open(bait_file, "r") as f:
    for line in f:
        arr = line.strip().split("\t")
        chrm = arr[0]
        start = arr[1]
        end = arr[2]
        bait_other_info = "\t".join(arr[3:])
        key = chrm + ":" + start + "-" + end


        value = new_ref_dict[key]
        exome_id = value[0]
        exome_name = value[1]
        exome_num = value[2]
        exome_strand = value[3]
        exome_ids = ",".join(value[4])

        exome_info = exome_id + "\t" + exome_name + "\t" + exome_num + "\t" + exome_strand + "\t" + exome_ids

        result_str += chrm.replace("chr","") + "\t" + start + "\t" + end + "\t" + bait_other_info + "\t" + exome_info + "\n"
        


with open(outdir + "/bait_annotated.bed", "w") as g:
    g.write(result_str.rstrip("\n"))




