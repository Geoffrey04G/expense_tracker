
import streamlit as st
import datetime
import hashlib

# ✅ FIRST: set page config before anything else
st.set_page_config(page_title="Robotic Expense Tracker", layout="wide")


st.markdown("""
<style>
/* Remove link icon from headers */
h1 a, h2 a, h3 a, h4 a, h5 a, h6 a {
    text-decoration: none !important;
    pointer-events: none !important;
    color: inherit !important;
}

/* Sidebar text sizing and styling */
.css-1d391kg, .css-1v0mbdj, .css-16idsys {
    font-size: 20px !important;
}

<style>
/* Increase sidebar radio label size */
[data-testid="stSidebar"] .stRadio label {
    font-size: 20px !important;
    font-weight: 600 !important;
    color: #00ffee !important;
}
</style>
""", unsafe_allow_html=True)


# ✅ THEN: import modules that might use Streamlit
import expense_manager
import charts
import features_page as features
import theme_manager

# ✅ Apply CSS
st.markdown('<style>' + open('app/style.css').read() + '</style>', unsafe_allow_html=True)

st.markdown("""
    <style>
    /* Hide the default toggle label */
    .stToggle > div > label > div[data-testid="stMarkdownContainer"] {
        display: none;
    }
    /* Custom toggle switch styling */
    .stToggle > div > label {
        display: inline-block;
        position: relative;
        width: 60px;
        height: 30px;
        background-color: #333;
        border-radius: 30px;
        cursor: pointer;
        transition: background-color 0.3s;
    }
    .stToggle > div > label::after {
        content: '';
        position: absolute;
        width: 26px;
        height: 26px;
        background-color: #00ffee;
        top: 2px;
        left: 2px;
        border-radius: 50%;
        transition: transform 0.3s;
    }
    .stToggle input:checked + label {
        background-color: #ff00ff;
    }
    .stToggle input:checked + label::after {
        transform: translateX(30px);
    }
    </style>
""", unsafe_allow_html=True)

# Daily tips list
daily_tips = [
    "Track your small expenses — they add up!",
    "Set a monthly savings goal and stick to it.",
    "Review your budget weekly to stay on track.",
    "Avoid impulse purchases — take 24 hours before buying.",
    "Use color-coded categories for clear visual tracking.",
    "Limit your daily spending with a wallet budget.",
    "Categorize everything to see where you can cut back.",
    "Automate savings to build wealth passively.",
    "Review subscriptions monthly — cancel unused ones.",
    "Always keep an emergency fund ready!"
]

# Determine today's tip based on date
today = datetime.date.today().isoformat()
index = int(hashlib.sha256(today.encode()).hexdigest(), 16) % len(daily_tips)
today_tip = daily_tips[index]

with st.sidebar:
    st.markdown(f"""
        <div style='
            background: rgba(0,0,20,0.7);
            border: 1px solid #00ffee;
            padding: 15px;
            border-radius: 15px;
            box-shadow: 0 0 15px #00ffee;
            font-size: 14px;
            margin-bottom: 20px;
        '>
        <b>Hi!! Today's tip 💡</b><br>
        {today_tip}
        </div>
    """, unsafe_allow_html=True)


# 🌗 Theme toggle (Light/Dark)
if "theme" not in st.session_state:
    st.session_state.theme = "Dark"

with st.sidebar:
    toggle_state = st.toggle("Theme", key="theme_toggle_switch")

if toggle_state and st.session_state.theme != "Light":
    st.session_state.theme = "Light"
    st.rerun()
elif not toggle_state and st.session_state.theme != "Dark":
    st.session_state.theme = "Dark"
    st.rerun()

# Apply the theme
theme_manager.apply_theme(st.session_state.theme)



page = st.sidebar.radio(
    "Navigate", 
    ["📥 Add Expense", "📊 Reports", "💡 Features"],
    label_visibility="collapsed"
)
if page == "📥 Add Expense":
    st.markdown("<h1 style='color: #00ffee; text-shadow: 0 0 15px #00ffee;'>🤖 Robo Expense</h1>", unsafe_allow_html=True)
    st.title("📥 Add & Manage Expenses")
    expense_manager.display_expense_ui()

elif page == "📊 Reports":
    st.title("📊 Expense Analytics")
    charts.display_charts()

elif page == "💡 Features":
    features.show_Features()
