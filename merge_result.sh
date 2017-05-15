#! /bin/bash

#$ -S /bin/bash
#$ -cwd
#$ -o /home/ymako/log -e /home/ymako/log

outdir=$1


#reading tmp.bed and merge all intersect files into final result
python ./merge_result.py ${outdir}




