#! /usr/bin/env python

import sys
import os
import re
import pybedtools
from collections import OrderedDict



def calc_mean_depth(bamfile, bedfile, outdir, outfile, sge_task_id):

	print "Starting bedtools intersect..."

	bam_p = pybedtools.BedTool(bamfile)
	bed_p = pybedtools.BedTool(outdir + "/bait_annotated.bed")
	bam2ref = bam_p.intersect(bed_p, bed=True, wo=True).saveas(outdir + "/tmp_intersect/ints."+sge_task_id)

	print "Finished bedtools intersect..."


	ref_dict = OrderedDict()

	with open(outdir + "/tmp_intersect/ints."+sge_task_id, "r") as f:
		for ff in f:
			line = ff.split("\t")
			chrm = line[0]
			match_start = line[1]
			match_end = line[2]
			ref_start = line[13]
			ref_end = line[14]
			match_base = int(line[len(line)-1])
			other_info = "\t".join(line[15:])
			key = ref_start + "-" + ref_end

			if not ref_dict.has_key(key):
				depth = match_base
				ref_dict[key] = [chrm, match_start, match_end, ref_start, ref_end, depth, other_info]
			else:
				depth = ref_dict[key][5] + match_base
				ref_dict[key][5] = depth



	print "Making output file..."

	#header
	result_str = "\t".join(["chromesome:start-end","mean-depth"]) + "\n"

	for k, v in ref_dict.items():
		mean_depth = int(v[5]) / (int(v[4]) - int(v[3]))
		result_str += "chr"+v[0]+":"+v[3]+"-"+v[4] + "\t" + str(mean_depth) + "\n"


	with open(outfile, "w") as g:
		g.write(result_str.strip())



	#os.remove("./tmp.bed")
	#os.remove("./tmp_intersect/ints."+sge_task_id)

	print "Finished all process!"


bamfile = sys.argv[1]
bedfile = sys.argv[2]
outdir = sys.argv[3]
outfile = sys.argv[4]
sge_task_id = sys.argv[5]


calc_mean_depth(bamfile, bedfile, outdir, outfile, sge_task_id)


sys.exit()




