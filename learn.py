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

import util

"""
Create neural network from learning data set
"""

# Returns DataFrame. A comma-separated values (csv) file is returned as two-dimensional data structure with labeled axes.
print(Back.GREEN + "Loading dataset from file" + Style.RESET_ALL)
dataset = pd.read_csv('raw_games_scored_states.csv', header=None)

print(Back.GREEN + "selects first 169 columns" + Style.RESET_ALL)
X = dataset.iloc[:, 0:169].values # selects first 9 columns
y = dataset.iloc[:, 169:170].values # select the last column

print(Back.GREEN + "Encode categorical variables as numeric" + Style.RESET_ALL)
labelencoder_X = util.getlabelencoder()
for _ in range(169):
    X[:, _] = labelencoder_X.transform(X[:, _])

print(Back.GREEN + "Encode target categorical variable as numberic" + Style.RESET_ALL)
labelencoder_y = util.getlabelencoderSc()
y[:, 0] = labelencoder_y.transform(y[:, 0])

print(Back.GREEN + "Onehot encode all dependent categorical variables" + Style.RESET_ALL)
onehotencoder = util.getonehotencoder()
X = onehotencoder.transform(X).toarray()

print(Back.GREEN + "Remove every third column" + Style.RESET_ALL)
X = util.remove3rdcols(X)

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
print(X_train)

# Initialize neural network
nnet = Sequential()

# Add first hidden layer (and input layer)
nnet.add(Dense(units=169, kernel_initializer='uniform', activation='relu', input_dim=338))

# Add second hidden layer
nnet.add(Dense(units=169, kernel_initializer='uniform', activation='relu'))

# Add output layer
nnet.add(Dense(units=1, kernel_initializer='uniform', activation='sigmoid'))

# Compile network
nnet.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

print(Back.GREEN + "Train network" + Style.RESET_ALL)
nnet.fit(X_train, y_train, batch_size=10, epochs=100)

print(Back.GREEN + "Predicting the test set results" + Style.RESET_ALL)
y_pred = nnet.predict(X_test)
count = 0
for _ in range(len(y_pred)):
    if y_test[_] == round(y_pred[_][0]):
        count += 1
print(f"{count} / {len(y_pred)} = {count/len(y_pred)}%")

print(Back.GREEN + "Saving model to disk" + Style.RESET_ALL)
# serialize model to JSON
model_json = nnet.to_json()
with open("model.json", "w") as json_file:
    json_file.write(model_json)
# serialize weights to HDF5
nnet.save_weights("model.h5")