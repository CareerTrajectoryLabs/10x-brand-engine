import os
import requests

# Your PayPal Vault
CLIENT_ID = os.getenv('PAYPAL_CLIENT_ID')
SECRET = os.getenv('PAYPAL_SECRET')

def get_paypal_token():
    url = "https://api-m.sandbox.paypal.com/v1/oauth2/token"
    data = {"grant_type": "client_credentials"}
    auth = (CLIENT_ID, SECRET)
    response = requests.post(url, data=data, auth=auth)
    return response.json().get('access_token')

def create_test_order(token):
    url = "https://api-m.sandbox.paypal.com/v2/checkout/orders"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }
    payload = {
        "intent": "CAPTURE",
        "purchase_units": [{"amount": {"currency_code": "USD", "value": "9.00"}}]
    }
    res = requests.post(url, json=payload, headers=headers)
    return res.json()

if __name__ == "__main__":
    token = get_paypal_token()
    order = create_test_order(token)
    print(f"✅ PayPal Order Created! ID: {order.get('id')}")
    # In a real app, this ID would trigger the 'Buy Now' button on your site
