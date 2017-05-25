#! /bin/bash

#$ -S /bin/bash
#$ -cwd

outdir=$1


#reading tmp.bed and merge all intersect files into final result
python ./merge_result.py ${outdir}




