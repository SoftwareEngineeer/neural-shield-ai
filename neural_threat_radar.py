# neural_threat_radar.py

import streamlit as st
import time
import random

def show_radar():
    st.subheader("📡 Neural Threat Radar – Real-Time Intrusion Feed")
    st.markdown("AI is scanning the neural grid for anomalies...")

    with st.spinner("Loading AI radar..."):
        time.sleep(1.5)

    for _ in range(5):
        st.markdown(f"🧠 Detected anomaly at node {random.randint(100,999)} - Status: {'⚠️ Breach Attempt' if random.random() > 0.4 else '✅ Safe'}")
