import os
import requests

# Your Secret Vault
CLIENT_ID = os.getenv('PAYPAL_CLIENT_ID')
SECRET = os.getenv('PAYPAL_SECRET')
DISCORD_URL = os.getenv('DISCORD_WEBHOOK_URL')

def test_wallet():
    # 1. Get Access Token from PayPal
    auth_url = "https://api-m.sandbox.paypal.com/v1/oauth2/token"
    token_response = requests.post(
        auth_url,
        auth=(CLIENT_ID, SECRET),
        data={"grant_type": "client_credentials"}
    )
    token = token_response.json().get('access_token')

    # 2. Create a Mock Order for the MBA Report ($9.00)
    order_url = "https://api-m.sandbox.paypal.com/v2/checkout/orders"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }
    payload = {
        "intent": "CAPTURE",
        "purchase_units": [{
            "amount": {"currency_code": "USD", "value": "9.00"},
            "description": "2026 Online MBA ROI Premium Report"
        }]
    }
    
    order_res = requests.post(order_url, json=payload, headers=headers)
    order_id = order_res.json().get('id')
    
    return f"✅ **Wallet Live!** Created PayPal Order: `{order_id}` for $9.00"

if __name__ == "__main__":
    status_msg = test_wallet()
    requests.post(DISCORD_URL, json={"content": status_msg})
