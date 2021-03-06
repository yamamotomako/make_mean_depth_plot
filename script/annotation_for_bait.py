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


#intersect exon with bait
a = pybedtools.BedTool(bait_file)
b = pybedtools.BedTool(refgene_file)
result = a.intersect(b, bed=True, wao=True).saveas(outdir + "/bait_refgene_ints.bed")


#add exon info into bait file.
with open(outdir + "/bait_refgene_ints.bed", "r") as f:
    for line in f:
        arr = line.strip().split("\t")
        chrm = arr[0]
        bait_start = arr[1]
        bait_end = arr[2]
        exon_start = arr[8]
        exon_num = arr[9]
        strand = arr[10]
        refgene_id = arr[11]
        gene_symbol = arr[12]
        key = chrm + ":" + bait_start + "-" + bait_end

        if not key in ref_dict:
            ref_dict[key] = [[refgene_id], [gene_symbol], [exon_num], [strand]]
        else:
            ref_dict[key][0].append(refgene_id)
            ref_dict[key][1].append(gene_symbol)
            ref_dict[key][2].append(exon_num)
            ref_dict[key][3].append(strand)



#find representavie exon by sort and renew ref_dict
new_ref_dict = OrderedDict()
for key, value in ref_dict.items():
    refgene_id = value[0]
    gene_symbol = value[1]
    exon_num = value[2]
    strand = value[3]
    refgene_id_num = []

    for r_id in refgene_id:
        num = re.findall(r"\d.+", r_id)
        if len(num) == 0:
            num = None
        else:
            num = int(num[0])
        refgene_id_num.append([num, r_id])
        refgene_id_num.sort(key=lambda x:x[0])

    index = 0
    new_ref_dict[key] = [refgene_id_num[index][1], gene_symbol[index], exon_num[index], strand[index], refgene_id]



g = open(outdir + "/bait_annotated.bed", "w")

with open(bait_file, "r") as f:
    for line in f:
        arr = line.strip().split("\t")
        chrm = arr[0]
        start = arr[1]
        end = arr[2]
        bait_other_info = "\t".join(arr[3:])
        key = chrm + ":" + start + "-" + end


        value = new_ref_dict[key]
        refgene_id = value[0]
        gene_symbol = value[1]
        exon_num = value[2]
        strand = value[3]
        refgene_ids = ",".join(value[4])

        exon_info = refgene_id + "\t" + gene_symbol + "\t" + exon_num + "\t" + strand + "\t" + refgene_ids

        result_str = chrm.replace("chr","") + "\t" + start + "\t" + end + "\t" + bait_other_info + "\t" + exon_info + "\n"
        
        g.write(result_str)

g.close()

