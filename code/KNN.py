import sys
import numpy as np
from numpy import *
from sklearn.model_selection import StratifiedKFold
from sklearn import datasets
from sklearn import metrics
from sklearn.metrics import classification_report
from sklearn.neighbors.nearest_centroid import NearestCentroid

#output=sys.stdout
#type = sys.getfilesystemencoding()
#outputfile=open('contipLDA+KNN_RESULT.txt','a',encoding='utf-8')
#sys.stdout=outputfile

def file2metrix(filename):
    fr=open(filename, encoding='gb18030', errors='ignore')
    numline=fr.readlines()
    m=len(numline)
    returnmat=zeros((m,1))
    classlabel=[]
    index=0
    for line in numline:
        line=line.strip( )
        listfoemline=line.split(',')
        returnmat[index,:]=listfoemline[0:1]
        classlabel.append(float(listfoemline[-1]))
        index+=1
    return returnmat,classlabel

#trainMat,trainLabel=file2metrix("DeepGO_GO_LDA.csv")
trainMat,trainLabel=file2metrix("LDADeepGOContip.csv")
clf = NearestCentroid(metric='euclidean', shrink_threshold=15).fit(trainMat, trainLabel)
print('K=15')
trainLabel = np.array(trainLabel)

ACCs = []
#Recalls = []
MCCS = []
skf = StratifiedKFold(n_splits=5, random_state=None, shuffle=False)
for train_index, test_index in skf.split(trainMat, trainLabel):
    #print("TRAIN:", train_index, "TEST:", test_index)
    X_train, X_test = trainMat[train_index], trainMat[test_index]
    y_train, y_test = trainLabel[train_index], trainLabel[test_index]
    #train_pred = clf.predict(X_train)
    #print ('train_ACC=',metrics.accuracy_score(y_train, train_pred))
    #print (clf.score(x_test, Lab_test))
    test_pred = clf.predict(X_test)
    ACC = metrics.accuracy_score(y_test, test_pred)
	
    #recall = metrics.recall_score(y_test, test_pred, average='micro')
    MCC = metrics.matthews_corrcoef(y_test, test_pred)
    print ('ACC=',ACC)
    #print ('recall=',recall)
    print ('MCC=',MCC)
    ACCs.append(ACC)
    #Recalls.append(recall)
    MCCS.append(MCC)
    target_names = ['class 0','class 1']
    print(classification_report(y_test, test_pred, digits=4, target_names=target_names))

print("ACC=",np.mean(ACCs),"MCC=",np.mean(MCCS))


#test = model.score (testData,testLabel)

#print ('KNN_ACC：', test)