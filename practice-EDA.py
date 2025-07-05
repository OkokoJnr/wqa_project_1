#EXPLORATORY DATA ANALYSIS SECTION  
# This section is for exploratory data analysis (EDA) of the cleaned dataset.
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.io as pio

# Recommended setting
pio.renderers.default = "browser"
# Load the cleaned dataset
df = pd.read_csv('cleaned_mexico_real_estate.csv')

#Task 1: Using Scatter Mapbox plot
# fig = px.scatter_map(
#     df,
#     lat='lat',
#     lon='lon',
#     center={"lat":19.43, "lon":-99.13},  # Center on Mexico City
#     width=1000,
#     height=800,
#     hover_data=['price_usd', 'state'],
# )
#Add mapbox style to figure layout
#fig.update_layout(mapbox_style="carto-positron")
# fig.update_layout(
#     mapbox_style="open-street-map",  # Use OpenStreetMap style
#     mapbox_zoom=5,  # Set zoom level
#     mapbox_center={"lat": 19.43, "lon": -99.13}  # Center on Mexico City
    
# )
# # Show the plot
# fig.show()
# # Save the figure as an image
# fig.write_image("images/mexico_map.png")

#Summary statistics of the dataset
#sumStat = df[["area_m2", "price_usd"]].describe()


#determine the 10 most prevalent states in our dataset.
top10 = df["state"].value_counts().head(10)

plt.figure(figsize=(8, 8))
# Visualize the top 10 states by count using a bar chart
'''
plt.bar(top10.index, top10.values, color='skyblue')
plt.xlabel('State')
plt.ylabel('Count')
plt.title('Top 10 States by Count in Mexico Real Estate Dataset')
plt.savefig("images/topstates.png", dpi=300)  # Save at 300 DPI
'''

#-----------------------------------------------------------------------------
#Task 3: Create a histogram of "area_m2"
# plt.hist(df["area_m2"],  color='lightblue', edgecolor='black')
# plt.xlabel("Area [sq meters]")
# plt.ylabel("Frequency") 
# plt.title("Distribution of Home Sizes")
# plt.savefig("images/area_distribution.png", dpi=300)  # Save at 300 DPI

#-----------------------------------------------------------------------------
#Task 4: Create a horizontal boxplot of "area_m2"
# plt.boxplot(df["area_m2"], vert=False)
# plt.xlabel("Area [sq meters]")
# plt.title("Distribution of Home Sizes") 
# plt.savefig("images/area_boxplot.png", dpi=300)  # Save at 300 DPI


#-----------------------------------------------------------------------------
#Task5: Create a histogram and boxplot of "price_usd"
# plt.hist(df["price_usd"], color='lightblue', edgecolor='black'
#          )
# plt.xlabel("Price [USD]")
# plt.ylabel("Frequency")
# plt.title("Distribution of Home Prices")
# plt.savefig("images/price_distribution.png", dpi=300)  # Save at 300

# Create a horizontal boxplot of "price_usd"
# plt.boxplot(df["price_usd"], vert=False)
# plt.xlabel("Price [USD]")
# plt.title("Distribution of Home Prices")
# plt.savefig("images/price_boxplot.png", dpi=300)  # Save at 300 DPI

#-----------------------------------------------------------------------------
#Groupby State
mean_price_by_state = df.groupby("state")["price_usd"].mean().sort_values(ascending=True)
# Create a horizontal bar chart of average home prices by state using Matplotlib
plt.barh(mean_price_by_state.index, mean_price_by_state.values, color='skyblue')
# plt.xlabel('State')
# plt.ylabel('Average Price (USD)')
# plt.title('Average Home Price by State in Mexico')
# # Save the figure as an image
# plt.savefig("images/average_price_by_state_m.png", dpi=300)  # Save at 300 DPI


# Create a horizontal bar chart of average home prices by state using pandas
mean_price_by_state.head(10).plot(kind='barh', color='skyblue', ylabel='State', title='Average Home Price by State in Mexico',xlabel='Average Price [USD]', figsize=(10, 8))
# Save the figure as an image
plt.savefig("images/average_price_by_state_p.png", dpi=300)  # Save at 300 DPI



#show the plot
plt.show()

# Display the first few rows of the DataFrame
#print(df.head())  