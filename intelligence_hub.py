import yfinance as yf
import feedparser
import json
import os
from datetime import datetime

# ১. মার্কেট ও ইকোনমিক ডাটা মডিউল (BTC, ETH, TSLA, NVDA)
def fetch_market_intel():
    print("📈 Fetching Live Market & NG-Tech Data...")
    symbols = {
        "Bitcoin": "BTC-USD",
        "Ethereum": "ETH-USD",
        "Tesla": "TSLA",
        "NVIDIA (AI Trend)": "NVDA",
        "Gold": "GC=F"
    }
    market_report = {}
    for name, ticker in symbols.items():
        try:
            stock = yf.Ticker(ticker)
            price = stock.history(period="1d")['Close'].iloc[-1]
            market_report[name] = f"${round(price, 2)}"
        except:
            market_report[name] = "Data Unavailable"
    return market_report

# ২. ডিপ লার্নিং ও এআই রিসার্চ মডিউল (ArXiv)
def fetch_ai_research_intel():
    print("🧠 Fetching AI & Deep Learning Research from ArXiv...")
    url = "http://export.arxiv.org/api/query?search_query=cat:cs.AI+OR+cat:cs.LG&sortBy=submittedDate&max_results=5"
    feed = feedparser.parse(url)
    research_list = []
    for entry in feed.entries:
        research_list.append({
            "title": entry.title.replace('\n', ' '),
            "link": entry.link
        })
    return research_list

# ৩. ডাটা সিঙ্ক্রোনাইজেশন ও ড্যাশবোর্ড আপডেট
def sync_to_dashboard(market_data, ai_data):
    file_path = "live_intel.json"
    dashboard_payload = {
        "last_updated": datetime.now().strftime("%Y-%m-%d %I:%M %p"),
        "node": "Tecno-Station-Mohammadpur",
        "market_analysis": market_data,
        "latest_ai_research": ai_data,
        "status": "Operational"
    }
    
    with open(file_path, "w") as f:
        json.dump(dashboard_payload, f, indent=4)
    
    print("✅ Dashboard JSON generated. Pushing to GitHub...")
    os.system("git add .")
    os.system(f'git commit -m "Sentinel Update: {datetime.now().strftime("%H:%M")}"')
    os.system("git push origin main")

if __name__ == "__main__":
    print("🛰️ Sentinel Core Engine Starting...")
    
    # ডাটা কালেকশন
    markets = fetch_market_intel()
    ai_research = fetch_ai_research_intel()
    
    # অটোমেটিক সিঙ্ক এবং পুশ
    sync_to_dashboard(markets, ai_research)
    
    print(f"🏁 Mission Accomplished at {datetime.now().strftime('%I:%M %p')}")
