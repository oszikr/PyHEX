# https://www.kdnuggets.com/2017/09/neural-networks-tic-tac-toe-keras.html
# https://pandas.pydata.org/docs/reference/api/pandas.Series.iloc.html#pandas.Series.iloc
# https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html
import numpy as np
import pandas as pd
from colorama import Fore, Back, Style
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from keras.models import Sequential
from keras.layers import Dense
from keras.models import model_from_json

"""
Collections of read network, encoders and functions to learn and predict.
"""

def getnnet():
    json_file = open('model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    nnet = model_from_json(loaded_model_json)
    nnet.load_weights("model.h5")
    return nnet

def getlabelencoder():
    labelencoder = LabelEncoder()
    labelencoder.fit([0, 1, 2]) # 0,1,2 == blank, blue, red || or process variable
    return labelencoder

def getlabelencoderSc():
    labelencoder = LabelEncoder()
    labelencoder.fit(['negative', 'positive'])
    return labelencoder

def getonehotencoder():
    onehotencoder = OneHotEncoder()

    array0 = np.array([], dtype="object")
    array1 = np.array([], dtype="object")
    array2 = np.array([], dtype="object")
    n = 13
    for i in range(n*n+1):
        array0 = np.append(array0, 0)
        array1 = np.append(array1, 1)
        array2 = np.append(array2, 2)

    onehotencoder.fit([
        array0,
        array1,
        array2
    ])
    return onehotencoder

def remove3rdcols(X, limit):
    print("remove3rdcols>", "size:", X.shape[1], "limit:", limit)
    colstodelete = []
    for i in range(X.shape[1]): # range(3*169+1) = 507+1 = 508 => for(i=0; i<508; i++)
        #if i % 3 == 0 and i < limit:
        colstodelete.append(i) # i = 0, 3, 6, .. 504
    X = np.delete(X, colstodelete, axis=1)
    return X