# Data Preprocessing Template
# %%
# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import Imputer, LabelEncoder, OneHotEncoder
from sklearn.model_selection import train_test_split

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
# Feature Scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train)"""
