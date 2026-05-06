import requests

# আপনার কনফিগারেশন
BOT_TOKEN = "8555103560:AAFumrrDCPgcxydJdlmV5QLq4OZ7wLLaUYg"
MY_CHAT_ID = "1277791976"

def send_alert(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": MY_CHAT_ID, "text": message}
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            print("[✔] Alert Sent to Telegram!")
            return True
        else:
            print(f"[!] API Error: {response.status_code}")
            return False
    except Exception as e:
        print(f"[!] Connection Error: {e}")
        return False

if __name__ == "__main__":
    send_alert("🔴 [SENTINEL] Pixel-7 Node is now ONLINE.")
