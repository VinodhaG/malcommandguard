import logging
import os
from plyer import notification

# Setup logging
log_file_path = os.path.join("logs", "alerts.log")
logging.basicConfig(filename=log_file_path,
                    level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

def alert_user(classification, data, method="Unknown"):
    # Console output
    print(f"\n[ALERT] {classification} activity detected!")
    print(f"[DETAIL] Input: {data}")
    print(f"[STATUS] Classification: {classification} via {method}\n")

    # Log file output (with log input sanitization)
    safe_data = data.replace("\n", " ").replace("\r", " ").replace(";", "").replace("&", "")
    logging.info(f"Input: {safe_data} | Classification: {classification} via {method}")

    # Windows notification (only for malicious or suspicious)
    if classification in ["Malicious", "Suspicious"]:
        notification.notify(
            title="⚠️ MalCommandGuard Alert",
            message=f"{classification} activity detected ({method}):\n{data}",
            timeout=5  # seconds
        )

if __name__ == "__main__":
    alert_user("Malicious", "Test payload: rm -rf /")
