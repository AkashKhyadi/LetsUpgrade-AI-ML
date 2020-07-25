# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 23:22:18 2020

@author: Akash M Khyadi
"""
import pandas as pd
data=pd.read_csv("general_data.csv")

nonull=data.isnull()
print(nonull)

dupe=data.duplicated().any()
print(dupe)

#Since there were no duplicate values just removed null rows using dropna function.
cleandata=data.dropna()
print(cleandata)

print(cleandata.info())

#Converting categorical values into numerical
cleandata["Attrition"].replace(to_replace=("Yes","No"),value=(1,0),inplace=True)

print(cleandata.info())

from scipy.stats import pearsonr
import matplotlib.pyplot as plt

print(pearsonr(cleandata.Attrition,cleandata.Age))
#print(stats,p)

#Used single line of code to plot data between attrition and other vaariables.
plt.scatter(cleandata.Attrition,cleandata.YearsWithCurrManager)

# Following code provides the correlation between all the variables in the dataset.
correlationmat=cleandata.corr()



