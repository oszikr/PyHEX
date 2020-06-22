import numpy as np
import pandas as pd
from colorama import Fore, Back, Style

from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

from keras.models import Sequential
from keras.layers import Dense
from keras.models import model_from_json

import util

"""
Create neural network from learning data set
"""

# Returns DataFrame. A comma-separated values (csv) file is returned as two-dimensional data structure with labeled axes.
print(Back.GREEN + "Loading dataset from file" + Style.RESET_ALL)
dataset = pd.read_csv('raw_games_scored_states.csv', header=None)

X = dataset.iloc[:, 0:169].values # selects first 9 columns
y = dataset.iloc[:, 169:170].values # select the last column

labelencoder_X = util.getlabelencoder()
for _ in range(169):
    X[:, _] = labelencoder_X.transform(X[:, _])

labelencoder_y = util.getlabelencoderSc()
y[:, 0] = labelencoder_y.transform(y[:, 0])

onehotencoder = util.getonehotencoder()
X = onehotencoder.transform(X).toarray()

X = util.remove3rdcols(X)

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
print(X_train)

# Initialize neural network
nnet = util.getnnet()

print(Back.GREEN + "Predicting the test set results" + Style.RESET_ALL)
y_pred = nnet.predict(X_test)
count = 0
for _ in range(len(y_pred)):
    print("Expected:", y_test[_], "Actual:", round(y_pred[_][0] , 10))
    if y_test[_] == round(y_pred[_][0]):
        count += 1
print(f"{count} / {len(y_pred)} = {count/len(y_pred)}%")
