#! /usr/bin/env python

import sys
import os
import pybedtools
from collections import OrderedDict


bait_file = sys.argv[1]
outdir = sys.argv[2]
refgene_file = outdir + "/refGene.nonmerge.bed"


a = pybedtools.BedTool(bait_file)
b = pybedtools.BedTool(refgene_file)
result = a.intersect(b, bed=True, wao=True).saveas(outdir + "/bait_refgene_ints.bed")

ref_dict = OrderedDict()

print "start converting intersect file"
with open(outdir + "/bait_refgene_ints.bed", "r") as f:
	for line in f:
		arr = line.strip().split("\t")
		chrm = arr[0]
		start = arr[1]
		end = arr[2]
		count = arr[9]
		plusminus = arr[10]
		name = arr[11]
		detail_name = arr[12]
		pos = chrm + ":" + start + "-" + end

		if not pos in ref_dict:
			ref_dict[pos] = [name, [detail_name], [start], [plusminus], [count]]
		else:
			ref_dict[pos][1].append(detail_name)
			ref_dict[pos][2].append(start)
			ref_dict[pos][3].append(plusminus)
			ref_dict[pos][4].append(count)



print "start writing result file"
result_str = ""

with open(bait_file, "r") as f:
	for line in f:
		arr = line.strip().split("\t")
		pos = arr[0] + ":" + arr[1] + "-" + arr[2]

		if pos in ref_dict:
			v = ref_dict[pos]
			arr = line.strip().split("\t")
			chrm = arr[0].replace("chr","")
			others = arr[1:]

			digit = v[3]
			min_start_index = v[2].index(min(v[2]))
			max_start_index = v[2].index(max(v[2]))

			if digit == "+":
				rep_detail_name = v[1][min_start_index]
				rep_count = v[4][min_start_index]
			else:
				rep_detail_name = v[1][max_start_index]
				rep_count = v[4][max_start_index]
			
			result_str += chrm + "\t" + "\t".join(others) + "\t" + rep_detail_name + "\t" + rep_count + "\t" + ",".join(v[1]) + "\n"


with open(outdir + "/bait_annotated.bed", "w") as g:
	g.write(result_str)




