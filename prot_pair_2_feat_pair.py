#Original data format:
#label Ara-prot-name pathogen-prot-name
#...

#Needed data format:
#label,feat-value1,feat-value2,...

from sklearn.ensemble import RandomForestClassifier
import re
import os

#featsFile contains lines of protein name and feature values
#example: proteinname;val1;val2;val3;...
featsFilePath = "E:/InterSPPIDatas/DPC/dpcs.txt"
seperator = ';'

#the directory for training datas (with headers)
dataPath = "E:/InterSPPIDatas/Training_data/"

#output path
outPath = "E:/InterSPPIDatas/DPC/"

#protdic stores proteins' features in featsFile
protdic = dict()

def main():
    #read features into protdic
    featsFile = open(featsFilePath, "r")
    for line in featsFile.readlines():
        prot = line.split(seperator)
        name = prot[0].split()[0]
        feat = prot[1:] #should have used str.strip()
        protdic[name] = feat

    #traverse all training data files
    traing_files = os.listdir(dataPath)
    for fileName in traing_files:
        tmpDataFile = open(dataPath+fileName,"r")
        outFile = open(outPath+fileName,"w")
        for line in tmpDataFile.readlines()[1:]: #ignore headers
            data = line.split()
            outFile.write(data[0]+','+','.join(protdic[data[1]])[:-1]+','+','.join(protdic[data[2]])) # there's one '\n' at the end of each protein feature in featFile
        tmpDataFile.close()
        outFile.close()

    featsFile.close()

#entrance
if __name__=="__main__":
    main()
