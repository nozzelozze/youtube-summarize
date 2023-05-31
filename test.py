import configparser
import requests
from requests_oauthlib import OAuth1

config = configparser.ConfigParser()

config.read("./configs/mainconf.ini")

API_KEY = config.get('TWITTER', 'API_KEY')
API_SECRET_KEY = config.get('TWITTER', 'API_SECRET_KEY')
ACCESS_TOKEN = config.get('TWITTER', 'ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = config.get('TWITTER', 'ACCESS_TOKEN_SECRET')

# Define the URL of the Twitter API
url = "https://api.twitter.com/2/tweets"

# Create the OAuth1 authentication object
auth = OAuth1(API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# Main function to post the tweet
def tweet_fact():
    # Get a random fact

    # Make the POST request to the Twitter API to post the tweet
    response = requests.post(url, auth=auth, json={"text": "quzi"})

    # Print the response from the Twitter API
    print(response.json())

# Call the function to post the tweet
tweet_fact()