# Polynomial Regression
# %%
# import the libraries
import numpy as np
import matplotlib.pyplot as pyplot
import pandas as pd
from sklearn.preprocessing import Imputer, LabelEncoder, OneHotEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from pprint import pprint

# suppress printing of scientific notation
np.set_printoptions(suppress=True)

# %%
# import the dataset
dataset = pd.read_csv('Position_Salaries.csv')

# %%
# create features matrix
X = dataset.iloc[:, 1:-1].values
# create dependent variable vector
y = dataset.iloc[:, -1].values
