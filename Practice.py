import pandas as pd
df1 = pd.read_csv('mexico-real-estate-1.csv')
df2 = pd.read_csv('mexico-real-estate-2.csv')
#Cleaning df1
# 1. Remove NaN values
df1.dropna(inplace=True)
# 2. Transform price_usd column: Remove "$" and "," and convert to float

df1["price_usd"] = (
    df1["price_usd"]
    .str.replace("$", "") #remove dollar sign
    .str.replace(",", "") #remove commas
    .astype(float)) #convert to float

print(df1["price_usd"])
print(df1.info())
