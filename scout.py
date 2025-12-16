import os
import requests

DISCORD_URL = os.getenv('DISCORD_WEBHOOK_URL')
SERP_KEY = os.getenv('SERP_API_KEY')

def get_business_opportunities():
    # Category 12 = Business & Industrial | Category 30 = Finance
    # We scan for 'Rising' queries which represent the 10x 'Breakout' potential
    params = {
        "engine": "google_trends",
        "data_type": "RELATED_QUERIES",
        "cat": "12", 
        "api_key": SERP_KEY
    }
    
    try:
        response = requests.get("https://serpapi.com/search", params=params)
        data = response.json()
        rising = data.get('related_queries', {}).get('rising', [])
        
        if not rising:
            return "🔍 Market is steady. No massive breakouts in Category 12 yet."

        report = "🚀 **10x BUSINESS OPPORTUNITY REPORT** 🚀\n"
        report += "--- *High-Growth Niche Detected* ---\n"
        
        for item in rising[:5]: # Top 5 rising trends
            query = item.get('query')
            growth = item.get('extracted_value')
            # The higher the growth %, the higher the "10x" potential
            report += f"🔥 **Niche:** {query}\n📈 **Velocity:** +{growth}%\n"
            report += f"💡 **Angle:** Can we build a service/tool for this?\n\n"
        
        return report
    except Exception as e:
        return f"⚠️ Scout Error: {str(e)}"

def send_to_discord(text):
    requests.post(DISCORD_URL, json={"content": text})

if __name__ == "__main__":
    report_content = get_business_opportunities()
    send_to_discord(report_content)
