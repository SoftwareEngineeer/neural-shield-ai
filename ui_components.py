# ui_components.py

import streamlit as st

def cyberpunk_theme():
    """Applies a custom cyberpunk theme from CSS file."""
    try:
        with open("assets/styles.css") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.warning("⚠️ Custom theme file not found. Using default Streamlit style.")

def navbar():
    """Displays the main app title and subtitle as a custom navbar."""
    st.markdown("""
    <div class="navbar" style='text-align: center; padding: 10px 0;'>
        <h1 style='color: cyan; font-family: monospace;'>🛰 NEURAL-SHIELD AI</h1>
        <p style='color: #AAA; font-size: 16px;'>Real-Time AI Malware Defense Command System</p>
    </div>
    """, unsafe_allow_html=True)
