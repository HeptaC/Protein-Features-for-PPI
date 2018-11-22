#This script is not used this time.
#Merge splitted subsets for K fold cross validation.

from sklearn.ensemble import RandomForestClassifier
from sklearn.externals import joblib
import pandas
import numpy


DataPath = "E:/InterSPPIDatas/AC/"
pairName = "Ara-Hpa"

#Every subset is supposed to be of the same size
singleSetSize = 2046

#feature size
featSize = 420

#subset counts
fold=10

def main():
    for i in range(fold):
        #initialize the whole numpy array at once
        data_x = numpy.zeros(shape=[singleSetSize * (fold - 1), featSize])
        data_y = numpy.zeros(singleSetSize * (fold - 1))
        dataCnt = 0
        #traverse all other subsets
        for j in range(fold):
            if j!=i:
                # subset file name example: Ara-Gor_train_0.txt
                trainingData = pandas.read_csv(DataPath+pairName+"_train_"+str(j)+".txt",sep=',',header=None)
                #feature columns
                col = trainingData.columns.values.tolist()[1:]
                tmpx = numpy.array(trainingData[col])
                #tag column
                tmpy = numpy.array(trainingData[0])
                for idx in range(len(tmpy)):
                    data_x[dataCnt] = tmpx[idx]
                    data_y[dataCnt] = tmpy[idx]
                    dataCnt+=1
            else:
                pass

        #tags:[0,1]
        clf = RandomForestClassifier(n_estimators=1000, max_features="sqrt")
        mod = clf.fit(data_x, data_y)

        validData = pandas.read_csv(DataPath+pairName+"_train_"+str(i)+".txt",sep=',',header=None)
        # feature columns
        validDataCol = validData.columns.values.tolist()[1:]
        validData_x = numpy.array(validData[validDataCol])
        # tag column
        validData_y = numpy.array(validData[0])

        #predict
        predictFile = open(DataPath+pairName+'-'+str(i)+"-predicted.txt","w")
        #probabilities of tag 1
        predictFile.write(','.join([str(item) for item in list(mod.predict_proba(validData_x)[:,1])])+'\n')
        #predicted tags
        predictFile.write(','.join([str(item) for item in mod.predict(validData_x)])+'\n')
        #true tags
        predictFile.write(','.join([str(item) for item in validData_y])+'\n')
        predictFile.close()

        #save the model
        joblib.dump(mod, DataPath+pairName+'-rf-' + str(i) + '.model')


if __name__ == "__main__":
    main()