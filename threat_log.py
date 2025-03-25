# threat_log.py

import streamlit as st
import pandas as pd
import random
import time

def generate_logs():
    attacks = []
    countries = ["USA", "Russia", "India", "China", "Germany", "UK", "France"]
    types = ["Adversarial", "Obfuscated", "Zero-Day", "DDoS", "Ransomware"]
    for _ in range(10):
        attacks.append({
            "Time": time.strftime('%H:%M:%S'),
            "Origin": random.choice(countries),
            "Type": random.choice(types),
            "Severity": random.randint(1, 10),
            "Blocked": random.choice(["✅", "❌"])
        })
    return pd.DataFrame(attacks)

def show_threat_log():
    st.subheader("📜 AI Threat Feed – Attack History")
    st.markdown("Live history of malware activity and AI decisions.")

    logs = generate_logs()
    st.dataframe(logs, use_container_width=True)

    csv = logs.to_csv(index=False).encode('utf-8')
    st.download_button("⬇️ Export Log as CSV", csv, "threat_log.csv", "text/csv")
