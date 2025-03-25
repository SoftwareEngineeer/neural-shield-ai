# threat_log.py

import streamlit as st
import random
import time

def show_threat_log():
    st.subheader("📜 Threat Intelligence Feed – Log Stream")
    st.write("Live updates from AI’s anomaly detection logs:")

    logs = [
        "ALERT: Suspicious .zip file blocked – Vietnam node",
        "FIREWALL: Adversarial packet dropped at gateway",
        "SCAN: No threat detected from external IP 192.168.88.1",
        "INTRUSION: Possible Trojan.exe mutation attempt detected",
        "ALERT: AI Core auto-updated with new weights"
    ]

    for log in logs:
        st.markdown(f"🟢 {log}")
        time.sleep(0.3)
