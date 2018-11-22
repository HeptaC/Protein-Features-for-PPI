#copy fasta files used in datasets into an other directory
import os
import shutil

seqNames = set()
#splitted fasta directory
fastaDir = 'E:/InterSPPIDatas/splited/'
#target directory
outDir = 'E:/InterSPPIDatas/used/'
outFileName = 'E:/InterSPPIDatas/used_seqs.txt'
#Original dataset directories
dataPaths = ['E:/InterSPPIDatas/Independent_data/','E:/InterSPPIDatas/Training_data/']

for dataPath in dataPaths:
    fileNames = os.listdir(dataPath)
    for fileName in fileNames:
        tmpFile = open(dataPath+fileName,'r')
        for line in tmpFile.readlines()[1:]:
            datas = line.strip().split()
            seqNames.add(datas[1])
            seqNames.add(datas[2])
        tmpFile.close()

outFile = open(outFileName,'w')
for seqName in seqNames:
    outFile.write(seqName+'\n')
    shutil.copyfile(fastaDir + seqName + '.fasta', outDir + seqName + '.fasta')

outFile.close()