# make_mean_depth_plot

<h3>for usage</h3>
cd ./script
bash ./runall.sh 'path of refGene.txt' 'path of sample name list' 'path of bam directory' 'path of bait file' 'path of result directory'

<br>
(eg). bash ./runall.sh ./refGene.txt ./sample_list.txt ./data/JALSG_bam ./JALSG_sample.bed ./result

<br>
<br>

<h3>result</h3>
Within the path of result directory (you chose in the runall.sh script), two outcomes will be made.<br><br>
./result/table.txt -> table of mean depth of all samples.<br>
./result/result.png -> boxplot of lower depth exome whose mean-depth is under 50 calculated by all samples.<br>

