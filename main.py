import pandas as pd
import numpy as np
df=pd.read_csv(r"D:\MyProject\matches.csv")
print(df.head())
print(df.info())
print(df.summary())
print(df.describe())
print(df.values())
print(df)