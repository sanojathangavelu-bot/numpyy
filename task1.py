#Task1
import pandas as pd
df=pd.read_csv(r"C:\Users\acer\Downloads\Titanic (1).csv")
print(df.head(10).to_string())
print(df.tail(5).to_string())
print(df.shape)
print(df.columns)
print(df.info)
print(df.describe())

