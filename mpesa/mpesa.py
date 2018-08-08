import requests,base64
from requests.auth import HTTPBasicAuth

consumer_key = "7ZMqQX8lPhQdyuA2IuFsBA2RzI5JkYHZ"
consumer_secret = "oqLpPUVGzkF14VP1"
api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
print (r.request.headers['Authorization'])


# auth_token = "7ZMqQX8lPhQdyuA2IuFsBA2RzI5JkYHZ:oqLpPUVGzkF14VP1"
auth_token_encoded = r.request.headers['Authorization']
print(auth_token_encoded)


access_token = auth_token_encoded
api_url = "http://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"
headers = {"Authorization": access_token}
request = { "ShortCode": "600532",
    "ResponseType": " Cancelled",
    "ConfirmationURL": "http://http://127.0.0.1:8000/confirmation",
    "ValidationURL": "http://http://127.0.0.1:8000/validation_url"}

response = requests.post(api_url, json = request, headers=headers)

print (response.text)