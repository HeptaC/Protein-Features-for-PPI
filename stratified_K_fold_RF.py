from sklearn.ensemble import RandomForestClassifier
from sklearn.externals import joblib
from sklearn.metrics import precision_recall_curve,classification_report,average_precision_score,auc
from sklearn.model_selection import KFold,StratifiedKFold
from sklearn.utils.fixes import signature
import pandas
import numpy
import matplotlib.pyplot as plt

#Training data file name example: Ara-Gor_train_0.txt
featName = 'AC'
DataPath = "E:/InterSPPIDatas/"+featName+"/"
pairName = "Ara-All_pathogen"

fold = 10


#times = 10
i = 0 #Training data file name suffix

#P-R plotting args
step_kwargs = ({'step': 'post'}
            if 'step' in signature(plt.fill_between).parameters
            else {})

def main():
    # for i in range(times):
        totalauprc = 0
        data = pandas.read_csv(DataPath + pairName + "_train_" + str(i) + ".txt", sep=',', header=None)
        dataCol = data.columns.values.tolist()[1:]
        data_x = numpy.array(data[dataCol])
        data_y = numpy.array(data[0])

        #kf2 = KFold(n_splits=10)
        kf = StratifiedKFold(n_splits=10)
        splitted = kf.split(data_x,data_y)

        for j,(train,test) in enumerate(splitted):
            clf = RandomForestClassifier(n_estimators=1000, max_features="sqrt")
            mod = clf.fit(data_x[train], data_y[train])
            probs = mod.predict_proba(data_x[test])
            predicts = mod.predict(data_x[test])
            print(predicts)
            print(data_y[test])
            print(classification_report(data_y[test],predicts))
            #P-R datas
            precision, recall, thresholds = precision_recall_curve(data_y[test],probs[:,1])
            #P-R auc
            tmpauc = auc(recall,precision)
            totalauprc+=tmpauc
            print(tmpauc)
            #joblib.dump(mod, ModelPath + pairName + '-rf-' + str(i) +'-'+str(j)+ '.model')

            #plotting P-R
            plt.step(recall, precision, color='b', alpha=0.1,where='post')
            plt.fill_between(recall, precision, alpha=0.1, color='b', **step_kwargs)

        #average auPRC
        print(totalauprc/fold)
        # plotting P-R
        plt.xlabel('Recall')
        plt.ylabel('Precision')
        plt.ylim([0.0, 1.05])
        plt.xlim([0.0, 1.05])
        plt.title('2-class Precision-Recall curve-'+pairName+'-'+featName)
        plt.show()


if __name__ == "__main__":
    main()