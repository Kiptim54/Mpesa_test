import requests,base64
from requests.auth import HTTPBasicAuth

consumer_key = "7ZMqQX8lPhQdyuA2IuFsBA2RzI5JkYHZ"
consumer_secret = "oqLpPUVGzkF14VP1"
api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
print (r.text)


# auth_token = "7ZMqQX8lPhQdyuA2IuFsBA2RzI5JkYHZ:oqLpPUVGzkF14VP1"
auth_token_encoded = r.request.headers['Authorization']
print(auth_token_encoded)


access_token = auth_token_encoded
api_url = "http://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"
headers = {"Authorization": access_token}
request = { "ShortCode": "600532",
    "ResponseType": " Cancelled",
    "ConfirmationURL": "https://http://127.0.0.1:8000/api/confirmation.php",
    "ValidationURL": "https://http://127.0.0.1:8000/api/validation.php"}

response = requests.post(api_url, json = request, headers=headers)

print (response.text)

import requests

access_token = auth_token_encoded
api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/simulate"
headers = {"Authorization":access_token}
request = { "ShortCode":"600532",
  "CommandID":"CustomerPayBillOnline",
  "Amount":"10",
  "Msisdn":"254708374149",
  "BillRefNumber":"account" }

response = requests.post(api_url, json = request, headers=headers)

print (response.text)