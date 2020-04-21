# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
df=pd.read_csv(r"C:\Users\aswin\Documents\ds_salary_proj\glassdoor_jobs.csv")
df
##salary parcing
##company name text only
df=df[df['Salary Estimate']!='-1']