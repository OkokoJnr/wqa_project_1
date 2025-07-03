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
fig = px.scatter_map(
    df,
    lat='lat',
    lon='lon',
    center={"lat":19.43, "lon":-99.13},  # Center on Mexico City
    width=1000,
    height=800,
    hover_data=['price_usd', 'state'],
)
#Add mapbox style to figure layout
#fig.update_layout(mapbox_style="carto-positron")
fig.update_layout(
    mapbox_style="open-street-map",  # Use OpenStreetMap style
    mapbox_zoom=5,  # Set zoom level
    mapbox_center={"lat": 19.43, "lon": -99.13}  # Center on Mexico City
    
)
# Show the plot
fig.show()
# Save the figure as an image
fig.write_image("images/mexico_map.png")

# Display the first few rows of the DataFrame
print(df.info())