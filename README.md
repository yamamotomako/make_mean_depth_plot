# make_mean_depth_plot

<h3>Usage</h3>
cd ./script<br>
bash ./runall.sh 'path of sample name & bam path list' 'path of bait file' 'path of result directory'<br>

<br>
(eg). bash ./runall.sh ./sample_path_list.txt ./JALSG_sample.bed ./result<br>

　./sample_path_list.txt：　検体リストとそのbamファイルパス<br>
　./sample.bed：　baitのパス<br>
　./result：　出力先<br>

<br>
<br>

<h3>Output</h3>
Within the path of result directory (you chose in the runall.sh script), two outcomes will be made.<br><br>
./result/table.txt -> table of mean depth of all samples.<br>
./result/result.png -> boxplot of lower depth exome whose mean-depth is under 50 calculated by all samples.<br>

