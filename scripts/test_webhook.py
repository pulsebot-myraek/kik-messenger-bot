import requests

payload = {
  "messages": [{
    "from": "test_user",
    "body": "hi"
  }]
}

r = requests.post("http://localhost:8000/webhook", json=payload)
print(r.json())
