import requests
from bs4 import BeautifulSoup
import json

def get_views_by_url(url: str):
    if not url:
        return None

    page_data = requests.get(url)
    parsed_data = BeautifulSoup(page_data.text, 'html.parser')
    body = parsed_data.find('body')
    script = body.find('script')
    script_content = script.string
    script_content_json = script_content.replace('var ytInitialPlayerResponse = ', '')[:-1]
    yt_data_json = json.loads(script_content_json)
    return yt_data_json.get('videoDetails', {}).get('viewCount')    
