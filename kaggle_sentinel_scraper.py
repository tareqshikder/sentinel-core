import os, json, datetime
try:
    import kaggle
except ImportError:
    print("Kaggle library not found. Install it using: pip install kaggle")

def sovereign_analysis():
    # ক্যাগেল থেকে ডেটা ফেচ করা (সার্চ প্যারামিটার আপনি পরে চেঞ্জ করতে পারবেন)
    try:
        competitions = kaggle.api.competitions_list(search='data science', sort_by='latestDeadline')
        report = []
        
        for c in competitions[:5]:
            days_left = (c.deadline - datetime.datetime.now()).days
            # আপনার সেই হাই-ইন্টেল স্কোর লজিক
            p_score = round((getattr(c, 'reward', 10000) / (days_left + 1)) * 0.01, 3)
            
            report.append({
                "title": c.title,
                "pinnacle_score": p_score,
                "days_left": days_left,
                "teams": getattr(c, 'teamCount', 0),
                "reward": c.reward,
                "recommendation": "HIGH PRIORITY" if p_score > 0.8 else "STABLE"
            })

        output = {
            "best_pick": report[0]['title'] if report else "No Active Stream",
            "last_update": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "report": report
        }

        with open('sentinel_data.json', 'w') as f:
            json.dump(output, f, indent=4)
        print("Success: sentinel_data.json generated.")

    except Exception as e:
        print(f"Error during analysis: {e}")

if __name__ == "__main__":
    sovereign_analysis()
