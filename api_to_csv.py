import requests
import pandas as pd

url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    df = pd.DataFrame(data)

    df.to_csv("users_data.csv", index=False)

    print("Data successfully written to users_data.csv")
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")