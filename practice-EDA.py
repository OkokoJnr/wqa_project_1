#EXPLORATORY DATA ANALYSIS SECTION  
# This section is for exploratory data analysis (EDA) of the cleaned dataset.
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
# Load the cleaned dataset
df = pd.read_csv('cleaned_mexico_real_estate.csv')
# Display the first few rows of the DataFrame
print(df.info())