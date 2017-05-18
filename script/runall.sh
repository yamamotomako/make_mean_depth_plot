#! /bin/bash

#$ -S /bin/bash
#$ -cwd


write_usage(){
    echo ""
    echo "bash ./runall.sh 'path of refGene.txt' 'path of config.csv' 'path of bait file' 'path of result directory'"
    echo "(eg). bash ./runall.sh ./refGene.txt ./sample_config.csv ./JALSG_sample.bed ./result"
    echo ""
}


refgenepath=$1
configfile=$2
baitpath=$3
outdir=$4


if [ $# -ne 4 ]; then
    echo "argument is not enough."
    write_usage
    exit
fi

if [ ! -e ${refgenepath} ]; then
    echo "${refgenepath} is not existing."
    write_usage
    exit
fi

if [ ! -e ${configfile} ]; then
    echo "${configfile} is not existing."
    write_usage
    exit
fi

if [ ! -e ${baitpath} ]; then
    echo "${baitpath} is not existing."
    write_usage
    exit
fi




#check python package dependency
install_pkg_check_1=`pip freeze | grep -c depth-tool`
if [ ${install_pkg_check_1} -eq 0 ]; then
    echo "python package depth-tool(0.0.0) is required."
fi

install_pkg_check_2=`pip freeze | grep -c pybedtools`
if [ ${install_pkg_check_2} -eq 0 ]; then
    echo "python package pybedtools(0.7.9) is required."
fi


#make directories
logdir=${outdir}/log

mkdir -p ${outdir}
mkdir -p ${outdir}/calc_depth_result
mkdir -p ${logdir}


#copy sample list for backup
configfile_name=`basename ${configfile}`
cp ${configfile} ${outdir}/${configfile_name}


#make sample name list
awk -F "[,]" '{print $1}' ${outdir}/${configfile_name} > ${outdir}/sample_list.txt

#make bam path list
awk -F "[,]" '{print $2}' ${outdir}/${configfile_name} > ${outdir}/bam_list.txt


#count all sample types
lsnum=`wc -l ${outdir}/${configfile_name}`


#making bait-reference-file
qsub -o ${logdir} -e ${logdir} -N prepatation preparation.sh ${refgenepath} ${baitpath} ${outdir}


#making intersect file for each bam
qsub -o ${logdir} -e ${logdir} -N calc_mean_depth -hold_jid preparation -t 1:${lsnum} calc_mean_depth.sh ${outdir}


#making whole intersect file as final result
qsub -o ${logdir} -e ${logdir} -N merge_result -hold_jid calc_mean_depth merge_result.sh ${outdir}


#making Rplot
qsub -o ${logdir} -e ${logdir} -N make_rplot -hold_jid merge_result making_r_plot.sh ${outdir}


exit


