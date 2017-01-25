# Data Preprocessing Template

# Importing the dataset
dataset = read.csv('Salary_Data.csv')

# Splitting the dataset into the Training set and Test set
# install.packages('caTools')
library(caTools)
set.seed(123)
split = sample.split(dataset$Salary, SplitRatio = 0.67)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)

# fit simple linear regression to trainging set
regr = lm(formula = Salary ~ YearsExperience, 
          data = training_set)

# predict the test set
y_pred = predict(regr, newdata = test_set)

# visualize the training set results
# install.packages('ggplot2')
library(ggplot2)
ggplot() +
  geom_point(aes(x = training_set$YearsExperience, y = training_set$Salary),
             color = 'red') +
  geom_point(aes(x = test_set$YearsExperience, y = test_set$Salary),
             color = 'green') +
  geom_line(aes(x = training_set$YearsExperience, y = predict(regr, newdata = training_set)),
            color = 'blue') +
  ggtitle('Salary vs Experience') +
  xlab('Year of Expeience') +
  ylab('Salary')