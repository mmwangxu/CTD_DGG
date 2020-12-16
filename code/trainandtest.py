from numpy import *
import numpy as np

def file2metrix(filename):
    fr=open(filename, encoding='gb18030', errors='ignore')
    numline=fr.readlines()
    m=len(numline)
    returnmat=zeros((m,343))
    classlabel=[]
    index=0
    for line in numline:
        line=line.strip( )
        listfoemline=line.split(',')
        returnmat[index,:]=listfoemline[0:343]
        classlabel.append(float(listfoemline[-1]))
        index+=1
    return returnmat,classlabel

trainMat,trainLabel=file2metrix("DeepGO_GO_CONTIP.csv")
#print(trainMat,trainMat.shape)
#print(trainLabel,len(trainLabel))