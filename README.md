# make_mean_depth_plot

<h3>Usage</h3>
cd ./script<br>
bash ./runall.sh 'path of refGene.txt' 'path of sample name list' 'path of bam directory' 'path of bait file' 'path of result directory'<br>

<br>
(eg). bash ./runall.sh ./refGene.txt ./sample_list.txt ./data/JALSG_bam ./JALSG_sample.bed ./result<br>

　refGene.txt：　refGene.txtのパス<br>
　sample_list.txt：　検体リストのパス<br>
　./data/JALSG_bam：　bamのパス<br>
　./JALSG_sample.bed：　baitのパス<br>
　./result：　出力先<br>

<br>
<br>

<h3>Output</h3>
Within the path of result directory (you chose in the runall.sh script), two outcomes will be made.<br><br>
./result/table.txt -> table of mean depth of all samples.<br>
./result/result.png -> boxplot of lower depth exome whose mean-depth is under 50 calculated by all samples.<br>

