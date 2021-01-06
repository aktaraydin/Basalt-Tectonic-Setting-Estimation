# Basalt-Tectonic-Setting-Estimation
Basalt Tectonic Setting Estimation from Georoc Basalt Data

There are 8 different Basalt data in Georoc web site. Here is the link: http://georoc.mpch-mainz.gwdg.de/georoc/

## Notebook Content:

1. Data cleaning 
  1.1. Empty column drop
  1.2. Split data according to column names 
  1.3. Row cleaning 
  
2. NaN values filling based on other column values 

3. Principal Componenet Analysis Application 
  3.1. Label Encoder Usage 
  3.2. Standar Scaler Usage 

4.Model Developing 
  4.1. Comparison of Machine Learning Methods according to accuracy score 
  4.2. Best KFold determination 
  4.3. Hyperparameter Selection with RepeatedStratifiedKFold and RandomizedSearchCV

5. Model Application 
  5.1. Other 7 data application to model with PCA 
  5.2. Model application Fail and Toughts about the fail. 
