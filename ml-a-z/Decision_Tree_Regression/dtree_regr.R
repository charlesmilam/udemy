# Decision Tree Regression 

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

# fit regression to dataset
library(rpart)
regr = rpart(formula=Salary ~ ., 
             data=dataset,
             control=rpart.control(minsplit = 1))

# predict a new single result
new_pred = predict(regr, data.frame(Level = 6.5))

# visualize the results
library(ggplot2)
x_grid = seq(min(dataset$Level), max(dataset$Level), 0.01)
ggplot() +
  geom_point(aes(x = dataset$Level, y = dataset$Salary), 
             color = 'red') +
  geom_line(aes(x = x_grid, y = predict(regr, newdata = data.frame(Level = x_grid))), color = 'steelblue') +
  ggtitle('Truth or Bluff') +
  xlab('Level') +
  ylab('Salary')


