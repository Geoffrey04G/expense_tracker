# app/features_page.py

import streamlit as st

def show_Features():
    st.markdown("""
        <h1 style='text-align: center; color: #00ffee; text-shadow: 0 0 15px #00ffee;'>💡 Robo-Saving Features</h1>
        <div class='features-grid'>
            <div class='feature-box'><div class='feature-title'>🧾 Expense Management</div><div class='feature-desc'>Track expenses with beautiful interface.</div></div>
            <div class='feature-box'><div class='feature-title'>📊 Visual Reports</div><div class='feature-desc'>Bar and pie charts to analyze your spending.</div></div>
            <div class='feature-box'><div class='feature-title'>📱 SMS Import</div><div class='feature-desc'>Upload SMS logs and extract spend data instantly.</div></div>
        </div>
        <style>
            .features-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
                gap: 25px;
                padding: 40px;
                max-width: 950px;
                margin: 0 auto;
            }
            .feature-box {
                background-color: #0d0d1a;
                border-radius: 20px;
                padding: 25px;
                box-shadow: 0 0 12px #00ffee;
                border: 1px solid #00ffee40;
            }
            .feature-title {
                font-size: 22px;
                font-weight: bold;
                color: #00ffee;
                margin-bottom: 10px;
                text-shadow: 0 0 5px #00ffee;
            }
            .feature-desc {
                font-size: 15px;
                color: #cccccc;
                line-height: 1.6;
            }
        </style>
    """, unsafe_allow_html=True)
