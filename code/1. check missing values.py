"""
Created on Thu Jun  1 10:02:15 2017

@author: scapk
"""
import pandas as pd
import glob

#file = 'mimic3/ADMISSIONS.csv'
def count_missing(file):
    df = pd.read_csv(file, header=0, sep=',', index_col=0)
    #counting missing values per columns
    print('Count of missing values per columns in '+ file +': ')
    print(df.isnull().sum())
    #row count
    print('Total row count in '+ file +': ')
    print(len(df))

for f in glob.glob('mimic3/*.csv'):
    count_missing(f)
