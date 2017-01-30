# Data Preprocessing Template

# Importing the dataset
dataset = read.csv('50_Startups.csv')

# encode the categorical state data
dataset$State = factor(dataset$State,
                       levels = c('New York', 'California', 'Florida'),
                       labels = c(1, 2, 3))

# Splitting the dataset into the Training set and Test set
# install.packages('caTools')
library(caTools)
set.seed(123)
split = sample.split(dataset$Profit, SplitRatio = 0.8)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)

# fit multiple linear regression to training set
regr = lm(formula = Profit ~ ., 
          data = training_set)
summary(regr)

# predict the test set results
pred = predict(regr, newdata = test_set)
