#download dependences
if (!require("BiocManager", quietly = TRUE))
  install.packages("BiocManager")
if(!require("topGO",quietly = T))
  BiocManager::install("topGO")

suppressPackageStartupMessages({
  library(topGO)
  library(dplyr)
  library(Rgraphviz)
  library(org.Hs.eg.db)
  library(plyr)
  library(ggplot2)
})

# function that returns TRUE/FALSE for p-values<0.05
selection <- function(allScore){ return(allScore < 0.05)} 

#allGO2genes <- annFUN.org(whichOnto="BP", feasibleGenes=NULL, mapping="org.Hs.eg.db", ID="symbol")

#function readMappings to read Gene to GO file
readMappings <- function(file, sep = "\t", IDsep = ",") {
  a <- read.delim(file = file, header = FALSE,
                  quote = "", sep = sep, colClasses = "character")
  
  ## a bit of preprocesing to get it in a nicer form
  map <- a[, 2]
  names(map) <- gsub(" ", "", a[, 1]) ## trim the spaces
  
  ## split the IDs
  return(lapply(map, function(x) gsub(" ", "", strsplit(x, split = IDsep)[[1]])))
}

#get the file Gene to GO term
geneID2GO <- readMappings(file = "/home/alexandre/Documents/LBLGC/Script/R_script/Gene2G0_Popv4 .txt")

#Get DEG's informations & filter them on Pvalue Adj
tab_deg <- read.csv("/home/alexandre/Documents/LBLGC/Script/myDEG's/No_filtered/KD_CvS_transcript.tabular", header = F, sep = "\t")
tab_deg<-filter(tab_deg, abs(V3)>1)
tab_deg<-filter(tab_deg, V7<0.05)
List_deg<-tab_deg$V7
names(List_deg)<-tab_deg$V1
List_deg<-na.omit(List_deg)

#Create "GO data" object usefull for TopGo analyse
GOdata <- new("topGOdata", 
              description = "Biological Process",
              ontology = "BP", 
              allGenes = List_deg, 
              annot = annFUN.gene2GO, 
              gene2GO = geneID2GO,
              nodeSize=1,
              geneSel=selection
)

#Enrichissement by Test of Kolmogorov-Smirnov (we can also choose wright-Fisher, etc...)
results.ks <- runTest(GOdata, algorithm="classic", statistic="ks")
goEnrichment <- GenTable(GOdata, KS=results.ks, orderBy="KS", topNodes=20)
goEnrichment$KS <- as.numeric(goEnrichment$KS)
goEnrichment <- goEnrichment[goEnrichment$KS<0.05,]
goEnrichment <- goEnrichment[,c("GO.ID","Term","KS")]
goEnrichment$Term <- gsub(" [a-z]*\\.\\.\\.$", "", goEnrichment$Term)
goEnrichment$Term <- gsub("\\.\\.\\.$", "", goEnrichment$Term)
goEnrichment$Term <- paste(goEnrichment$GO.ID, goEnrichment$Term, sep=", ")
goEnrichment$Term <- factor(goEnrichment$Term, levels=rev(goEnrichment$Term))
View(goEnrichment)

#Save the enrichissement in PNG
png("/home/alexandre/Documents/LBLGC/Script/myDEG's/No_filtered/KD_CvS_transcript.png", units="in", width=30, height=10, res=500)

#Create the network interaction of our Go terms enrichissement
ggplot(goEnrichment, aes(x=Term, y=-log10(KS))) +
  stat_summary(geom = "bar", fun = mean, position = "dodge") +
  xlab("Biological Process") +
  ylab("Enrichment") +
  ggtitle("GO Enrichment") +
  scale_y_continuous(breaks = round(seq(0, max(-log10(goEnrichment$KS)), by = 2), 1)) +
  theme_bw(base_size=24) +
  theme(
    legend.position='none',
    legend.background=element_rect(),
    plot.title=element_text(angle=0, size=24, face="bold", vjust=1),
    axis.text.x=element_text(angle=0, size=18, face="bold", hjust=1.10),
    axis.text.y=element_text(angle=0, size=18, face="bold", vjust=0.5),
    axis.title=element_text(size=24, face="bold"),
    legend.key=element_blank(),     #removes the border
    legend.key.size=unit(1, "cm"),      #Sets overall area/size of the legend
    legend.text=element_text(size=18),  #Text size
    title=element_text(size=18)) +
  guides(colour=guide_legend(override.aes=list(size=2.5))) +
  coord_flip()

dev.off()

#Save it in PNG
png("/home/alexandre/Documents/LBLGC/Script/myDEG's/No_filtered/KD_CvS_transcript_tree.png", units="in", width=20, height=15, res=500)

par(cex = 0.3)
showSigOfNodes(GOdata, score(results.ks), firstSigNodes = 5, useInfo = 'def')
dev.off()

printGraph(GOdata, results.ks, firstSigNodes = 5, fn.prefix = "KD_CvS_transcript", useInfo = "def", pdfSW = T)