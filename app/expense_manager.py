import time
import streamlit as st
import pandas as pd
import os
from datetime import datetime

DATA_PATH = "data/expenses/sampleuser.csv"

# Initialize CSV if it doesn't exist
def init_csv():
    if not os.path.exists(DATA_PATH):
        os.makedirs(os.path.dirname(DATA_PATH), exist_ok=True)
        df = pd.DataFrame(columns=["Date", "Category", "Amount", "Note"])
        df.to_csv(DATA_PATH, index=False)

def load_expenses():
    init_csv()
    return pd.read_csv(DATA_PATH)

def save_expenses(df):
    df.to_csv(DATA_PATH, index=False)

def display_expense_ui():
    st.subheader("➕ Add a New Expense")

    # 🌐 Glowing Glass Form
    with st.form("add_expense_form", clear_on_submit=True):
        col1, col2, col3 = st.columns(3)
        with col1:
            date = st.date_input("Date", value=datetime.today())
        with col2:
            category = st.selectbox("Category", ["Food", "Transport", "Shopping", "Bills", "Health", "Other"])
        with col3:
            amount = st.number_input("Amount", min_value=0.0, format="%.2f")
        note = st.text_input("Note (Optional)", max_chars=50)
        submitted = st.form_submit_button("💾 Save Expense")

    if submitted:
        new_entry = {"Date": str(date), "Category": category, "Amount": amount, "Note": note}
        df = load_expenses()
        df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)
        save_expenses(df)
       
          
        msg = st.empty()
        msg.success("✅ Expense saved!")
        time.sleep(1)
        msg.empty()

    # 🧾 Show Expense Table with Edit/Delete
    st.markdown("---")
    st.subheader("📋 Your Expenses")
    df = load_expenses()

    if not df.empty:
        edited_df = df.copy()
        for i in df.index:
            col1, col2, col3 = st.columns([6, 1, 1])
            with col1:
                st.markdown(f"**{df.at[i, 'Date']} | {df.at[i, 'Category']} | ₹{df.at[i, 'Amount']}** — {df.at[i, 'Note']}")
            with col2:
                if st.button("✏️", key=f"edit_{i}"):
                    edited_df = edit_expense(df, i)
            with col3:
                if st.button("🗑️", key=f"delete_{i}"):
                    df = df.drop(index=i).reset_index(drop=True)
                    save_expenses(df)

                    msg = st.empty()
                    msg.warning("❌ Expense deleted.")
                    time.sleep(1)
                    msg.empty()
                    st.rerun()

    else:
        st.info("No expenses added yet.")

def edit_expense(df, index):
    st.markdown("### ✏️ Edit Expense")
    row = df.loc[index]
    with st.form(f"edit_form_{index}"):
        new_date = st.date_input("Date", value=pd.to_datetime(row["Date"]))
        new_cat = st.selectbox("Category", ["Food", "Transport", "Shopping", "Bills", "Health", "Other"], index=["Food", "Transport", "Shopping", "Bills", "Health", "Other"].index(row["Category"]))
        new_amt = st.number_input("Amount", min_value=0.0, value=float(row["Amount"]), format="%.2f")
        new_note = st.text_input("Note", value=row["Note"])
        updated = st.form_submit_button("✅ Update")

    if updated:
        df.at[index, "Date"] = str(new_date)
        df.at[index, "Category"] = new_cat
        df.at[index, "Amount"] = new_amt
        df.at[index, "Note"] = new_note
        save_expenses(df)
        st.success("✅ Expense updated!")
        st.rerun()

    return df
