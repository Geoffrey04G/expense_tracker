# app/main.py

import streamlit as st
import datetime
import hashlib

from app import auth, expense_manager, charts, features_page as features, sms_importer, export_data

st.set_page_config(page_title="Expenselytics", layout="wide")

# Apply CSS
with open("app/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Session state init
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.username = ""
    st.session_state.phone = ""

# Auth
if not st.session_state.logged_in:
    option = st.sidebar.radio("Authentication", ["Login", "Register"])
    if option == "Login":
        auth.login()
    else:
        auth.register()
    st.stop()

# ──────🌟 Top Title ──────
st.markdown("""
    <style>
        .title-container {
            margin-top: -90px;
            padding-top: 12px;
            padding-left: 20px;
        }
        .title-container h1 {
            font-size: 50px;
            color: #00ffee;
            margin-bottom:0;
            text-shadow: 0 0 10px #00ffee;
        }
        .title-container p {
            font-size: 20px;
            color: #cccccc;
            margin-top: 0;
            text-shadow: 0 0 6px #888;
        }
    </style>

    <div class='title-container'>
        <h1>Expenselytics</h1>
        <p>Track, Analyze & Conquer Your Costs</p>
    </div>
""", unsafe_allow_html=True)



# ──────📱 Sidebar Layout ──────
# Pad top of sidebar to align with top title
st.sidebar.markdown("""
    <div style='padding-top: -120px;'>
        <h3 style='margin-bottom: 8px; color: #00ffee;'>📱 Registered Number</h3>
    </div>
""", unsafe_allow_html=True)

st.sidebar.markdown(
    f"""
    <div style="background-color:#00ffaa; padding:10px 15px; border-radius:8px;
                font-size:16px; text-align:center; color:black; font-weight:bold;
                box-shadow: 0 0 12px 2px rgba(0,255,170,0.8);">
        {st.session_state.phone}
    </div>
    """,
    unsafe_allow_html=True
)

if st.sidebar.button("🚪 Logout", use_container_width=True):
    auth.logout()

st.sidebar.markdown("---")

# Tip of the day
tips = [
    "Track your small expenses — they add up!",
    "Set a monthly savings goal and stick to it.",
    "Avoid impulse purchases — wait 24 hours.",
    "Review your budget weekly.",
    "Try a no-spend challenge for 7 days.",
]
index = int(hashlib.sha256(str(datetime.date.today()).encode()).hexdigest(), 16) % len(tips)

st.sidebar.markdown("### 💡 Tip of the Day")
st.sidebar.markdown(f"""
    <div class="tip-card" style="padding: 10px 15px; background-color: #111927;
         border-radius: 8px; color: #eee; margin-bottom: 15px; box-shadow: 0 0 8px #00ffee;">
         {tips[index]}
    </div>
""", unsafe_allow_html=True)

# Navigation
st.sidebar.markdown("### 🔍 Navigate")
page = st.sidebar.radio("Select a page", ["📥 Add Expense", "📊 Reports", "💡 Features", "📩 Import SMS"])

# Export CSV button ONLY in sidebar
st.sidebar.markdown("---")
st.sidebar.markdown("### ⬇️ Export CSV")
export_data.export_user_data()

# ────── Routing ──────
if page == "📥 Add Expense":
    st.title("📥 Add & Manage Expenses")
    expense_manager.display_expense_ui()

elif page == "📊 Reports":
    st.title("📊 Expense Analytics")
    charts.display_charts()

elif page == "💡 Features":
    features.show_Features()

elif page == "📩 Import SMS":
    sms_importer.import_sms()
