import os
import requests

DISCORD_URL = os.getenv('DISCORD_WEBHOOK_URL')
SERP_KEY = os.getenv('SERP_API_KEY')

def spy_on_competition():
    # We are searching specifically for what people see when they look for Online MBAs
    params = {
        "engine": "google",
        "q": "best accelerated online mba programs 2026",
        "api_key": SERP_KEY
    }
    
    response = requests.get("https://serpapi.com/search", params=params)
    results = response.json().get('organic_results', [])
    
    report = "🕵️ **COMPETITOR INTELLIGENCE REPORT: ONLINE MBA** 🕵️\n"
    report += "Targeting: *Accelerated / High ROI* \n\n"
    
    for result in results[:3]:
        title = result.get('title')
        link = result.get('link')
        snippet = result.get('snippet')
        
        report += f"🏫 **Top Competitor:** {title}\n"
        report += f"🔗 **Link:** {link}\n"
        report += f"📝 **Their Hook:** {snippet[:100]}...\n\n"
    
    report += "💡 **Scout Insight:** If they all mention 'Accreditation,' we should mention 'Salary Increase' to stand out."
    return report

def send_to_discord(text):
    requests.post(DISCORD_URL, json={"content": text})

if __name__ == "__main__":
    intelligence = spy_on_competition()
    send_to_discord(intelligence))
