#! /bin/bash

#$ -S /bin/bash
#$ -cwd

outdir=$1
num=$SGE_TASK_ID


samplename=`sed -n ${num}P ${outdir}/sample_list.txt`
bamfile=`sed -n ${num}P ${outdir}/bam_list.txt`


baitfile=${outdir}"/bait_annotated.bed"
outfile=${outdir}"/calc_depth_result/"${samplename}


depth_tool ${bamfile} ${baitfile} ${outfile}

