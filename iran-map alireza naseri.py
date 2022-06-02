#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import folium
import pandas as pd
from folium.plugins import HeatMap


iran_map = folium.Map(location=[32.4279, 53.6880], zoom_start=5)


# In[ ]:


ubaar= pd.read_csv("train.csv")
sample_ubaar = ubaar.head(1000)

for lat, lng in zip(sample_ubaar.sourceLatitude,sample_ubaar.sourceLongitude):
    folium.CircleMarker(
        [lat,lng],
        radius=2,
        color='red',
        fill=True,
        fill_color='darkred',
        fill_opacity=0.5
    ).add_to(iran_map)


# In[ ]:


for lat,lng in zip(sample_ubaar.destinationLatitude,sample_ubaar.destinationLongitude) :
    folium.CircleMarker(
        [lat,lng],
        radius=2,
        color='blue',
        fill=True,
        fill_color='blue',
        fill_opacity=0.3
    ).add_to(iran_map)

iran_map


# In[ ]:


new_iranmap = folium.Map(location=[32.4279,53.6880],zoom_start = 5)


# In[ ]:


for row in range(sample_ubaar.shape[0]):

    radius = (sample_ubaar.iloc[row,:]['price'] - sample_ubaar.iloc[row,:]['price'].min())/ sample_ubaar.iloc[row,:]['price'].max()

    folium.CircleMarker(
    location=[sample_ubaar.iloc[row,:]['sourceLatitude'], sample_ubaar.iloc[row,:]['sourceLongitude']],
    radius=radius,
    color='red',
    fill=True,
    fill_color='darkred',
    fill_opacity = 0.7
    ).add_to(new_iranmap)


# In[ ]:


for row in range(sample_ubaar.shape[0]):

    radius = (sample_ubaar.iloc[row,:]['price'] - sample_ubaar.iloc[row,:]['price'].min())/ sample_ubaar.iloc[row,:]['price'].max()

    folium.CircleMarker(
    location=[sample_ubaar.iloc[row,:]['destinationLatitude'], sample_ubaar.iloc[row,:]['destinationLongitude']],
    radius=radius,
    color='blue',
    fill=True,
    fill_color='blue',
    fill_opacity = 0.1
    ).add_to(new_iranmap)
new_iranmap


# In[ ]:


iran_heat_map = folium.Map(location = [32.4279,53.6880],zoom_start = 5)

ubaar['price_normalized'] = (ubaar['price'] - ubaar['price'].min())/ ubaar['price'].max()
HeatMap(
data=list(zip(ubaar.head(20000)['sourceLatitude'],
ubaar.head(20000)['sourceLongitude'],
ubaar.head(20000)['price_normalized'])
) ,
radius = 12
).add_to(iran_heat_map)
iran_heat_map

