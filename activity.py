import sys
import requests

[_, type, username] = sys.argv

def get_url(username):
    return f'https://api.github.com/users/{username}/events'

response = requests.get(get_url(username))

if (response.status_code == 200):
    print('Success: ', response.json())
else:
    print('Failed: ', response.status_code)
    
