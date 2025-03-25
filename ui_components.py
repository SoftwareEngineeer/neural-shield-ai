# ui_components.py

import streamlit as st

def cyberpunk_theme():
    with open("assets/styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def navbar():
    st.markdown("""
    <div class="navbar">
        <h1>🛰 NEURAL-SHIELD AI</h1>
        <p>Real-Time AI Malware Defense Command System</p>
    </div>
    """, unsafe_allow_html=True)
