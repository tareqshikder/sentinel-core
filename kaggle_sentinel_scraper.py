import kaggle
import json
from datetime import datetime

try:
    api = kaggle.KaggleApi()
    api.authenticate()
    
    # নতুন এপিআই ফরমেট অনুযায়ী প্রতিযোগিতার তালিকা সংগ্রহ
    # এটি সাধারণত একটি লিস্ট অবজেক্ট রিটার্ন করে
    competitions = api.competitions_list(search='sentiment')
    
    data_list = []
    # সরাসরি লুপ ব্যবহার না করে লিস্টে কনভার্ট করে নেওয়া হচ্ছে
    # যদি এটি সরাসরি লিস্ট না হয়, তবে এর 'competitions' প্রোপার্টি দেখা হয়
    comps = getattr(competitions, 'competitions', competitions)
    
    count = 0
    for comp in comps:
        if count >= 3: break
        data_list.append({
            "title": str(getattr(comp, 'title', 'N/A')),
            "deadline": str(getattr(comp, 'deadline', 'N/A')),
            "category": str(getattr(comp, 'category', 'N/A'))
        })
        count += 1

    result = {
        "status": "ONLINE",
        "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "node": "Pixel-7 [Termux]",
        "intelligence_feed": data_list
    }

    with open('sentinel_data.json', 'w') as f:
        json.dump(result, f, indent=4)
    print("Success: sentinel_data.json has been created!")

except Exception as e:
    print(f"Error during analysis: {e}")
