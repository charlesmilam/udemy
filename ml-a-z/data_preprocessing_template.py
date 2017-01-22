# Data Preprocessing

# import the libraries
import numpy as np
import matplotlib.pyplot as pyplot
import pandas as pd
from sklearn.preprocessing import Imputer, LabelEncoder, OneHotEncoder
from sklearn.cross_validation import train_test_split

# import the dataset
dataset = pd.read_csv('Data.csv')

# view the dataset
print dataset
print

# create features matrix
X = dataset.iloc[:, : -1].values
# and view it
print X
print

# create dependent variable vector
y = dataset.iloc[:, 3].values
# and view
print y
print

# take care of missing data
imputer = Imputer('NaN')
imputer = imputer.fit(X[:, 1:3])
X[:, 1:3] = imputer.transform(X[:, 1:3])
print X
print

# encode categorical data
labeler_X = LabelEncoder()
X[:, 0] = labeler_X.fit_transform(X[:, 0])
hotlabler = OneHotEncoder(categorical_features = [0])
X = hotlabler.fit_transform(X).toarray()
print X
print
labeler_y = LabelEncoder()
y = labeler_X.fit_transform(y)
print y
print

# splitting the dataset into a training and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
print X_train, X_test, y_train, y_test
print 
