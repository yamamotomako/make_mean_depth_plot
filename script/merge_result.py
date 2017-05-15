#! /usr/bin/env python


import sys
import os
import re
from collections import OrderedDict


outdir = sys.argv[1]
result_file = outdir + "/table.txt"

sample_list = []

ref_dict = OrderedDict()
ref_dict_header = []  #header
ref_dict_header.append("bait")


with open(outdir + "/sample_list.txt", "r") as f:
	for line in f:
		sample_list.append(line.strip())


with open(outdir + "/bait_annotated.bed", "r") as f:
	for line in f:
		arr = line.strip().split("\t")
		chrm = "chr"+arr[0]
		start = arr[1]
		end = arr[2]
		genome = arr[6]
		count = arr[7]

		#making empty hash 
		ref_dict[chrm+":"+start+"-"+end] = [genome, count, []]


for sample_name in sample_list:
	calc_file_dict = {}
	#try:
	with open(outdir + "/calc_depth_result/"+sample_name+".tmp", "r") as f:
		ref_dict_header.append(sample_name)
		for line in f:
			arr = line.strip().split("\t")
			calc_file_dict[arr[0]] = arr[1]

	for key in ref_dict:
		if key in calc_file_dict:
			ref_dict[key][2].append(calc_file_dict[key])
		else:
			ref_dict[key][2].append("0")
	#except:
	#	print sample_name+".tmp doesn't exist."



result_str = "\t".join(ref_dict_header) + "\n"

for k,v in ref_dict.items():
	str = "\t".join(v[2])
	result_str += k + " " + v[0] + " " + v[1] + "\t"+ str + "\n"

with open(result_file, "w") as g:
	g.write(result_str)


sys.exit()


