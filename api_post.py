import requests

url = "https://jsonplaceholder.typicode.com/posts"

payload = {
    "title": "Hello AI",
    "body": "This is my first post request",
    "userId": 1
}

response = requests.post(url, json=payload)

if response.status_code == 201:
    print("✅ Login successful!")
    print("Response Data:", response.json())
else:
    print("❌ Login failed with status code:", response.status_code)
    print("Response Data:", response.text)
