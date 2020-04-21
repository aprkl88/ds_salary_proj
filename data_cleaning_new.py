# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
df=pd.read_csv(r"C:/Users/aswin/Documents/ds_salary_proj/glassdoor_jobs.csv")
df


#SALARY PARCING
import pandas as pd
df=pd.read_csv(r"C:\Users\aswin\Documents\ds_salary_proj\glassdoor_jobs.csv")

df=df[df['Salary Estimate']!='-1']
df['salary'] = df['Salary Estimate'].apply(lambda x: x.split("(")[0])
df['salary']=df['salary'].apply(lambda x:x.replace('K','1000').replace('$'," "))

df['hourly']=df['salary'].apply(lambda x: 1 if 'per hour' in x.lower() else 0) 
df['employer']=df['salary'].apply(lambda x: 1 if 'employer provided salary' in x.lower() else 0)

df['hourly_salary']=df['salary'].apply(lambda x:x.lower().replace( 'per hour',' ' ).replace('employer provided salary',' ').replace(':',' ').replace('000',' '))

df["min_salary"]=df['hourly_salary'].apply(lambda x: int(x.split("-")[0]))
df["min_salary"]=df['hourly_salary'].apply(lambda x: x.split("-")[0])
df["min_salary"].dtype

##df["min_salary"]=df["min_salary"].astype(int)  ## another method to convert to int type

df["max_salary"]=df['hourly_salary'].apply(lambda x: int(x.split("-")[1]))

df["avg_salary"]=(df.min_salary+df.max_salary)/2

#COMPANY NAME TEXT ONLY

df["company_txt"]=df.apply(lambda x: x["Company Name"] if x['Rating'] <0 else x["Company Name"][:-3] ,axis=1 )

#STATE FIELD

df["state"] =df["Location"].apply(lambda x: x.split(",")[1])


df.state.value_counts()  ## counts the no: of present
df["same_state"] =df.apply (lambda x: 1 if x["Location"][1]==x["Headquarters"][1] else 0,axis=1)

#AGE OF COMPANY

df ["Age"] = df["Founded"].apply(lambda x: x if x<1 else 2020-x)

#PARSING OF JOB DESCRIPTION

#PYTHON
df["Python_jd"] =df["Job Description"].apply (lambda x: 1 if "python" in x.lower() else 0 )

#R STUDIO
df["R_jd"] =df["Job Description"].apply (lambda x: 1 if "r studio" in x.lower() or "r-studio" in x.lower() else 0 )
 
#SPARK
df["Spark_jd"] =df["Job Description"].apply (lambda x: 1 if "spark" in x.lower() else 0 )

#EXCEL
df["Excel_jd"] =df["Job Description"].apply (lambda x: 1 if "excel" in x.lower() else 0 )


df=df.drop(["Unnamed: 0"], axis=1)







