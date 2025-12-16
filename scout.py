import os
import requests

# Load your secret keys
DISCORD_URL = os.getenv('DISCORD_WEBHOOK_URL')
SERP_KEY = os.getenv('SERP_API_KEY')

def get_10x_trends():
    # Target 'Rising' trends in the 'Business & Industrial' category
    params = {
        "engine": "google_trends",
        "data_type": "RELATED_QUERIES",
        "cat": "12", # Category 12 is Business & Industrial
        "api_key": SERP_KEY
    }
    
    response = requests.get("https://serpapi.com/search", params=params)
    data = response.json()
    
    # We look for 'Rising' queries - these are the explosive ones
    rising_queries = data.get('related_queries', {}).get('rising', [])
    
    if not rising_queries:
        return "No breakout trends found in the last 4 hours. Scanning again soon..."

    # Format the top 3 discoveries for Discord
    report = "🚀 **10x Opportunity Scout Report** 🚀\n"
    for item in rising_queries[:3]:
        query = item.get('query')
        extract = item.get('extracted_value')
        report += f"🔹 **Trend:** {query} | **Growth:** +{extract}%\n"
    
    return report

def send_to_discord(text):
    requests.post(DISCORD_URL, json={"content": text})

if __name__ == "__main__":
    report_content = get_10x_trends()
    send_to_discord(report_content)
