import requests

url = "http://localhost:8000/create_user/"
data = {
    "username": "john_doe",
    "email": "john@example.com"
}

response = requests.post(url, json=data)
print(response.json())
