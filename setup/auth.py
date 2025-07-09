# auth.py
import requests
from config import CONFIG
from typing import Optional

def authenticate() -> Optional[str]:
    """
    Authenticate with the API and return the token if successful.
    
    Returns:
        Token string if successful, None otherwise
    """
    login_url = f"{CONFIG['baseUrl']}/api/account/login"
    payload = {
        "username": "francisc@admin.com",
        "password": "password"
    }
    
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    try:
        # Disable SSL verification for dev environment only
        response = requests.post(
            login_url,
            json=payload,
            headers=headers,
            verify=False
        )
        
        if response.status_code == 200:
            return response.json().get('token')
        
        print(f"Login failed (HTTP {response.status_code}): {response.text}")
        
    except Exception as e:
        print(f"Authentication error: {str(e)}")
    
    return None

def main():
    print("Attempting login...")
    token = authenticate()
    
    if token:
        print("Login successful!")
        print(f"Session token: {token}")
        return 0
    else:
        print("Login failed")
        return 1

if __name__ == "__main__":
    import sys
    sys.exit(main())