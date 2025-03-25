# neural_threat_radar.py

import streamlit as st
import random
import time

def show_radar():
    st.subheader("📡 Neural Threat Radar – Real-Time Intrusion Feed")
    st.markdown("AI is actively scanning for adversarial anomalies...")

    radar_data = [
        "Node 72.98.45.1 – ⚠️ Suspicious entropy spike",
        "Node 198.77.21.9 – ✅ Cleared after rescan",
        "Node 123.33.55.3 – ⚠️ Port scanning activity",
        "Node 45.12.89.7 – 🟡 Timeout during threat analysis",
        "Node 99.11.22.1 – ✅ Safe"
    ]

    with st.spinner("🔍 Scanning neural net..."):
        time.sleep(1)

    for log in radar_data:
        st.markdown(f"🧠 {log}")
        time.sleep(0.4)
