import requests
from requests_oauthlib import OAuth1
from utils import log_and_send

def use_bots(config, text):
    
    if config.getboolean('TWITTER', 'ENABLE'):
        API_KEY = config.get('TWITTER', 'API_KEY')
        API_SECRET_KEY = config.get('TWITTER', 'API_SECRET_KEY')
        ACCESS_TOKEN = config.get('TWITTER', 'ACCESS_TOKEN')
        ACCESS_TOKEN_SECRET = config.get('TWITTER', 'ACCESS_TOKEN_SECRET')

        def tweet_text(text):
            url = "https://api.twitter.com/2/tweets"
            auth = OAuth1(API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
            response = requests.post(url, auth=auth, json={"text": text})
            return response

        try:
            response = tweet_text(text)
            if 200 <= response.status_code < 300:
                log_and_send(f"Received status code: {response.status_code}")
                if 'errors' in response.json(): 
                    for error in response.json()['errors']:
                        log_and_send(f"Error from Twitter API: {error['message']}", level="ERROR")  # Log the error message
                else:
                    log_and_send(f"Request to Twitter API failed: {response.json()}", level="ERROR") 
            else:
                log_and_send("Tweeted: " + text)
                log_and_send("Twitter API response: " + str(response.json()))
        except Exception as e:
            log_and_send("Error occurred while tweeting:", e, level="ERROR")