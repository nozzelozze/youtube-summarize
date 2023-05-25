import time
from yt_search import get_newest_video_id, get_transcript
from openai_client import summarize_urban_rescue
import configparser

main_config = configparser.ConfigParser()

main_config.read("./configs/mainconf.ini")

def do_stuff():
    print("Bom! Done:D:D:D")

if __name__ == "__main__":
    
    currentID = ""
    
    while True:
        try:
            newID = get_newest_video_id("TheUrbanRescueRanch", main_config)
            if currentID != newID:
                currentID = newID
                transcript = get_transcript(currentID)
                do_stuff()
            time.sleep(1800) # Sleep for 1800 seconds (30 minutes)
        except Exception as e:
            print("An error occurred:", e)
