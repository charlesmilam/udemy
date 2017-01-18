# Data Preprocessing

# import the libraries
import numpy as np
import matplotlib.pyplot as pyplot
import pandas as pd

# import the dataset
dataset = pd.read_csv('Data.csv')

# view the dataset
print dataset

# create features matrix
X = dataset.iloc[:, : -1].values
# and view it
print X

# create dependent variable vector
y = dataset.iloc[:, 3].values
# and view
print y
