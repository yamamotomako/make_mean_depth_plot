targetPackages <- c("ggplot2", "dplyr", "tidyr", "pipeR")
newPackages <- targetPackages[!(targetPackages %in% installed.packages()[,"Package"])]
if(length(newPackages)) install.packages(newPackages, repos = "https://cran.ism.ac.jp/")
for(package in targetPackages) library(package, character.only = T)




library(ggplot2)
library(dplyr)
library(tidyr)
library(pipeR)

args <- commandArgs(trailingOnly = T)
outdir <- args[1]
data_path <- paste0(outdir, "/table.txt")
save_path <- paste0(outdir, "/result.png")

data <- read.table(data_path, stringsAsFactors=FALSE, header=TRUE, sep="\t")

data1 <- data %>% tidyr::gather(key=sample, value=depth, JALSG_001:JALSG_220)
data2 <- data1 %>% group_by(bait) %>% summarize(M=mean(depth)) %>% arrange(M)
data3 <- data2 %>% filter(M <= 50)

badBait <- data3$bait

data4 <- data1 %>% filter(bait %in% badBait)

<<<<<<< HEAD
ggplot(data4, aes(x=bait, y=depth, fill=bait)) + geom_boxplot() + theme(axis.text.x=element_text(angle=90)) + geom_label_repel(show.legend=TRUE)
=======
ggplot(data4, aes(x=bait, y=depth, fill=bait)) + geom_boxplot() + theme(axis.text.x=element_text(angle=90))
>>>>>>> 060ce20899bd18392434292d31f8712883ca951a
ggsave(save_path)




