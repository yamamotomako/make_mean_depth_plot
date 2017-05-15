import sys

bedfile = sys.argv[1]
outdir = sys.argv[2]

resultfile = outdir + "/refGene.nonmerge.bed"
result = ""

with open(bedfile, "r") as f:
	for line in f:
		arr = line.strip().split("\t")
		#chr = arr[2].relace("chr","")
		name_detail = arr[1]
		chr = arr[2]
		plusminus = arr[3]
		count = arr[8]
		start_list = arr[9].split(",")
		end_list = arr[10].split(",")
		name = arr[12]
		tmp_str = ""

		for i in range(int(count)):
			tmp_str += chr + "\t" + start_list[i] + "\t" + end_list[i] + "\t" + str(i+1) + "\t" + plusminus + "\t" + name + "\t" + name_detail + "\n"

		result += tmp_str



with open(resultfile, "w") as f:
	f.write(result)


