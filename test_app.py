import requests

# Hardcoded API key - đây là lỗi bảo mật!
API_KEY = "ghp_aBcDeFgHiJkLmNoPqRsTuVwXyZ123456"

def get_data():
    response = requests.get("https://api.example.com", headers={"Authorization": API_KEY})
    return response.json()
