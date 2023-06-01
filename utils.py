import json
import logging
import requests
import traceback

logging.basicConfig(filename='app.log', filemode='a', format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)

WEBHOOK_URL = 'your-webhook-url'

def log_and_send(message, e=None, level="INFO"):
    
    log_func = {
        "DEBUG": logging.debug,
        "INFO": logging.info,
        "WARNING": logging.warning,
        "ERROR": logging.error,
        "CRITICAL": logging.critical
    }
    
    if e is not None:
        message += "\n" + traceback.format_exc()
        
    log_func[level.upper()](message)

    '''     data = {"content": message}
    response = requests.post(WEBHOOK_URL, data=json.dumps(data), headers={"Content-Type": "application/json"})
    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        logging.error(f'Discord webhook failed: {err}') '''