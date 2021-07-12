import os
import copy
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('final_train.csv')

# Copy Data
df = copy.deepcopy(data)
df.columns
df = df.drop('Id',axis = 1)


# Set outlier thresholds
def outlier_thresholds(dataframe, col_name, th1=0.05, th3=0.95):
    quartile1 = dataframe[col_name].quantile(th1)
    quartile3 = dataframe[col_name].quantile(th3)
    interquantile_range = quartile3 - quartile1
    up_limit = quartile3 + 1.5 * interquantile_range
    low_limit = quartile1 - 1.5 * interquantile_range
    return low_limit, up_limit

  
# Check for outliers
def check_outlier(dataframe, col_name):
    low_limit, up_limit = outlier_thresholds(dataframe, col_name)
    if dataframe[(dataframe[col_name] > up_limit) | (dataframe[col_name] < low_limit)].any(axis=None):
        return True
    else:
        return False

# Replace outliers with boundary values
def replace_with_thresholds(dataframe, col_name, th1=0.05, th3=0.95):
    low_limit, up_limit = outlier_thresholds(dataframe, col_name, th1, th3)
    if low_limit > 0:
        dataframe.loc[(dataframe[col_name] < low_limit), col_name] = low_limit
        dataframe.loc[(dataframe[col_name] > up_limit), col_name] = up_limit
    else:
        dataframe.loc[(dataframe[col_name] > up_limit), col_name] = up_limit


# Drop outliers
def drop_outliers(dataframe, col_name, th1=0.05, th3=0.95):
    low_limit, up_limit = outlier_thresholds(dataframe, col_name, th1, th3)
    if low_limit > 0:
        dataframe = dataframe[dataframe[col_name] > low_limit]
        dataframe = dataframe[dataframe[col_name] < up_limit]
    else:
        dataframe = dataframe[dataframe[col_name] < up_limit]
    return dataframe


# Check & Replace Outliers
for col in df.columns:
    print(col,check_outlier(df, col))
    
for col in df.columns:
    replace_with_thresholds(df, col)

# Drop Outliers
a = drop_outliers(df,'Insulin',th1=0.05, th3=0.9)
