from ..auth import authenticate
from ..config import CONFIG
import urllib.parse
import requests

def get_content_by_license(token):
    """Make protected request to get content by license ID"""
    query_params = {
        "licenseid": "d3c25de4-12c8-41e9-a294-300f95e4692f"
    }
    
    # Build query string
    query_string = urllib.parse.urlencode(query_params)
    url = f"{CONFIG['baseUrl']}/api/content/getcontentbylicenseid?{query_string}"
    
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    try:
        response = requests.get(
            url,
            headers=headers,
            verify=False  # Disable SSL verification for dev only
        )
        
        # Return both status code and data
        return {
            "status_code": response.status_code,
            "data": response.json() if response.status_code == 200 else response.text
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
    result = get_content_by_license(token)
    
    print("\nResults:")
    print(f"Status Code: {result.get('status_code')}")
    print(f"\nResults: {result}")
    
    if 'data' in result:
        print("Response Data:")
        print(result['data'])
    elif 'error' in result:
        print(f"Error: {result['error']}")