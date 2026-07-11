def monitor_command():
    print("\n[Command Input] Enter the command you want to simulate:")
    command = input(">> ").strip()

    # Basic input validation
    if not command:
        print("❌ Empty command. Please enter a valid command.\n")
        return monitor_command()

    return command
