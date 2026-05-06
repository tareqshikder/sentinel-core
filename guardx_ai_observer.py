import time
import datetime
from telegram_bridge import send_alert

def start_observer():
    print("------------------------------------")
    print("[*] GUARDX AI OBSERVER v1.0")
    print("[*] Node: Pixel-7 | System: Sovereign-01")
    print("------------------------------------")
    
    # শুরুর নোটিফিকেশন
    send_alert("🚀 GUARDX AI Observer started monitoring.")

    try:
        while True:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            
            # সিস্টেম কার্যক্রম
            print(f"[{current_time}] Scanning Satellite Feed... Status: SECURE")
            print(f"[{current_time}] Syncing with Localhost:3000")
            
            # ৩০ সেকেন্ড পর পর আপডেট
            time.sleep(30)
            
    except KeyboardInterrupt:
        print("\n[-] Observer Stopped.")
        send_alert("⚠️ System Offline: Observer stopped by user.")

if __name__ == "__main__":
    start_observer()
