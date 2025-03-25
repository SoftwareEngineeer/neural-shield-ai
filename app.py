# app.py

import streamlit as st
from ui_components import cyberpunk_theme, navbar
from red_team_console import show_red_team_console
from blue_team_lab import show_blue_team_lab
from global_threat_map import show_global_map
from neural_threat_radar import show_radar
from threat_log import show_threat_log

st.set_page_config(layout="wide", page_title="NEURAL-SHIELD AI", page_icon="🛡️")

cyberpunk_theme()
navbar()

# Sidebar mode switch
mode = st.sidebar.radio("⚔️ Choose Your Role:", ["🌍 Live Map", "💀 Red Team Console", "🛡️ Blue Team Lab", "📡 AI Radar", "📜 Threat Feed"])

if mode == "🌍 Live Map":
    show_global_map()
elif mode == "💀 Red Team Console":
    show_red_team_console()
elif mode == "🛡️ Blue Team Lab":
    show_blue_team_lab()
elif mode == "📡 AI Radar":
    show_radar()
elif mode == "📜 Threat Feed":
    show_threat_log()
