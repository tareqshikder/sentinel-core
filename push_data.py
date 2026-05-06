import requests
import time

# আপনার ড্যাশবোর্ড বা ব্যাকএন্ড এপিআই ইউআরএল
ENDPOINT = "https://shikder.blogspot.com/api/v1/update" 
# নোট: ব্লগস্পটে সরাসরি ডেটা পুশ করতে কাস্টম স্ক্রিপ্ট বা ফায়ারবেস ব্যবহার করা ভালো।

payload = {
    "node_id": "Pixel-7",
    "system_status": "Sovereign-01",
    "action": "SCANNING_SATELLITE_FEED",
    "secure_handshake": "TRUE"
}

def initiate_push():
    try:
        print("[*] Initializing Secure Handshake...")
        response = requests.post(ENDPOINT, json=payload)
        if response.status_code == 200:
            print("[+] Push Success: Initialized from Termux Node [Pixel-7]")
        else:
            print(f"[-] Error: {response.status_code}")
    except Exception as e:
        print(f"[-] Connection Failed: {e}")

if __name__ == "__main__":
    initiate_push()
