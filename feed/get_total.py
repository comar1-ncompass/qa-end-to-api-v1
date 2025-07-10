import urllib.parse
import requests

from setup.auth import authenticate
from setup.config import CONFIG

# Add the project root to Python path

def get_total(token):
    
    title="Get Total Stats for Feed"
    url = f"{CONFIG['baseUrl']}/api/feed/gettotal"
    
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    try:
        response = requests.get(
            url,
            headers=headers,
            verify=True  # Disable SSL verification for dev only
        )
        
        # Return both status code and data
        return {
            "title": title,  # Add title to the result
            "status_code": response.status_code,
            "data": response.json() if response.status_code == 200 else response.text,
        }
        
    except Exception as e:
        return {
            "status_code": None,
            "error": str(e)
        }

if __name__ == "__main__":
    print("Authenticating...")
    token = authenticate()
    
    if not token:
        print("Authentication failed")
        exit(1)
    
    print("\nMaking API request...")
    result = get_total(token)
    
    print("\nResults:")
    print(f"Title: {result.get('title')}")
    print(f"Status Code: {result.get('status_code')}")
    print(f"\nResults: {result}")
    
    if 'data' in result:
        print("Response Data:")
        print(result['data'])
    elif 'error' in result:
        print(f"Error: {result['error']}")