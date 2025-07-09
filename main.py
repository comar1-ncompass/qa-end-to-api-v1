import click
from setup.auth import authenticate
from licenses import *


@click.group()
def cli():
    pass

@cli.command()
def hello():
    # Add your other API calls here
    print("Hello World!")

@cli.command()
def test():
    print("Authenticating...")
    token = authenticate()
    
    if not token:
        print("Authentication failed")
        exit(1)
    
    result = get_content_by_license(token)
    
    print("\nResults:")
    print(f"Status Code: {result.get('status_code')}")
    
    if 'data' in result:
        print("Response Data:")
        print(result['data'])
    elif 'error' in result:
        print(f"Error: {result['error']}")

@cli.command()
def dashboard():
    print("Authenticating...")
    token = authenticate()
    
    if not token:
        print("Authentication failed")
        exit(1)
    
    result = get_content_by_license(token)
    
    print("\nResults:")
    print(f"Status Code: {result.get('status_code')}")
    
    if 'data' in result:
        print("Response Data:")
        print(result['data'])
    elif 'error' in result:
        print(f"Error: {result['error']}")

if __name__ == "__main__":
    cli()