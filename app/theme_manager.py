import streamlit as st

def apply_theme(theme):
    if theme == "Light":
        st.markdown("""
            <style>
            body { background: #f0f0f0; color: #111111; }
            button, input, select, textarea {
                background: #ffffff;
                color: #000000;
                box-shadow: none;
            }
            .tip-card {
                background: #ffffff;
                color: #000000;
                border: 1px solid #aaa;
                box-shadow: none;
            }
            </style>
        """, unsafe_allow_html=True)
    else:
        # Keep robotic theme as default (already loaded in style.css)
        pass