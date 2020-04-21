# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 22:50:36 2020

@author: aswin
"""


import glassdoor_scraper as gs
import pandas as pd
from selenium import webdriver
##driver = webdriver.Chrome(r"C:/webdrivers/chromedriver")
path="C:/Users/aswin/Documents/ds_salary_proj/chromedriver"

df=gs.get_jobs('data_scientist',15,False,path,5)
