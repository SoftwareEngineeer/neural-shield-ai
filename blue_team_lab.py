# blue_team_lab.py

import streamlit as st

def show_blue_team_lab():
    st.subheader("🛡️ Blue Team Lab – AI Defense System")
    st.markdown("Welcome, Security Analyst. Monitor and improve AI-based malware detection strategies.")

    st.success("✅ No current attacks detected.")
    st.info("📊 AI Model Accuracy: 92.4%")
    st.warning("⚠️ Retrain recommended: Last model update was 14 days ago.")
    st.button("🔁 Retrain AI Model")
