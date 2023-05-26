import tweepy

def use_bots(config, message):
    
    # check if discord
    
    # check if twitter
    if config.getboolean("TWITTER", "ENABLE"):
        
        auth = tweepy.OAuthHandler(config.get("TWITTER", "API_KEY"), config.get("TWITTER", "API_SECRET_KEY"))
        auth.set_access_token(config.get("TWITTER", "ACCESS_TOKEN"), config.get("TWITTER", "ACCESS_TOKEN_SECRET"))

        api = tweepy.API(auth)
        
        api.update_status(message)