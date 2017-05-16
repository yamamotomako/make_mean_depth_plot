#! /bin/bash

#$ -S /bin/bash
#$ -cwd


write_usage(){
	echo ""
	echo "bash ./runall.sh 'path of refGene.txt' 'path of sample name list' 'path of bam directory' 'path of bait file' 'path of result directory'"
	echo "(eg). bash ./runall.sh ./refGene.txt ./sample_list.txt ./data/JALSG_bam ./JALSG_sample.bed ./result"
	echo ""
}


refgenepath=$1
samplelist=$2
bamdir=$3
baitpath=$4
outdir=$5

#bamdir="/home/ymako/data/JALSG_bam"
#baitpath="./038107_D_BED_20120106.bed"
#outdir="./result"


if [ $# -ne 5 ]; then
	echo "argument is not enough."
	write_usage
	exit
fi

if [ ! -e ${refgenepath} ]; then
	echo "${refgenepath} is not existing."
	write_usage
	exit
fi

if [ ! -e ${samplelist} ]; then
	echo "${samplelist} is not existing."
	write_usage
	exit
fi

if [ ! -e ${bamdir} ]; then
	echo "${bamdir} is not existing."
	write_usage
	exit
fi

if [ ! -e ${baitpath} ]; then
	echo "${baitpath} is not existing."
	write_usage
	exit
fi



#rm -r -f ${outdir}/tmp_intersect
#rm -r -f ${outdir}/calc_depth_result

mkdir -p ${outdir}
mkdir -p ${outdir}/tmp_intersect
mkdir -p ${outdir}/calc_depth_result

#copy sample list for backup
cp ${samplelist} ${outdir}/sample_list.txt

#listing all bam files
ls ${bamdir} > ${outdir}/list.txt


#count all sample types
lsnum=`wc -l ${samplelist}`
lsnum=220


#making bait-reference-file
qsub -N job1 preparation.sh ${refgenepath} ${baitpath} ${outdir}


#making intersect file for each bam
qsub -N job2 -hold_jid job1 -t 1:${lsnum} calc_mean_depth.sh ${bamdir} ${baitpath} ${outdir}


#making whole intersect file as final result
qsub -N job3 -hold_jid job2 merge_result.sh ${outdir}


#making Rplot
qsub -N job4 -hold_jid job3 making_r_plot.sh ${outdir}


exit


