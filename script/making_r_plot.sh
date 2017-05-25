#! /bin/bash

#$ -S /bin/bash
#$ -cwd

outdir=$1

start_sample=`head -n 1 ${outdir}/sample_list.txt`
end_sample=`tail -n 1 ${outdir}/sample_list.txt`

Rscript --vanilla make_plot.R ${outdir} ${start_sample} ${end_sample}


