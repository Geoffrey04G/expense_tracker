import os
import pandas as pd
from datetime import datetime
import re

def save_expense(username, expense_data):
    filepath = f"data/expenses/{username}.csv"
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    df = pd.DataFrame([expense_data])
    if os.path.exists(filepath):
        df.to_csv(filepath, mode="a", header=False, index=False)
    else:
        df.to_csv(filepath, index=False)

def extract_amount(text):
    match = re.search(r"(INR|Rs\.?)\s?(\d+[.,]?\d*)", text, re.IGNORECASE)
    if match:
        return float(match.group(2).replace(",", ""))
    return 0.0

def current_date():
    return datetime.now().strftime("%Y-%m-%d")
