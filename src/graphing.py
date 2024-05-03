import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Horizontal Bar Charts

def horizontal_charts(grouped_df, col_1, col_2, graph_title, x_label, y_label, colors_lst):
    grouped_df.sort_values(by=col_1, ascending=False)
    top_values = grouped_df.iloc[:16]

    plt.figure(figsize=(16, 12))
    plt.barh(top_values[col_2], top_values[col_1], color=colors_lst)

    # Add labels and title
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(graph_title, fontsize=16, fontweight='bold')

    plt.yticks(fontsize=20)
    plt.xticks(fontsize=15)
    # plt.xticks(rotation=90)
    plt.show()

#Line Charts Over Time

def line_plot(df, col_1, col_2, graph_title, x_label, y_label):
    plt.plot(df[col_1], df[col_2], marker='o', color='steelblue', linestyle='-')

    # Add labels and title
    plt.title(graph_title, fontsize=16, fontweight='bold')
    plt.xlabel(x_label, fontsize=14)
    plt.ylabel(y_label, fontsize=14)
    plt.xticks(rotation=45)
    plt.grid(True, linestyle='--', alpha=0.7)
    # Show plot
    plt.grid(True)
    plt.show()

#Heat Map Over Time

import folium
import folium.plugins as plugins
import geopandas as gpd
from folium import Choropleth, Circle, Marker
from folium.plugins import HeatMap, MarkerCluster, HeatMapWithTime

def generate_heatmap_with_time(dataframe, save_path):
    # Filter out rows with missing latitude or longitude values
    geo_data = dataframe.dropna(subset=['Latitude', 'Longitude'])
    # Group data by year and count the number of attacks in each location
    geo_data_grouped = geo_data.groupby(['Date (Year)', 'Latitude', 'Longitude']).size().reset_index(name='fatalities')
    # Create a base map centered around the mean latitude and longitude
    base_map = folium.Map(location=[geo_data_grouped['Latitude'].mean(), geo_data_grouped['Longitude'].mean()], zoom_start=2)
    # Create a list of lists containing location data and attack count for each year
    heat_data = [[[row['Latitude'], row['Longitude'], row['fatalities']] for index, row in geo_data_grouped[geo_data_grouped['Date (Year)'] == year].iterrows()] for year in sorted(geo_data_grouped['iyear'].unique())]
    # Create HeatMapWithTime layer
    HeatMapWithTime(heat_data, radius=15).add_to(base_map)
    # Display the map
    base_map.save(save_path)

#Histogram

def histogram(df, col_1, col_2, graph_title, x_label, y_label):
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df, x=col_1, bins=50, color='steelblue', kde=True)
    plt.title(graph_title, fontsize=16, fontweight='bold')
    plt.xlabel(x_label, fontsize=14)
    plt.ylabel(y_label, fontsize=14)
    plt.show()



