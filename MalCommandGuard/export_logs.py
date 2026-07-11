import os
import csv
import re
from datetime import datetime

def export_logs_to_csv(log_path, output_path):
    if not os.path.exists(log_path):
        print(f"❌ Log file not found: {log_path}")
        return

    with open(log_path, "r") as f:
        lines = f.readlines()

    log_entries = []
    pattern = re.compile(r"(.*?) - .*? - Input: (.*?) \| Classification: (.*?) via (.*)")

    for line in lines:
        match = pattern.search(line)
        if match:
            timestamp, input_data, classification, method = match.groups()
            log_entries.append([timestamp.strip(), input_data.strip(), classification.strip(), method.strip()])

    if not log_entries:
        print("⚠️ No valid entries found in log.")
        return

    with open(output_path, "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["Timestamp", "Input", "Classification", "Method"])
        writer.writerows(log_entries)

    print(f"✅ Exported log data to {output_path}")
