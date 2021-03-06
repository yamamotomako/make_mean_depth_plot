#! /bin/bash

#$ -S /bin/bash
#$ -cwd

baitpath=$1
outdir=$2

wget -q "http://hgdownload.cse.ucsc.edu/goldenPath/hg19/database/refGene.txt.gz"
gunzip -f -c ./refGene.txt.gz > ${outdir}/refGene.txt
rm ./refGene.txt.gz

#extract necessary info from refGene.txt
python ./choose_exon.py ${outdir} || { echo "choose_exon.py was failed."; exit 1; }


#annotate exome info into bait file using previous result-file
python ./annotation_for_bait.py ${baitpath} ${outdir} || { echo "annotation.py was failed."; exit 1; }


