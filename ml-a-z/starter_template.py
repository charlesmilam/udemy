# Data Preprocessing

# import the libraries
import numpy as np
import matplotlib.pyplot as pyplot
import pandas as pd
from sklearn.preprocessing import Imputer, LabelEncoder, OneHotEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from pprint import pprint

# suppress printing of scientific notation
np.set_printoptions(suppress=True)

# import the dataset
dataset = pd.read_csv('Data.csv')

# view the dataset
print 'the dataset'
print dataset.head(10)
print

# create features matrix
X = dataset.iloc[:, : -1].values
# and view it
print 'features matrix: X'
print X
print

# create dependent variable vector
y = dataset.iloc[:, 3].values
# and view
print 'dependent variable: y'
print y
print

# splitting the dataset into a training and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
print 'training and testing sets'
print 'X train:', X_train
print
print 'X test:', X_test
print
print 'y train:', y_train
print
print 'y test:', y_test
print

# feature scaling
"""sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
'X train and test after feature scaling:'
print 'X train:', X_train
print
print 'X test:', X_test
print"""
