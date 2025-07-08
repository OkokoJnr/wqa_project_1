import pandas as pd
df1 = pd.read_csv('data/mexico-real-estate-1.csv')
df2 = pd.read_csv('data/mexico-real-estate-2.csv')
df3 = pd.read_csv('data/mexico-real-estate-3.csv')

#Task1: Cleaning df1
# 1. Remove NaN values
df1.dropna(inplace=True)
# 2. Transform price_usd column: Remove "$" and "," and convert to float
df1["price_usd"] = (
    df1["price_usd"]
    .str.replace("$", "", regex=False) #remove dollar sign
    .str.replace(",", "", regex=False) #remove commas
    .astype(float)  #convert to float
    ) 


#Task 2: Clean df2
# 1. Remove NaN values
df2.dropna(inplace=True)

df2["price_usd"] = (df2["price_mxn"]/19).round(2) #convert price_mxn to price_usd

df2.drop(columns=["price_mxn"], inplace=True) #drop price_mxn column

# Task 3: Clean df3
df3.dropna(inplace=True)  # Remove NaN values

df3[["lat", "lon"]] = df3["lat-lon"].str.split(",", expand=True).astype(float) # Split lat-lon into two columns
df3.drop(columns=["lat-lon"], inplace=True)  # Drop the original lat-lon column

df3["state"] = df3["place_with_parent_names"].str.split("|", expand=True)[2]  # Extract state from place_with_parent_names

df3.drop(columns=["place_with_parent_names"], inplace=True)  # Drop place_with_parent_names column

df = pd.concat([df1, df2, df3], ignore_index=True)  # Concatenate df1, df2, df3 into a new DataFrame
df.to_csv('data/cleaned_mexico_real_estate.csv', index=False)  # save the new DataFrame as a CSV file
print(df.head())  