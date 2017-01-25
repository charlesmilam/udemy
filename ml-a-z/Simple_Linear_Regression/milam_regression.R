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

