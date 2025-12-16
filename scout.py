import os
import requests

# Grab your keys from the GitHub Vault
DISCORD_URL = os.getenv('DISCORD_WEBHOOK_URL')
SERP_KEY = os.getenv('SERP_API_KEY')

def scout_trends():
    # This tells the AI to look for rising business keywords
    search_url = f"https://serpapi.com/search?engine=google_trends&q=startup+ideas&api_key={SERP_KEY}"
    # For now, we'll send a test 'Success' message to your Discord
    message = {
        "content": "🚀 **Scout Agent Online!** I have access to the Market Eyes and the PayPal Wallet. Ready to hunt for 10x brands."
    }
    requests.post(DISCORD_URL, json=message)

if __name__ == "__main__":
    scout_trends()
