#!/usr/bin/env python
# coding: utf-8

# In[2]:

import streamlit as st
import leafmap.foliumap as leafmap
import folium
from branca.colormap import linear
from leafmap.foliumap import SplitControl

st.set_page_config(layout="wide")
st.title("Tree Biomass and Carbon Stock of Quezon City, Philippines - Random Forest Predictions")

biomass_rasters = {
    "2020": "2020_AGB_RF.tif",
    "2021": "2021_AGB_RF.tif",
    "2022": "2022_AGB_RF.tif",
    "2023": "2023_AGB_RF.tif",
    "2024": "2024_AGB_RF.tif",
}

col1, col2 = st.columns(2)
with col1:
    left_year = st.selectbox("Left Map (Year)", list(biomass_rasters.keys()), index=0)
with col2:
    right_year = st.selectbox("Right Map (Year)", list(biomass_rasters.keys()), index=len(biomass_rasters)-1)

m = leafmap.Map(center=[14.65, 121.05], zoom=12, basemap=None)

white_tiles = folium.raster_layers.TileLayer(
    tiles="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/wcAAgEBAXV3kPAAAAAASUVORK5CYII=",
    name="White Background",
    attr="Blank",
    overlay=False,
    control=False
)
white_tiles.add_to(m)

m.split_map(
    left_layer=biomass_rasters[left_year],
    right_layer=biomass_rasters[right_year],
    left_args={'palette': 'Greens', 'vmin': 0, 'vmax': 2500},
    right_args={'palette': 'Greens', 'vmin': 0, 'vmax': 2500},
)
colormap = linear.Greens_09.scale(0, 2000)
colormap.caption = "Aboveground Biomass (kg)"
green_palette = colormap.colors  

m.add_colorbar(colors=colormap.colors, vmin=0, vmax=2500, caption="Aboveground Biomass (kg)")

m.to_streamlit(height=600)

