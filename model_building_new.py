# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 13:58:40 2020

@author: aswin
"""

import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 

df = pd.read_csv(r'C:\Users\aswin\Documents\ds_salary_proj\eda_data.csv')

# choose relevant columns 
df_model = df[['avg_salary','Rating','Size','Type of ownership','Industry','Sector','Revenue','num_comp','hourly','employer_provided',
             'job_state','same_state','age','python_yn','spark','aws','excel','job_simp','seniority','desc_len']]


# get dummy data 
df_dum = pd.get_dummies(df_model)

# train test split 
from sklearn.model_selection import train_test_split

X=df_dum.drop("avg_salary",axis=1)
y = df_dum[["avg_salary"]]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# multiple linear regression 

import statsmodels.api as sm

X_sm = X = sm.add_constant(X)
model = sm.OLS(y,X_sm)
model.fit().summary()

from sklearn.linear_model import LinearRegression, Lasso

from sklearn.model_selection import cross_val_score
lm=LinearRegression()
lm.fit(X_train,y_train)
np.mean(cross_val_score(lm,X_train,y_train,cv=3 ,scoring= "neg_mean_absolute_error")) ## shows deviation of example20,000 dollars from mean

lm_1=Lasso( )
np.mean(cross_val_score(lm_1,X_train,y_train,cv=3 ,scoring= "neg_mean_absolute_error"))

alpha=[]
error=[]

for i in range (1 , 100):
    alpha.append(i/100)
    lm_1=Lasso(alpha=i/100)
    error.append(np.mean(cross_val_score(lm_1,X_train,y_train,cv=3 ,scoring= "neg_mean_absolute_error")))

print(error)
plt.plot(alpha,error)

## err = tuple(zip(alpha,error)) ## creation of data frame using zip
err={"alpha":alpha, "error":error}

df_err=pd.DataFrame(err)

df_err[df_err.error == max(df_err.error)]
df_err.loc[df_err.error==max(df_err.error)]
