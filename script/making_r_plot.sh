#! /bin/bash

#$ -S /bin/bash
#$ -cwd

outdir=$1

Rscript --vanilla make_plot.R ${outdir}


