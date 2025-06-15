# app/auth.py

import streamlit as st
import json
import hashlib
import os

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def load_users():
    if os.path.exists("data/users.json"):
        with open("data/users.json") as f:
            return json.load(f)
    return {}

def save_users(users):
    with open("data/users.json", "w") as f:
        json.dump(users, f, indent=4)

def register():
    st.markdown("""
        <h2 style='color:#00ffee; text-align:center; text-shadow:0 0 10px #00ffee;'>Welcome to Expenselytics 🚀</h2>
        <hr style='border: 1px solid #00ffee; box-shadow: 0 0 10px #00ffee; margin-top:10px; margin-bottom:20px;'>
    """, unsafe_allow_html=True)

    st.title("Register")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    phone = st.text_input("Phone Number (Required)")

    if st.button("Register"):
        if not phone.strip():
            st.error("Phone number is required.")
            return

        users = load_users()

        for user_data in users.values():
            if user_data["phone"] == phone:
                st.error("Phone number already registered.")
                return

        if username in users:
            st.error("Username already exists!")
        else:
            users[username] = {
                "password": hash_password(password),
                "phone": phone
            }
            save_users(users)
            st.success("Registered successfully! Please login.")


def login():
    st.markdown("""
        <h2 style='color:#00ffee; text-align:center; text-shadow:0 0 10px #00ffee;'>Welcome Back to Expenselytics 👋</h2>
        <hr style='border: 1px solid #00ffee; box-shadow: 0 0 10px #00ffee; margin-top:10px; margin-bottom:20px;'>
    """, unsafe_allow_html=True
     
    )

    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        users = load_users()
        if username in users and users[username]["password"] == hash_password(password):
            st.session_state.logged_in = True
            st.session_state.username = username
            st.session_state.phone = users[username]["phone"]
            st.success("Login successful.")
            st.rerun()
        else:
            st.error("Invalid username or password")


def logout():
    st.session_state.logged_in = False
    st.session_state.username = ""
    st.session_state.phone = ""
    st.success("Logged out successfully.")
    st.rerun()

def show_user_info():
    users = load_users()
    phone = users.get(st.session_state.username, {}).get("phone", "N/A")
    st.sidebar.markdown(f"📱 Phone: `{phone}`")
