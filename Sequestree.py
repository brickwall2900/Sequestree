#!/usr/bin/env python
# coding: utf-8

# In[2]:

import streamlit as st

st.title("Spatial Assessment and Backcasting of Tree Carbon Sequestration (CS) in Quezon City, Philippines")

choice = st.sidebar.selectbox(
    "Select map to display:",
    ["Tree Biomass and Carbon Stock of Quezon City, Philippines - Random Forest Predictions", "Tree Biomass and Carbon Stock of Quezon City, Philippines - Geographically Weighted Regression Predictions", 
     "Tree Carbon Sequestration Potential of Quezon City, Philippines - Random Forest Predictions", "Tree Carbon Sequestration Potential of Quezon City Philippines - Geographically Weighted Regression Predictions", 
     "Tree Biomass and Carbon Stock of Quezon City, Philippines Per Zone - Random Forest Predictions", "Tree Biomass and Carbon Stock of Quezon City, Philippines Per Zone - Geographically Weighted Regression Predictions",
     "Tree Carbon Sequestration Potential of Quezon City, Philippines Per Zone - Random Forest Predictions", "Tree Carbon Sequestration Potential of Quezon City, Philippines Per Zone - Geographically Weighted Regression Predictions"]
)

if choice == "Tree Biomass and Carbon Stock of Quezon City, Philippines - Random Forest Predictions":
    import visualization
elif choice == "Tree Biomass and Carbon Stock of Quezon City, Philippines - Geographically Weighted Regression Predictions":
    import visualization_copy
elif choice == "Tree Carbon Sequestration Potential of Quezon City, Philippines - Random Forest Predictions":
    import visualization_copy_copy
elif choice == "Tree Carbon Sequestration Potential of Quezon City Philippines - Geographically Weighted Regression Predictions":
    import visualization_copy_copy_copy
elif choice == "Tree Biomass and Carbon Stock of Quezon City, Philippines Per Zone - Random Forest Predictions":
    import zonal
elif choice == "Tree Biomass and Carbon Stock of Quezon City, Philippines Per Zone - Geographically Weighted Regression Predictions":
    import zonal_copy
elif choice == "Tree Carbon Sequestration Potential of Quezon City, Philippines Per Zone - Random Forest Predictions":
    import zonal_copy_copy
elif choice == "Tree Carbon Sequestration Potential of Quezon City, Philippines Per Zone - Geographically Weighted Regression Predictions":
    import zonal_copy_copy_copy