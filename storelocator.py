import requests
import json
import pandas as pd

def fetch_stores():
    url = "https://stockist.co/api/v1/u16021/locations/search"
    params = {
        "tag": "u16021",
        "latitude": 37.7749,  # Default to San Francisco, adjust if needed
        "longitude": -122.4194,
        "filter_operator": "and",
        "distance": 500000  # Large distance to capture most stores
    }

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    response = requests.get(url, params=params, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        stores = data.get("locations", [])
        
        if stores:
            save_data(stores)
        else:
            print("No store data found.")
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")

def save_data(stores):
    json_filename = "brightland_stores.json"
    csv_filename = "brightland_stores.csv"
    
    # Save the raw store data
    with open(json_filename, "w", encoding="utf-8") as json_file:
        json.dump(stores, json_file, indent=4)
    
    # Convert the stores to a DataFrame and save as CSV
    df = pd.DataFrame(stores)
    df.to_csv(csv_filename, index=False)
    
    print(f"Data saved to {json_filename} and {csv_filename}")

def filter_stores_with_website(json_filename="brightland_stores.json"):
    # Read the JSON file
    with open(json_filename, "r", encoding="utf-8") as json_file:
        stores = json.load(json_file)
    
    # Filter stores that have a non-empty 'website'
    filtered_stores = [store for store in stores if store.get("website")]
    
    # Remove duplicates based on the 'website' field
    seen_websites = set()
    unique_stores = []
    for store in filtered_stores:
        website = store.get("website")
        if website not in seen_websites:
            seen_websites.add(website)
            unique_stores.append(store)
    
    # Save filtered and deduplicated stores back to a new file
    filtered_json_filename = "brightland_stores_with_websites_unique.json"
    with open(filtered_json_filename, "w", encoding="utf-8") as json_file:
        json.dump(unique_stores, json_file, indent=4)
    
    # Also save to CSV if needed
    df = pd.DataFrame(unique_stores)
    filtered_csv_filename = "brightland_stores_with_websites_unique.csv"
    df.to_csv(filtered_csv_filename, index=False)

    print(f"Filtered and unique data saved to {filtered_json_filename} and {filtered_csv_filename}")

if __name__ == "__main__":
    fetch_stores()  # Uncomment this to fetch new data
    filter_stores_with_website()  # Uncomment to filter and save stores with websites and remove duplicates
