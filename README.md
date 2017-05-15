# make_mean_depth_plot

<h3>for usage</h3>
bash ./runall.sh 'path of refGene.txt' 'path of sample name list' 'path of bam directory' 'path of bait file' 'path of result directory'

<br>
(eg). bash ./runall.sh ./refGene.txt ./sample_list.txt ./data/JALSG_bam ./JALSG_sample.bed ./result

<br>
<br>

<h3>result</h3>
This program will make ./result directory.<br>
./result/table.txt -> table of mean depth of all samples.
./result/result.png -> boxplot of lower depth exome whose mean-depth is under 50 calculated by all samples..

