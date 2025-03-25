# ui_components.py

import streamlit as st

def cyberpunk_theme():
    try:
        with open("assets/styles.css") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.warning("⚠️ Theme file not found.")

def navbar():
    st.markdown("""
    <div class="navbar" style='text-align: center; padding: 10px 0;'>
        <h1 style='color: cyan;'>🛰 NEURAL-SHIELD AI</h1>
        <p style='color: gray;'>Real-Time AI Malware Defense Command System</p>
    </div>
    """, unsafe_allow_html=True)
