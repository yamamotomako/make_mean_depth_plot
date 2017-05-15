#! /bin/bash

#$ -S /bin/bash
#$ -cwd
#$ -o /home/ymako/log -e /home/ymako/log

bamfullpath=$1
baitfile=$2
outdir=$3
num=$SGE_TASK_ID


samplename=`sed -n ${num}P ${outdir}/sample_list.txt`
#bamfile=${bamfullpath}"/"${bamkind}"/"`sed -n ${num}P ${outdir}/list.txt`
bamfile=${bamfullpath}"/"`ls ${bamfullpath} | head -n ${num} | tail -n 1`


outfile=${outdir}"/calc_depth_result/"${samplename}.tmp


python ./calc_mean_depth.py ${bamfile} ${baitfile} ${outdir} ${outfile} ${num}

