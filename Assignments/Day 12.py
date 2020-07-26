# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 17:05:02 2020

@author: Akash M Khyadi
"""
import pandas as pd
ds=pd.read_csv("general_data.csv")
print(ds.head())

#Cleaning the data set.
#Removing null values
print(ds.isnull().sum())
cds=ds.dropna()
print(cds.head())

#Checking and removing duplicate values if available.
print(cds.duplicated().sum())
cds1=cds
#No Duplicates found.

#Based on the given current data in order to find attrition causing variables.
#Converting Attrition from categorical to binomial values
cds["Attrition"].replace(to_replace=("Yes","No"),value=(1,0),inplace=True)
print(cds.head())

#Processing wilcoxon test to check if a particular variable 
#H0= There is no significiant attrition in the company caused by the age of the employees and the distance from home.
#H1= There is significiant attrition in the company caused by the age of the employees and the distance from home.

from scipy.stats import wilcoxon
print("\n")
print(wilcoxon(cds.Age,cds.DistanceFromHome))
#Output: WilcoxonResult(statistic=2892.0, pvalue=0.0)

#Friedman test
from scipy.stats import friedmanchisquare
print("\n")
print(friedmanchisquare(cds.Age,cds.DistanceFromHome,cds.JobLevel))
#output: FriedmanchisquareResult(statistic=7478.114178094286, pvalue=0.0)

#Mann Whitney test
from scipy.stats import mannwhitneyu
print("\n")
print(mannwhitneyu(cds.JobLevel,cds.NumCompaniesWorked))

# Moving on to Krushkal Wallis Test
from scipy.stats import kruskal
print("\n")
print(kruskal(cds.TotalWorkingYears,cds.TrainingTimesLastYear,cds.YearsAtCompany,cds.YearsSinceLastPromotion))

#ChiSquare Test
from scipy.stats import chi2_contingency
print("\n")
chitab=pd.crosstab(cds1.Attrition,cds1.Gender)
print(chitab)

print(chi2_contingency(chitab))

#One Sample t test
from scipy.stats import ttest_1samp
print("\n")
print(ttest_1samp(cds.Age,37))

print("\n",cds['Age'].mean())

#Two Sample paired t-test
from scipy.stats import ttest_rel
print("\n")
print(ttest_rel(cds.Education,cds.JobLevel))

# #Two Sample Independent t-test
# ds1=pd.read_csv("Attrition.csv")
# print(ds1.head())

# from scipy.stats import ttest_rel
# print("\n")
# print(ttest_rel(ds1.Attrition0,ds1.Attrition1))
