# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 14:07:42 2021

@author: aishwary
"""

import os
os.chdir(r'G:\My Drive\2020\Coding\Stratified Sampling')
import pandas as pd
import numpy as np


####################################### Manual Sampling #####################################

# Kaggle Loan Default Prediction Data
data = pd.read_csv('train.csv')
data.dtypes
data['Gender'] = np.random.choice(['Male', 'Female'], size=len(data), p=[0.6, 0.4])

# Get Gender Distribution
# gender_dist = pd.DataFrame(data.groupby('Gender').agg({'Gender':'count'})).rename(
#     columns = {'Gender':'Gender Count'}).reset_index()
data['Gender'].value_counts(normalize = True)
data['Gender'].value_counts(normalize = False)


# Currently Gender Distribution is around 60-40, we want it to be 50-50
stratify_column_name = 'Gender'
stratify_values = ['Male','Female']
stratify_proportions = [0.5,0.5]

df_stratified = pd.DataFrame(columns = data.columns)

for i in range(len(stratify_values)):
    ratio_len = int(len(data)*stratify_proportions[i])
    df_filtered = data[data[stratify_column_name] == stratify_values[i]]
    df_temp = df_filtered.sample(n = ratio_len,replace = True)
    df_stratified = pd.concat([df_stratified,df_temp])
    
df_stratified['Gender'].value_counts()/len(data)


###################################### Stratified Sampling ################################

from sklearn.model_selection import train_test_split
X = data.loc[:,data.columns != 'Credit Default']
y = data.iloc[:,-2]
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.2,stratify = y)
np.sum(y_train)/len(y_train)
np.sum(y_test)/len(y_test)


