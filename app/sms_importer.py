# app/sms_importer.py

import streamlit as st
import pandas as pd
from app import utils

def import_sms():
    st.title("📩 Import SMS Expenses")
    uploaded_file = st.file_uploader("Upload your SMS log (.txt or .csv)", type=["txt", "csv"])

    if uploaded_file is not None:
        user_phone = st.session_state.get("phone", "").strip()
        if not user_phone:
            st.warning("No phone number found for this user.")
            return

        try:
            if uploaded_file.name.endswith(".csv"):
                df = pd.read_csv(uploaded_file)
            else:
                content = uploaded_file.read().decode("utf-8")
                lines = content.splitlines()
                df = pd.DataFrame({"SMS": lines})

            st.success("SMS logs uploaded successfully.")
            count = 0

            for _, row in df.iterrows():
                sms_text = str(row[0])
                if user_phone not in sms_text:
                    continue
                if "debited" in sms_text.lower() or "spent" in sms_text.lower():
                    amount = utils.extract_amount(sms_text)
                    note = sms_text[:60]
                    date = utils.current_date()
                    utils.save_expense(st.session_state.username, {
                        "Date": date,
                        "Category": "Auto",
                        "Amount": amount,
                        "Note": note
                    })
                    count += 1

            if count > 0:
                st.success(f"{count} expenses imported from SMS linked to your number.")
            else:
                st.warning("No matching expenses found for your phone number.")

        except Exception as e:
            st.error(f"Failed to parse file: {e}")
