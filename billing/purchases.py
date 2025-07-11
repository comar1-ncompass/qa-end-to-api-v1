import urllib.parse
import requests

from setup.auth import authenticate
from setup.config import CONFIG

# Add the project root to Python path

def purchases(token):
    """Make protected request to get content by license ID"""
    query_params = {
        "page": 1,
        "pageSize": 0,
        "filterBy": "",
        "from": "01-01-2025",
        "to": "07-10-2025",
        "status": "",
    }
    
    # Build query string
    query_string = urllib.parse.urlencode(query_params)
    
    title="Billing get all purchases"
    url = f"{CONFIG['baseUrl']}/api/billing/get/all/purchases?{query_string}"
    
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
    result = purchases(token)
    
    print("\nResults:")
    print(f"Title: {result.get('title')}")
    print(f"Status Code: {result.get('status_code')}")
    print(f"\nResults: {result}")
    
    if 'data' in result:
        print("Response Data:")
        print(result['data'])
    elif 'error' in result:
        print(f"Error: {result['error']}")