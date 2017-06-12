"""
Created on Thu Jun  1 10:02:15 2017

@author: scapk
"""
import pandas as pd

file = 'm3dq/adm.csv'
df = pd.read_csv(file, header=0, sep=';', index_col=0, parse_dates=True, encoding=None, tupleize_cols=False, infer_datetime_format=False)
#print summary
print('Summary of '+file+': ')
print(df.describe())
#counting missing values per columns
print('Count of missing values per columns in '+file+': ')
print(df.isnull().sum())
#row count
print('Total row count in '+file+': ')
print(len(df))
