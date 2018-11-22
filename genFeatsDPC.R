#sequences are supposed to be in the R workspace
#sequences are read through protr.readFASTA(filePath)

library(protr)
featFile = file("E:/InterSPPIDatas/DPCs.txt","w+")
seqs = GorSeqs
seqNames = names(seqs)
for(i in c(1:length(seqs))){
	DCs = extractDC(seqs[[i]]);
	writeLines(paste(seqNames[[i]],paste(DCs,collapse=';'),sep=';'),featFile)
}
seqs = HpaSeqs
seqNames = names(seqs)
for(i in c(1:length(seqs))){
	DCs = extractDC(seqs[[i]]);
	writeLines(paste(seqNames[[i]],paste(DCs,collapse=';'),sep=';'),featFile)
}
seqs = PsySeqs
seqNames = names(seqs)
for(i in c(1:length(seqs))){
	DCs = extractDC(seqs[[i]]);
	writeLines(paste(seqNames[[i]],paste(DCs,collapse=';'),sep=';'),featFile)
}
seqs = AraSeqs
seqNames = names(seqs)
for(i in c(1:length(seqs))){
	DCs = extractDC(seqs[[i]]);
	writeLines(paste(seqNames[[i]],paste(DCs,collapse=';'),sep=';'),featFile)
}
close(featFile)