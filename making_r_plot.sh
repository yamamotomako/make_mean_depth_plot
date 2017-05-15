#! /bin/bash

#$ -S /bin/bash
#$ -cwd
#$ -o /home/ymako/log -e /home/ymako/log

outdir=$1

Rscript --vanilla make_plot.R ${outdir}


