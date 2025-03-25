# neural_threat_radar.py

import streamlit as st
import plotly.graph_objects as go
import random
import time

def show_radar():
    st.subheader("📡 AI Threat Radar – Neural Confidence Scanner")
    st.markdown("Visualizing how the AI evaluates different threat categories in real-time.")

    # Simulate AI confidence scores
    labels = ["Known Malware", "Adversarial Malware", "Obfuscated Malware", "Benign Files", "Zero-Day Threats"]
    scores = [random.uniform(70, 100), random.uniform(30, 90), random.uniform(50, 85), random.uniform(80, 100), random.uniform(20, 60)]

    fig = go.Figure(data=go.Scatterpolar(
        r=scores,
        theta=labels,
        fill='toself',
        line=dict(color='lime'),
        marker=dict(size=6),
        name="AI Confidence %"
    ))

    fig.update_layout(
        polar=dict(
            bgcolor="#0a0a1a",
            radialaxis=dict(
                visible=True,
                range=[0, 100],
                showline=True,
                linewidth=2,
                linecolor='cyan',
                gridcolor='gray'
            ),
            angularaxis=dict(
                linecolor='cyan',
                linewidth=2,
                tickfont=dict(color='white')
            )
        ),
        showlegend=False,
        paper_bgcolor="#0f0f1a",
        font=dict(color="white"),
        title="🧠 Neural Radar: Confidence by Threat Category"
    )

    st.plotly_chart(fig, use_container_width=True)
    st.caption("Radar shows how confident the AI is across different malware types.")
