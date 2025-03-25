# global_threat_map.py

import streamlit as st
import pydeck as pdk
import pandas as pd
import random

def show_global_map():
    st.subheader("🌍 Global Threat Intelligence Map")
    st.write("Visualizing real-time AI-analyzed malware attack origins.")

    data = pd.DataFrame({
        'lat': [random.uniform(-90, 90) for _ in range(10)],
        'lon': [random.uniform(-180, 180) for _ in range(10)]
    })

    st.pydeck_chart(pdk.Deck(
        map_style='mapbox://styles/mapbox/dark-v10',
        initial_view_state=pdk.ViewState(latitude=0, longitude=0, zoom=1),
        layers=[pdk.Layer('ScatterplotLayer', data=data,
                          get_position='[lon, lat]',
                          get_color='[255, 0, 0, 160]',
                          get_radius=40000)]
    ))
