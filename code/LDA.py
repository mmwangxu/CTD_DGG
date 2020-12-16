
#from mpl_toolkits.mplot3d import Axes3D

#import matplotlib.pyplot as plt
import csv

import numpy as np

#import pandas as pd

from sklearn import datasets

from sklearn.decomposition import PCA

from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

from trainandtest import *

model_lda = LinearDiscriminantAnalysis(n_components=1)
X_lda = model_lda.fit(trainMat, trainLabel).transform(trainMat)
np.savetxt("LDADeepContip.txt", X_lda)


#model_pca = PCA(n_components=3)
#X_pca = model_pca.fit(trainMat).transform(trainMat)
#np.savetxt("F:\Python\GO\Result\mine\PCAcontip.txt", X_pca)