# Polynomial Regression
# %%
# import the libraries
import numpy as np
import matplotlib.pyplot as pyplot
import pandas as pd
from sklearn.preprocessing import Imputer, LabelEncoder, OneHotEncoder, StandardScaler, PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
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

# %%
# fit linear regression to the dataset
linear_regr = LinearRegression()
linear_regr.fit(X, y)

# %%
# fit polynomial regression to the dataset
poly_regr = PolynomialFeatures(2)
X_poly = poly_regr.fit_transform(X)

# %%
# fit X_poly to new linear regression
linear_regr2 = LinearRegression()
linear_regr2.fit(X_poly, y)
