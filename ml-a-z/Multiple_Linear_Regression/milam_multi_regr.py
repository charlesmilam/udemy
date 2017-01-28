# Data Preprocessing Template
# %%
# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import Imputer, LabelEncoder, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# suppress printing of scientific notation
np.set_printoptions(suppress=True)

# %%
# Importing the dataset
dataset = pd.read_csv('50_Startups.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

# %%
# %%
# encode categorical data
labeler_X = LabelEncoder()
X[:, 3] = labeler_X.fit_transform(X[:, 3])
hotlabler = OneHotEncoder(categorical_features = [3])
X = hotlabler.fit_transform(X).toarray()

# %%0
# Splitting the dataset into the Training set and Test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# %%
# fit multiple linear regression to training set
regr = LinearRegression()
regr.fit(X_train, y_train)

# %%
# predict test set results
pred = regr.predict(X_test)
score = regr.score(X_test, y_test)
