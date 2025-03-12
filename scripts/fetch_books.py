import requests
import json
import os

# API Endpoint
url = "https://api.nytimes.com/svc/books/v3/lists/current/hardcover-fiction.json"

# Your NYT API Key (Replace with your actual key)
api_key = "your_api_key_here"

# Send API Request
response = requests.get(url, params={"api-key": api_key})

# Check if request was successful
if response.status_code == 200:
    data = response.json()
    
    # Save the JSON response in a file inside the 'data' folder
    os.makedirs("../data", exist_ok=True)  # Ensure the data folder exists
    with open("../data/bestsellers.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    print("✅ Data saved successfully in 'data/bestsellers.json'")

else:
    print("❌ Error fetching data:", response.status_code)
