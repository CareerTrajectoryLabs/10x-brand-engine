import os
import requests

DISCORD_URL = os.getenv('DISCORD_WEBHOOK_URL')
SERP_KEY = os.getenv('SERP_API_KEY')

def get_intelligence():
    params = {
        "engine": "google",
        "q": "best accelerated online mba programs 2026",
        "api_key": SERP_KEY
    }
    
    try:
        response = requests.get("https://serpapi.com/search", params=params)
        results = response.json().get('organic_results', [])
        
        # Start the Report
        report = "📊 **10X INTELLIGENCE: MARKET PENETRATION REPORT** 📊\n"
        report += "--- \n"
        
        for result in results[:3]:
            title = result.get('title')
            snippet = result.get('snippet', '')
            
            # Logic to find the "Weakness" in their hook
            if "accredited" in snippet.lower():
                strategy = "Target 'Speed to Completion' instead."
            elif "rankings" in snippet.lower():
                strategy = "Target 'Salary ROI' instead."
            else:
                strategy = "Standard SEO competition; use high-conversion video."

            report += f"🏫 **Competitor:** {title}\n"
            report += f"💡 **Counter-Strategy:** {strategy}\n\n"
        
        return report
    except Exception as e:
        return f"⚠️ Intel Error: {str(e)}"

def send_to_discord(text):
    requests.post(DISCORD_URL, json={"content": text})

if __name__ == "__main__":
    intelligence_report = get_intelligence()
    send_to_discord(intelligence_report)
