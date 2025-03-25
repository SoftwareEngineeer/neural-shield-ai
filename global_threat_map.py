# global_threat_map.py

import streamlit as st
import pandas as pd
import random
import time
import pydeck as pdk

def generate_fake_attack():
    countries = {
        "USA": [37.0902, -95.7129],
        "Russia": [61.5240, 105.3188],
        "China": [35.8617, 104.1954],
        "India": [20.5937, 78.9629],
        "Brazil": [-14.2350, -51.9253],
        "Germany": [51.1657, 10.4515],
        "UK": [55.3781, -3.4360],
        "South Korea": [35.9078, 127.7669],
        "Vietnam": [14.0583, 108.2772],
        "France": [46.6034, 1.8883]
    }
    country = random.choice(list(countries.keys()))
    lat, lon = countries[country]
    severity = random.randint(1, 10)
    blocked = random.choice([True, False])
    return {
        "Country": country,
        "Lat": lat,
        "Lon": lon,
        "Severity": severity,
        "Blocked": blocked
    }

def show_global_map():
    st.subheader("🌍 Live Global Malware Threat Map")
    st.markdown("Visualizing AI-detected malware attacks around the world in real-time.")

    data = [generate_fake_attack() for _ in range(20)]
    df = pd.DataFrame(data)

    st.pydeck_chart(pdk.Deck(
        map_style='mapbox://styles/mapbox/dark-v10',
        initial_view_state=pdk.ViewState(
            latitude=20,
            longitude=0,
            zoom=1.2,
            pitch=45,
        ),
        layers=[
            pdk.Layer(
                'ScatterplotLayer',
                data=df,
                get_position='[Lon, Lat]',
                get_color='[255, 50, 50]' if not df["Blocked"].any() else '[50, 255, 50]',
                get_radius='Severity * 10000',
                pickable=True,
                opacity=0.9
            )
        ],
        tooltip={"text": "📍 {Country}\nSeverity: {Severity}/10\nBlocked: {Blocked}"}
    ))

    st.markdown("🕒 Refresh or switch pages to regenerate global threats.")
