# Data Preprocessing

# import the libraries
import numpy as np
import matplotlib.pyplot as pyplot
import pandas as pd
from sklearn.preprocessing import Imputer

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
