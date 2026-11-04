import numpy as np
import pandas as pd
df=pd.read_csv(r"C:\Users\acer\Downloads\Titanic (1).csv")
print(df.to_string())

df1=df[["Name","Age","Sex"]]
print(df1.to_string())

print(df1.head(20).to_string())

print(df1.iloc[10:25])

df2=df[["PassengerId","Pclass","Survived"]]
print(df2)

df3=df[["Name","Fare"]]
print(df3.head(10).to_string())
