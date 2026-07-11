import time
import os

from detector import detect_threat_realtime
from alert import alert_user
from detector import rule_based_check, signature_based_check, ml_based_check
from secure_utils import is_valid_input

# Path to PowerShell command history
HISTORY_FILE = os.path.expanduser(
    r"C:\Users\Vinodha G\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt"
)

# Store previously seen lines
def load_existing_lines():
    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            return f.readlines()
    except FileNotFoundError:
        print("❌ History file not found. Is PowerShell being used?")
        return []

def monitor_history():
    print("📡 MalCommandGuard is now monitoring PowerShell activity in real time...\n")
    seen = load_existing_lines()
    seen_count = len(seen)

    while True:
        try:
            with open(HISTORY_FILE, "r", encoding="utf-8") as f:
                lines = f.readlines()

            new_lines = lines[seen_count:]
            if new_lines:
                for line in new_lines:
                    cmd = line.strip()
                    if cmd:
                        print(f"[INPUT] New Command: {cmd}")

                        if is_valid_input(cmd):
                            if signature_based_check(cmd):
                                classification = "Malicious"
                                method = "Signature-Based"
                            elif rule_based_check(cmd, input_type="command"):
                                classification = "Suspicious"
                                method = "Rule-Based"
                            else:
                                classification = ml_based_check(cmd)
                                method = "Machine Learning-Based" if classification == "Malicious" else None

                            if classification != "Legitimate":
                                print(f"[ALERT] {classification} detected by {method}:\n→ {cmd}")
                                alert_user(f"{classification} ({method})", cmd)

                seen_count = len(lines)

        except Exception as e:
            print(f"⚠️ Error reading history: {e}")

        time.sleep(3)  # Check every 3 seconds

if __name__ == "__main__":
    monitor_history()

def monitor_history():
    print("📡 MalCommandGuard is now monitoring PowerShell activity in real time...")
    print("➡️ Press Ctrl + C to stop monitoring and return to main menu.\n")
    seen = load_existing_lines()
    seen_count = len(seen)

    try:
        while True:
            with open(HISTORY_FILE, "r", encoding="utf-8") as f:
                lines = f.readlines()

            new_lines = lines[seen_count:]
            if new_lines:
                for line in new_lines:
                    cmd = line.strip()
                    if cmd:
                        print(f"[INPUT] New Command: {cmd}")
                        classification, method = detect_threat_realtime(cmd, input_type="command")
                        alert_user(classification, cmd, method=method)

                seen_count = len(lines)

            time.sleep(3)  # Check every 3 seconds

    except KeyboardInterrupt:
        print("\n🔙 Returning to main menu...")