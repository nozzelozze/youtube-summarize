import requests
from requests_oauthlib import OAuth1

def use_bots(config, text):
    
    if config.getboolean('TWITTER', 'ENABLE'):

        API_KEY = config.get('TWITTER', 'API_KEY')
        API_SECRET_KEY = config.get('TWITTER', 'API_SECRET_KEY')
        ACCESS_TOKEN = config.get('TWITTER', 'ACCESS_TOKEN')
        ACCESS_TOKEN_SECRET = config.get('TWITTER', 'ACCESS_TOKEN_SECRET')
        
        def tweet_text(text):
            url = "https://api.twitter.com/2/tweets"
            auth = OAuth1(API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
            data = {"status": text}
            response = requests.post(url, auth=auth, json={"text": text})
            return response.json()
        
        tweet_text(text)