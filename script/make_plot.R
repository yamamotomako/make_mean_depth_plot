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

data1 <- data %>% tidyr::gather(key=sample, value=depth, -bait)
data2 <- data1 %>% group_by(bait) %>% summarize(M=mean(depth)) %>% arrange(M)
data3 <- data2 %>% filter(M <= 50)

badBait <- data3$bait

data4 <- data1 %>% filter(bait %in% badBait)

ggplot(data4, aes(x=bait, y=depth, fill=bait)) + geom_boxplot() + theme(axis.text.x=element_text(angle=90)) + guides(fill=FALSE)
ggsave(save_path)



#make summary table sortby chrmsome
test <- data2 %>% mutate(chrm=substr(bait,1,regexpr(":",bait)-1))
test2 <- test %>% group_by(chrm) %>% summarize(Mean=mean(MM))
test3 <- test2 %>% mutate(aaa=as.integer(sub("chr","",chrm))) %>% arrange(aaa)
as.integer(test3$aaa)
round(test3$Mean, digit=2)

write.table(test3[c(1,2)], paste0(outdir, "/summary.txt"), row.names = FALSE, quote=FALSE, append=FALSE)






