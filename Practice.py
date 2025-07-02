import pandas as pd
df1 = pd.read_csv('mexico-real-estate-1.csv')
df2 = pd.read_csv('mexico-real-estate-2.csv')
#Task1: Cleaning df1
# 1. Remove NaN values
df1.dropna(inplace=True)
# 2. Transform price_usd column: Remove "$" and "," and convert to float
df1["price_usd"] = (
    df1["price_usd"]
    .str.replace("$", "") #remove dollar sign
    .str.replace(",", "") #remove commas
    .astype(float)  #convert to float
    ) 


#Task 2: Clean df2
# 1. Remove NaN values
df2.dropna(inplace=True)

df2["price_usd"] = (df2["price_mxn"]/19).round(2) #convert price_mxn to price_usd

df2.drop(columns=["price_mxn"], inplace=True) #drop price_mxn column

print(df2.head())