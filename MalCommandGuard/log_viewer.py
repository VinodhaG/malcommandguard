import os
from datetime import datetime

LOG_FILE = os.path.join("logs", "alerts.log")

def view_log_history():
    print("\n🔍 Log History Viewer")

    if not os.path.exists(LOG_FILE):
        print("⚠️ No log file found.")
        return

    # Ask for filters
    date_filter = input("Enter date (YYYY-MM-DD) or leave blank for all: ").strip()
    category_filter = input("Filter by classification (Malicious/Suspicious/Legitimate) or leave blank: ").strip().capitalize()
    keyword_filter = input("Enter keyword to search in input (optional): ").strip().lower()

    print("\n📝 Matching Log Entries:\n" + "-" * 40)

    found = False
    with open(LOG_FILE, "r") as f:
        for line in f:
            if date_filter and date_filter not in line:
                continue
            if category_filter and category_filter not in line:
                continue
            if keyword_filter and keyword_filter not in line.lower():
                continue
            print(line.strip())
            found = True

    if not found:
        print("❌ No matching entries found.")
