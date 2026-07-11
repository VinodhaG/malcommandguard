# summary_chart.py

import os
import matplotlib.pyplot as plt
from collections import Counter
from datetime import datetime

def extract_classifications(log_path="logs/alerts.log"):
    labels = []
    if not os.path.exists(log_path):
        print("⚠️ No log file found.")
        return labels

    with open(log_path, "r") as file:
        for line in file:
            if "Classification:" in line:
                try:
                    part = line.split("Classification:")[1].strip()
                    label = part.split(" via")[0]
                    labels.append(label)
                except:
                    continue
    return labels

def plot_and_save_pie_chart(labels):
    if not labels:
        print("⚠️ No classification data found in logs.")
        return

    os.makedirs("reports", exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"detection_summary_{timestamp}.png"
    filepath = os.path.join("reports", filename)

    counts = Counter(labels)
    plt.figure(figsize=(6, 6))
    plt.pie(counts.values(), labels=counts.keys(), autopct="%1.1f%%", startangle=90)
    plt.title("MalCommandGuard Detection Summary")
    plt.axis("equal")
    plt.tight_layout()
    plt.savefig(filepath)
    plt.close()

    print(f"\n📊 Pie chart summary saved at: {filepath}")
