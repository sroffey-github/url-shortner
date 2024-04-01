from dotenv import load_dotenv
import os, requests

load_dotenv()
API_TOKEN = os.getenv('API_TOKEN')

def shorten_url(long_url):
    endpoint = 'https://api-ssl.bitly.com/v4/shorten'
    headers = {
        'Authorization': f'Bearer {API_TOKEN}',
        'Content-Type': 'application/json',
    }
    data = {
        'long_url': long_url,
    }
    response = requests.post(endpoint, json=data, headers=headers)
    if response.status_code == 200:
        return response.json()['link']
    else:
        return False

shorten_url('https://google.com')