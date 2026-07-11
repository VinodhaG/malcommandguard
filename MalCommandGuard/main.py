from monitor_realtime import monitor_history
from detector import rule_based_check, signature_based_check, ml_based_check
from secure_utils import is_valid_input
from alert import alert_user
import os
from datetime import datetime
from log_viewer import view_log_history

def main_menu():
    while True:
        print("\n🛡️ Welcome to MalCommandGuard 🛡️")
        print("1. Monitor in Real-Time ")
        print("2. Rule-Based Detection ")
        print("3. Signature-Based Detection ")
        print("4. Machine Learning-Based Detection ")
        print("5. Download Detection Summary Chart 📊")
        print("6. View Log History")
        print("7. Export logs as CSV")
        print("8. Exit")

        choice = input("Select an option: ").strip()

        if choice == "1":
            monitor_history()

        elif choice == "2":
            cmd = input("Enter command for Rule-Based Detection: ").strip()
            if is_valid_input(cmd):
                result = rule_based_check(cmd, input_type="command")
                final_result = result or "Legitimate"
                print(f"🔍 Detection Result: {final_result}")
                alert_user(final_result, cmd)
            else:
                print("❌ Invalid input detected. Please avoid special characters like ; | & `")

        elif choice == "3":
            cmd = input("Enter URL or command for Signature-Based Detection: ").strip()
            if is_valid_input(cmd):
                result = signature_based_check(cmd)
                final_result = result or "Legitimate"
                print(f"🔍 Detection Result: {final_result}")
                alert_user(final_result, cmd)
            else:
                print("❌ Invalid input detected. Please avoid special characters like ; | & `")


        elif choice == "4":

            cmd = input("Enter URL or command for Machine Learning Detection: ").strip()
            # SKIP strict validation for ML test
            result = ml_based_check(cmd)
            print(f"🤖 ML Detection Result: {result}")
            alert_user(result, cmd)

        elif choice == "5":
            from summary_chart import extract_classifications, plot_and_save_pie_chart
            labels = extract_classifications()
            plot_and_save_pie_chart(labels)

        elif choice == "6":
            view_log_history()

        elif choice == "7":
            from export_logs import export_logs_to_csv
            log_path = os.path.join("logs", "alerts.log")
            now = datetime.now().strftime("%Y%m%d")
            output_path = os.path.join("reports", f"alerts_{now}.csv")
            export_logs_to_csv(log_path, output_path)

        elif choice == "8":
            print("🔚 Exiting MalCommandGuard. Stay safe!")
            break
        else:
            print("❗ Invalid option. Please choose 1–5.")


            print("7. Export alerts.log as CSV")

if __name__ == "__main__":
    main_menu()
