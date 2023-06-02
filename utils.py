import json
import logging
import requests
import traceback
import configparser
import datetime

logging.basicConfig(filename='app.log', filemode='a', format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)

config = configparser.ConfigParser()
config.read("./configs/mainconf.ini")
WEBHOOK_URL = config.get("DISCORD_LOG", "WEBHOOK")
DIS_LOG_DEBUG = config.getboolean("DISCORD_LOG", "DEBUG")
DIS_LOG_INFO = config.getboolean("DISCORD_LOG", "INFO")
DIS_LOG_WARNING = config.getboolean("DISCORD_LOG", "WARNING")
DIS_LOG_ERROR = config.getboolean("DISCORD_LOG", "ERROR")
DIS_LOG_CRITICAL = config.getboolean("DISCORD_LOG", "CRITICAL")

def log_and_send(message, e=None, level="INFO"):
    
    log_func = {
        "DEBUG": logging.debug,
        "INFO": logging.info,
        "WARNING": logging.warning,
        "ERROR": logging.error,
        "CRITICAL": logging.critical
    }
    level = level.upper()
    
    if e is not None:
        message += "\n" + traceback.format_exc()
        
    log_func[level](message)

    if WEBHOOK_URL:
        if (level == "DEBUG" and DIS_LOG_DEBUG) or \
           (level == "INFO" and DIS_LOG_INFO) or \
           (level == "WARNING" and DIS_LOG_WARNING) or \
           (level == "ERROR" and DIS_LOG_ERROR) or \
           (level == "CRITICAL" and DIS_LOG_CRITICAL):
               
            color_code = {
                "DEBUG": 3447003,  # Blue
                "INFO": 3066993,  # Green
                "WARNING": 15105570,  # Orange
                "ERROR": 15158332,  # Red
                "CRITICAL": 16711680  # Darker Red
            }

            data = {
                "embeds": [{
                    "description": message,
                    "color": color_code.get(level, 0),
                    "footer": {
                        "text": f"Log Level: {level}"
                    },
                    "timestamp": datetime.datetime.now().isoformat()
                }]
            }
            
            response = requests.post(WEBHOOK_URL, data=json.dumps(data), headers={"Content-Type": "application/json"})
            try:
                response.raise_for_status()
            except requests.exceptions.HTTPError as err:
                logging.error(f'Discord webhook failed: {err}')