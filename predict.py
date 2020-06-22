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
Predicting with test data set
"""

