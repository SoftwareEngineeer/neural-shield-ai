# global_threat_map.py

import streamlit as st
import pydeck as pdk
import pandas as pd
import random

def show_global_map():
    st.subheader("🌍 Global Threat Intelligence Map")
    st.write("Displaying real-time geolocated threat attempts across the globe.")

    data = pd.DataFrame({
        'lat': [random.uniform(-80, 80) for _ in range(20)],
        'lon': [random.uniform(-170, 170) for _ in range(20)],
        'severity': [random.randint(1, 5) for _ in range(20)]
    })

    st.pydeck_chart(pdk.Deck(
        map_style='mapbox://styles/mapbox/dark-v10',
        initial_view_state=pdk.ViewState(
            latitude=0,
            longitude=0,
            zoom=1
        ),
        layers=[
            pdk.Layer(
                "ScatterplotLayer",
                data=data,
                get_position='[lon, lat]',
                get_radius="severity * 30000",
                get_fill_color='[255, 0, 0, 160]',
                pickable=True
            )
        ],
    ))
