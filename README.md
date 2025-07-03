# wqa_project_1

PROJECT 1 - MEXICO HOUSING PROJECT

In this project, I'll work with a dataset with 21,000 properties for sale in Mexico through the real estate website Properati.com. My goal is to determine whether sale prices are influenced more by property size or location.

Some of the things I'll learn in this project are:

How to organize information using basic Python data structures.

How to import data from CSV files and clean it using the pandas library.

How to create data visualizations like scatter and box plots.

How to examine the relationship between two variables using correlation.

The project consists of four lessons and one assignment. I'll work through the lessons following WordQuant Instructor  code-along videos.

Each of the following tasks were carried out:

Task 1: Clean df1 by dropping rows with NaN values. Then remove the "$" and "," characters from "price_usd" and recast the values in the column as floats.

Task 2: First, drop rows with NaN values in df2. Next, use the "price_mxn" column to create a new column named "price_usd". (Keep in mind that, when this data was collected in 2014, a dollar cost 19 pesos.) Finally, drop the "price_mxn" from the DataFrame.

Task 3: Drop rows with NaN values in df3. Then use the split method to create two new columns from "lat-lon" named "lat" and "lon", respectively.

Task 4: Use the split method again, this time to extract the state for every house. (Note that the state name always appears after "México|" in each string.) Use this information to create a "state" column. Finally, drop the "place_with_parent_names" and "lat-lon" columns from the DataFrame.

Task 5: Concatenate df1, df2, df3 as new DataFrame named df and then save it as a CSV file