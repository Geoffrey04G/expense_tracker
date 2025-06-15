# app/upi_classifier.py

def classify_transaction(note: str) -> str:
    note = note.lower()
    keywords = {
        "zomato": "Food",
        "swiggy": "Food",
        "ola": "Transport",
        "uber": "Transport",
        "amazon": "Shopping",
        "flipkart": "Shopping",
        "phonepe": "Transfer",
        "gpay": "Transfer",
        "electricity": "Utilities",
        "recharge": "Utilities",
        "rent": "Housing",
        "petrol": "Fuel",
        "dmart": "Groceries",
    }
    for key, category in keywords.items():
        if key in note:
            return category
    return "Others"
