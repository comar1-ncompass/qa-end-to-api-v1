import click

from licenses.test                      import *  
from licenses.get_installation_stats    import *  
from notification                             import get_total as notification 
from dealer                             import get_total as dealer 
from host                               import get_total as host
from advertiser                         import get_total as advertiser
from licenses                           import get_total as license
from feed                               import get_total as feed
from content                            import get_total as content
from user                               import get_total as user

#helper functions
def show_result(result):
    print("\nResults:")
    print(f"Title: {result.get('title')}")
    print(f"Status Code: {result.get('status_code')}")
    
    # Check status code first
    if result.get('status_code') != 200:
        # Print any available error data
        if 'data' in result:
            print("Error Data:")
            print(result['data'])
        elif 'error' in result:
            print(f"Error: {result['error']}")
        
        print("Test failed!")
    else:
        # Success case - only show data if present
        if 'data' in result:
            print("Response Data:")
            print(result['data'])
        
#main functions
@click.group()
def cli():
    pass

@cli.command()
def hello4():
    # Add your other API calls here
    print("Hello World!")

@cli.command()
def dashboard():
    # Add your other API calls here
    print("Dashboard Module")
    print("\nAuthenticating...")
    token = authenticate()
    
    if not token:
        print("Authentication failed")
        exit(1)
    
    show_result(notification.get_total(token))
    show_result(get_installation_stats(token))
    
    show_result(dealer.get_total(token))
    show_result(host.get_total(token))
    show_result(advertiser.get_total(token))
    show_result(license.get_total(token))
    
    show_result(get_installation_stats(token))
    
    show_result(feed.get_total(token))
    show_result(content.get_total(token))
    show_result(user.get_total(token))
    
if __name__ == "__main__":
    cli()