import re
import csv

# Load rule patterns from rules.txt with fail-safe handling
def load_rules():
    rules = []
    try:
        with open('rules.txt', 'r') as file:
            for line in file:
                pattern = line.strip()
                if pattern:
                    rules.append(pattern)
    except Exception as e:
        print("⚠️ Rules file missing or corrupted. Continuing with no rules.")
        rules = []  # Ensure safe default
    return rules


RULE_PATTERNS = load_rules()

# Load blacklist from signature.csv with secure file handling
def load_blacklist():
    blacklist = set()
    try:
        with open('signature.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                blacklist.add(row[0].strip().lower())
    except Exception as e:
        print("⚠️ Signature list not found. Continuing without blacklist.")
        blacklist = set()  # Safe fallback
    return blacklist

BLACKLIST = load_blacklist()

# Rule-based detection
def rule_based_check(data, input_type):
    for pattern in RULE_PATTERNS:
        if re.search(pattern, data, re.IGNORECASE):
            return "Suspicious"
    return None


# Signature-based detection (blacklist match)
def signature_based_check(data):
    for domain in BLACKLIST:
        if domain in data.lower():
            return "Malicious"
    return None

# Real-time detection logic (used in monitor_history)
# Final detection decision
def detect_threat_realtime(data, input_type="command"):
    result = signature_based_check(data)
    if result:
        return result, "Signature-Based"

    result = rule_based_check(data, input_type)
    if result:
        return result, "Rule-Based"

    # Machine Learning
    prediction = ml_model.predict([data])[0]
    if prediction == 1:
        return "Malicious", "Machine Learning"
    elif prediction == 0:
        return "Legitimate", "Machine Learning"

    return "Legitimate", "Unknown"

# NLP-based Detection
import joblib
import os

# Load ML model with fail-safe error handling
ml_model_path = os.path.join(os.path.dirname(__file__), "ml_model.joblib")
try:
    ml_model = joblib.load(ml_model_path)
except Exception as e:
    print("⚠️ ML model could not be loaded. ML detection will default to Legitimate.")
    ml_model = None  # Fallback: disables ML if broken

def ml_based_check(data):
    """
    Returns 'Malicious' or 'Legitimate' based on trained ML model.
    """
    if ml_model is None:
        return "Legitimate"
    try:
        prediction = ml_model.predict([data])[0]
        return "Malicious" if prediction == 1 else "Legitimate"
    except Exception as e:
        print(f"⚠️ ML prediction failed: {e}")
        return "Legitimate"

