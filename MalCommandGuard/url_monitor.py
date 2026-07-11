def monitor_url():
    print("\n[URL Input] Enter the URL you want to simulate:")
    url = input(">> ").strip()

    # Basic input validation
    if not url or not url.startswith(("http://", "https://")):
        print("❌ Invalid URL. Please enter a valid URL (starting with http:// or https://).\n")
        return monitor_url()

    return url
