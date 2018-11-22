#sequences are supposed to be in the R workspace
#sequences are read through protr.readFASTA(filePath)

library(protr)
featFile = file("E:/InterSPPIDatas/acs.txt","w+")
seqs = GorSeqs
seqNames = names(seqs)
for(i in c(1:length(seqs))){
	ACs = extractScales(x=seqs[[i]],propmat=aa7,pc=7,lag=30)[0:210];
	writeLines(paste(seqNames[[i]],paste(ACs,collapse=';'),sep=';'),featFile)
}
seqs = HpaSeqs
seqNames = names(seqs)
for(i in c(1:length(seqs))){
	ACs = extractScales(x=seqs[[i]],propmat=aa7,pc=7,lag=30)[0:210];
	writeLines(paste(seqNames[[i]],paste(ACs,collapse=';'),sep=';'),featFile)
}
seqs = PsySeqs
seqNames = names(seqs)
for(i in c(1:length(seqs))){
	ACs = extractScales(x=seqs[[i]],propmat=aa7,pc=7,lag=30)[0:210];
	writeLines(paste(seqNames[[i]],paste(ACs,collapse=';'),sep=';'),featFile)
}
seqs = AraSeqs
seqNames = names(seqs)
for(i in c(1:length(seqs))){
	if(nchar(seqs[[i]])>30){
		ACs = extractScales(x=seqs[[i]],propmat=aa7,pc=7,lag=30)[0:210];
		writeLines(paste(seqNames[[i]],paste(ACs,collapse=';'),sep=';'),featFile)
	}
}
close(featFile)