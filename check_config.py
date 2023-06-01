from utils import log_and_send


def check(config):
    
    required_keys = [
    ("GOOGLE", "API_KEY"),
    ("OPENAI", "API_KEY"),
    ("PROMPT", "DESCRIPTION"),
    ("TWITTER", "ENABLE"),
    ]
    
    for section, key in required_keys:
        if not config.get(section, key):
            log_and_send(f"Configuration key {key} in section {section} is not set", level="ERROR")
            raise RuntimeError(f"Configuration key {key} in section {section} is not set")

    if not config.get("YOUTUBE", "CHANNEL_ID") and not config.get("YOUTUBE", "CHANNEL_NAME"):
        log_and_send("Neither YOUTUBE CHANNEL_ID nor CHANNEL_NAME is set", level="ERROR")
        raise RuntimeError("Neither YOUTUBE CHANNEL_ID nor CHANNEL_NAME is set")

    try:
        if config.getboolean("TWITTER", "ENABLE"):
            required_twitter_keys = [
                ("TWITTER", "API_KEY"),
                ("TWITTER", "API_SECRET_KEY"),
                ("TWITTER", "ACCESS_TOKEN"),
                ("TWITTER", "ACCESS_TOKEN_SECRET"),
            ]

            for section, key in required_twitter_keys:
                if not config.get(section, key):
                    log_and_send(f"Configuration key {key} in section {section} is not set but TWITTER is enabled", level="ERROR")
                    raise RuntimeError(f"Configuration key {key} in section {section} is not set but TWITTER is enabled")
                
    except ValueError as e:
        log_and_send(f"Configuration key ENABLE in section TWITTER is not a valid boolean value: {config.get('TWITTER', 'ENABLE')}", level="ERROR")
        raise RuntimeError(f"Configuration key ENABLE in section TWITTER is not a valid boolean value: {config.get('TWITTER', 'ENABLE')}")