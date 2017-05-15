#! /bin/bash

#$ -S /bin/bash
#$ -cwd
#$ -o /home/ymako/log -e /home/ymako/log

refgenepath=$1
baitpath=$2
outdir=$3

#extract necessary info from refGene.txt
python ./choose_exon.py ${refgenepath} ${outdir}


#annotate exome info into bait file using previous result-file
python ./annotation_for_bait.py ${baitpath} ${outdir}

