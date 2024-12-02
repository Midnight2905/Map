import geopandas as gpd
import folium
import mapclassify
from matplotlib import pyplot as plt

# Load
file = gpd.read_file(r'ComArea_ACS14_f.shp')

# Display rows
print(file.head())

# Creates map
m = file.explore('Property_C')

# Saves the map as an html
m.save("map.html")
