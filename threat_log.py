# threat_log.py

import streamlit as st
import time
import random

def show_threat_log():
    st.subheader("📜 Threat Intelligence Log – Activity Feed")
    st.write("Streaming live threat detection updates from the AI firewall:")

    log_entries = [
        "🚨 [02:13:54] Trojan.exe attempt detected – Quarantined",
        "🟢 [02:14:07] No threat from 192.168.1.44",
        "⚠️ [02:14:23] Executable with suspicious signature blocked",
        "🟢 [02:14:42] Normal traffic – UDP port 53",
        "🚨 [02:15:01] ZIP bomb pattern identified – Dropped",
        "🛑 [02:15:20] AI Core under overload – mitigation in progress"
    ]

    for log in log_entries:
        st.markdown(log)
        time.sleep(0.5)
