# %%
# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
%matplotlib inline

# %%
# Importing the dataset
dataset = pd.read_csv('Salary_Data.csv')
dataset

# %%
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values
X, y

# %%
# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.33, random_state = 0)

# %%
X_train
X_test
y_train
y_test

# %%
# fit the simple linear regression to training set
from sklearn.linear_model import LinearRegression
regr = LinearRegression()
regr.fit(X_train, y_train)
regr.coef_
regr.intercept_

# %%
# predicit test set results
y_pred = regr.predict(X_test)
y_test, y_pred
score = regr.score(X_test, y_test)
score

# %%
# visualize the training set results
plt.scatter(X_train, y_train, color = 'red')
plt.scatter(X_test, y_test, color = 'green')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Salary vs Experience')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()
