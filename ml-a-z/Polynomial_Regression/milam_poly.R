# Polynomial Regression

# Importing the dataset
dataset = read.csv('Position_Salaries.csv')
dataset = dataset[2:3]

# Splitting the dataset into the Training set and Test set
# install.packages('caTools')
# library(caTools)
# set.seed(123)
# split = sample.split(dataset$DependentVariable, SplitRatio = 0.8)
# training_set = subset(dataset, split == TRUE)
# test_set = subset(dataset, split == FALSE)

# Feature Scaling
# training_set = scale(training_set)
# test_set = scale(test_set)

# fit linear regression to dataset
lin_regr = lm(formula = Salary ~ ., data = dataset)


# fit polynomial regression to dataset
dataset$Level2 = dataset$Level ^ 2
dataset$Level3 = dataset$Level ^ 3
dataset$Level4 = dataset$Level ^ 4
poly_regr = lm(formula = Salary ~ ., data = dataset)

# visualize the results
library(ggplot2)
ggplot() +
  geom_point(aes(x = dataset$Level, y = dataset$Salary), 
             color = 'red') +
  geom_line(aes(x = dataset$Level, y = predict(lin_regr, newdata = dataset)), color = 'blue') +
  geom_line(aes(x = dataset$Level, y = predict(poly_regr, newdata = dataset)), color = 'steelblue') +
  ggtitle('Truth or Bluff') +
  xlab('Level') +
  ylab('Salary')

# predict a new single result
new_pred = predict(lin_regr, data.frame(Level = 6.5))
new_poly_pred = predict(poly_regr, data.frame(Level = 6.5, 
                                              Level2 = 6.5^2, 
                                              Level3 = 6.5^3, 
                                              Level4 = 6.5^4))
