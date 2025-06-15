# app/export_data.py

import streamlit as st
import os

def export_user_data():
    username = st.session_state.username
    file_path = f"data/expenses/{username}.csv"
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            st.sidebar.download_button(  # 💡 NOTE: now rendered in sidebar only
                label="Download My Expenses CSV",
                data=f,
                file_name=f"{username}_expenses.csv",
                mime="text/csv"
            )
    else:
        st.sidebar.info("No expenses found to export.")
