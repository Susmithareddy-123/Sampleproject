import pandas as pd
import numpy as np
df=pd.read_csv(r"D:\\MyProject\\Sampleproject\\ds_salaries.csv")
#Checking the shape of the dataframe
df.shape
#checking dtypes of the dataframe
print(df.dtypes)
#Checking for null values in coluns
print(df.isnull().sum())
print(df.head())