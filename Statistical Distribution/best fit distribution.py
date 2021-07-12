import os
# os.chdir(r'G:\My Drive\2021\Check')
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

# ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness','Diabetes_beta', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age', 'Diabetes_alpha', 'Outcome']


# Plot histogram for each variable
fig, axes = plt.subplots(len(X.columns)//2, 2, figsize=(15, 15))
i = 0
for triaxis in axes:
    for axis in triaxis:
        X.hist(column = X.columns[i], bins = 100, ax=axis,normed=True)
        i = i+1

 
# Find probability distribution for each variable

dist_names = ['weibull_min','norm','weibull_max','beta','invgauss','uniform','gamma','expon','lognorm','pearson3','triang']

import scipy.stats as st

def get_best_distribution(data):
    dist_results = []
    params = {}
    for dist_name in dist_names:
        dist = getattr(st, dist_name)
        param = dist.fit(data)

        params[dist_name] = param
        # Applying the Kolmogorov-Smirnov test
        D, p = st.kstest(data, dist_name, args=param)
        print("p value for "+dist_name+" = "+str(p))
        dist_results.append((dist_name, p))

    # select the best fitted distribution
    best_dist, best_p = (max(dist_results, key=lambda item: item[1]))
    # store the name of the best fit and its p value

    print("Best fitting distribution: "+ str(best_dist))
    print("Best p value: "+ str(best_p))
    print("Parameters for the best fit: "+ str(params[best_dist]))
    return best_dist, best_p, params[best_dist]

  
get_best_distribution(df['Diabetes_alpha'])
