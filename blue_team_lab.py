# blue_team_lab.py

import streamlit as st
import pandas as pd
import plotly.express as px
from malware_ai_core import train_firewall_model, simulate_training_data

def show_blue_team_lab():
    st.subheader("🛡️ Blue Team AI Firewall Training Lab")

    st.markdown("🔬 Here you can retrain the AI firewall model using new data and improve its accuracy against mutated malware attacks.")

    if st.button("🚀 Retrain Firewall AI"):
        with st.spinner("Training AI firewall on new threat samples..."):
            accuracy, df = train_firewall_model()
        st.success(f"✅ AI Firewall Retrained — Accuracy: {accuracy:.2f}%")

        st.subheader("📈 Defense Accuracy Overview")
        fig = px.histogram(df, x="Label", color="Detected", barmode="group",
                           title="AI Defense Result After Training",
                           labels={"Label": "Actual Type", "Detected": "AI Prediction"})
        st.plotly_chart(fig, use_container_width=True)

        st.info("🧠 '1' = Malware, '0' = Safe | Blue = Correctly detected | Red = Missed")
    else:
        st.markdown("🧪 Click above to simulate real-time AI firewall training.")
