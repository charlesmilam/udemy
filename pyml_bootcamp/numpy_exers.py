import numpy as np

# create an array of 10 zeros
arr_0s = np.zeros(10)
print(arr_0s)

# create an array of 10 ones
arr_1s = np.ones(10)
print(arr_1s)
print()

# create an array of 10 fives
arr_5s = np.ones(10) * 5
print(arr_5s)
print()

# create an array of the integers from 10 to 50
arr_ints10to50 = np.arange(10, 51)
print(arr_ints10to50)
print()

# create an array of even integers from 10 to 50
arr_evenints_10to50 = np.arange(10, 51, 2)
print(arr_evenints_10to50)
print()

# create a 3x3 identity matrix
arr_eye3x3 = np.eye(3, 3)
print(arr_eye3x3)
print()

# generate a random number between 0 and 1
print(np.random.rand())
print()

# generate an array of 25 random numbers from std normal distribution
print(np.random.rand(25))
print()

# generate a specific matrix
print(np.linspace(0.01, 1.0, 100).reshape(10, 10))
print()

# create an array of 20 linearly spaced points between 0 and 1
print(np.linspace(0, 1, 20))
print()

# index and selection exercises
mat = np.arange(1, 26).reshape(5, 5)
print(mat)
print(mat[2:, 1:])
print(mat[3, 4])
print(mat[:3, 1].reshape(3, 1))
print(mat[4])
print(mat[3:])
print()

# sum of all values in mat
print(mat.sum())
print()

# standard deviation of values in mat
print(mat.std())
print()

# sum of columns in mat
print(mat.sum(axis=0))
print()
