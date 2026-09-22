import requests
url = "http://127.0.0.1:5000/webhook"

data ={
    "event": "payment_success",
    "amount": 500000,
    "customer": "Priya"
}

response  = requests.post(url, json=data) # it means "Send a POST request to this URL and put this data into the request as JSON."

print(response.status_code)
print(response.json())