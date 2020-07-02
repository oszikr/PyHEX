import numpy as np
import pandas as pd
from colorama import Fore, Back, Style

from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

from keras.models import Sequential
from keras.layers import Dense
from keras.models import model_from_json
import json
import util

"""
Predicting 
"""

def predictOne(X):
    y_pred = predict([X])
    return y_pred[0]

def predict(X):
    for _ in range(len(X)):
        X[_] = labelencoder.transform(X[_])

    X = onehotencoder.transform(X).toarray()

    X = util.remove3rdcols(X)

    y_pred = nnet.predict(X)
    return y_pred

if __name__ == "__main__":
    nnet = util.getnnet()
    labelencoder = util.getlabelencoder()
    onehotencoder = util.getonehotencoder()
    while True:
        print("Enter input")
        inputStr = input()
        #print("Got:", inputStr)
        if inputStr in ("quit", "q"):
            exit(0)
        #inputStr = "[[0,0,0,0,0,0,0,1,1,0,1,2,0,0,0,0,0,0,0,0,0,0,1,2,0,0,0,0,0,0,0,0,0,0,0,1,2,0,0,0,0,0,0,0,0,2,1,2,2,0,0,0,0,0,0,0,0,0,2,2,1,2,0,0,0,0,0,0,0,0,1,2,1,2,0,0,0,0,0,0,0,1,1,2,1,2,1,0,0,0,0,0,1,0,2,0,2,1,1,0,0,0,0,0,0,0,0,0,0,2,2,2,0,0,0,0,0,0,0,0,0,2,1,1,1,0,0,0,0,0,0,0,1,0,2,0,0,0,0,0,0,0,0,0,0,0,1,2,0,0,0,0,0,0,0,0,0,0,0,2,1,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,1,1,0,1,2,0,0,0,0,0,0,0,0,0,0,1,2,0,0,0,0,0,0,0,0,0,0,0,1,2,0,0,0,0,0,0,0,0,2,1,2,2,0,0,0,0,0,0,0,0,0,2,2,1,2,0,0,0,0,0,0,0,0,1,2,1,2,0,0,0,0,0,0,0,1,1,2,1,2,1,0,0,0,0,0,1,0,2,0,2,1,1,0,0,0,0,0,0,0,0,0,0,2,2,2,0,0,0,0,0,0,0,0,0,2,1,1,1,0,0,0,0,0,0,0,1,0,2,0,0,0,0,0,0,0,0,0,0,0,1,2,0,0,0,0,0,0,0,0,0,0,0,2,1,0,0,0,0,0,0,0,0]]"
        param = json.loads(inputStr)
        Y = predict(param)
        outputJson = ''
        for _ in range(len(Y)):
            if _ != 0:
                outputJson += ","
            outputJson += Y[_][0].__str__()
        result = '{"Result" : [' + outputJson + ']}'

        print(result)