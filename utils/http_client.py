import requests

class HttpClient:
    def post(self, url, headers=None, json=None):
        return requests.post(url, headers=headers, json=json, timeout=15)
