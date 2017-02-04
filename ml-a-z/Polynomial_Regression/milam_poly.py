# Polynomial Regression
# %%
# import the libraries
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.preprocessing import Imputer, LabelEncoder, OneHotEncoder, StandardScaler, PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from pprint import pprint

%matplotlib inline

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
poly_regr = PolynomialFeatures(4)
X_poly = poly_regr.fit_transform(X)

# %%
# fit X_poly to new linear regression
linear_regr2 = LinearRegression()
linear_regr2.fit(X_poly, y)

# %%
# visualize the results
X_grid = np.arange(min(X), max(X), 0.1)
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(X, y, color = 'red')
plt.plot(X, linear_regr.predict(X), color = 'blue')
plt.plot(X_grid, linear_regr2.predict(poly_regr.fit_transform(X_grid)), color = 'steelblue')
plt.title('Truth vs Bluff')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()

# %%
# predict new result with linear regression and polynomial regression
linear_regr.predict(6.5)
linear_regr2.predict(poly_regr.fit_transform(6.5))
