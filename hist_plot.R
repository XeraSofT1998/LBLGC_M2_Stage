library(ggplot2)

#give the count of transcript find in rMATs and SUPPA2
dt<-data.frame(Count=c(78, 190, 36, 101,
                       287, 503, 792, 1025,
                       303, 388, 857, 1142),Sample=c("RNAi-ddm1 S transcrit", "RNAi-ddm1 S","RNAi-ddm1 C", "RNAi-ddm1 C",
                                                                                      "OX-dml S", "OX-dml S","OX-dml C", "OX-dml C",
                                                                                      "RNAi-dml  S", "RNAi-dml  S", "RNAi-dml  C", "RNAi-dml  C"),type=rep(c("DET's sans DMC","DET's avec DMC"),2))

#The path to save the output
png("/home/alexandre/Documents/Rstudio/Histogram_DET_With_and_without_DMC_Conditions_Sécheresse_Control.png",units="px", width=4200, height=3500, res=500)

#Create the plot
p<-ggplot(data=dt, aes(x = Sample,y=Count,fill=type))+
  geom_bar(stat='identity')+
  geom_col(width = 0.001) +
  theme_minimal()+
  scale_fill_manual(values = c("DET's sans DMC"="orange","DET's avec DMC"="#6FAD7A"))
p+labs(x ="Echantillons", y = "Nombre de gènes ou de transcrits différentiellement exprimés")+
  theme(plot.title = element_text(color="black", size=1, face="bold",hjust = 0.5, angle = 90)
        + theme(axis.text.x = element_text(angle = 90, vjust = 0.5, hjust=1))
  )

dev.off()



