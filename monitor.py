import time
from yt_search import get_newest_video_id, get_transcript
from openai_client import summarize_urban_rescue
import configparser
import bot

main_config = configparser.ConfigParser()

main_config.read("./configs/mainconf.ini")

if __name__ == "__main__":
    
    transcript = get_transcript(get_newest_video_id("TheUrbanRescueRanch", main_config))
    bot.use_bots(main_config, summarize_urban_rescue(transcript, main_config))
    
    """    currentID = ""
    
    while True:
        try:
            newID = get_newest_video_id("TheUrbanRescueRanch", main_config)
            if currentID != newID:
                currentID = newID
                transcript = get_transcript(currentID)
                
                bot.use_bots(main_config, summarize_urban_rescue(transcript, main_config))
                
            time.sleep(1800) # Sleep for 1800 seconds (30 minutes)
        except Exception as e:
            print("An error occurred:", e)"""
