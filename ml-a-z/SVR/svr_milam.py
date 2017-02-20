# regression model template
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
X = dataset.iloc[:, 1:2].values
# create dependent variable vector
y = dataset.iloc[:, 2].values

# %%
# take care of missing data
# imputer = Imputer('NaN')
# imputer = imputer.fit(X[:, 1:3])
# X[:, 1:3] = imputer.transform(X[:, 1:3])

# %%
# encode categorical data
# labeler_X = LabelEncoder()
# X[:, 0] = labeler_X.fit_transform(X[:, 0])
# hotlabler = OneHotEncoder(categorical_features = [0])
# X = hotlabler.fit_transform(X).toarray()
# labeler_y = LabelEncoder()
# y = labeler_X.fit_transform(y)

# %%
# splitting the dataset into a training and test set
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# %%
# feature scaling
sc_X = StandardScaler()
sc_y = StandardScaler()
X = sc_X.fit_transform(X)
y = sc_y.fit_transform(y)

# %%
# fit the SVR to the dataset
from sklearn.svm import SVR
regr = SVR(kernel='rbf')
regr.fit(X, y)

# %%
# predict results
pred = regr.predict(6.5)

# %%
# visualize the results
X_grid = np.arange(min(X), max(X), 0.1)
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(X, y, color = 'red')
plt.plot(X_grid, regr.predict(X_grid), color = 'steelblue')
plt.title('Truth vs Bluff')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()
