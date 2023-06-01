from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from youtube_transcript_api import YouTubeTranscriptApi

from utils import log_and_send

YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def get_channel_id_by_name(name, config):
    log_and_send("Attempting to get channel id from " + name + "...")
    try:
        youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                        developerKey=config.get("GOOGLE", "API_KEY"))

        search_response = youtube.search().list(
            q=name,
            type="channel",
            part="id",
            maxResults=1
        ).execute()

        if not search_response["items"]:
            return None

        log_and_send("Successfully got channel id from " + name + ".")

        return search_response["items"][0]["id"]["channelId"]

    except Exception as e:
        log_and_send("Error occurred in get_channel_id_by_name:", e, level="ERROR")
        raise

def get_transcript(video_id):
    log_and_send("Attempting to get transcript from video with id " + video_id + "...")
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        log_and_send("Successfully got transcript from video with id " + video_id + ".")
        return " ".join([segment['text'] for segment in transcript])
    
    except Exception as e:
        log_and_send("Error occurred in get_transcript:", e, level="ERROR")
        raise

def youtube_search(options, config):
    try:
        youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=config.get("GOOGLE", "API_KEY"))

        channel_response = youtube.channels().list(
            id=options['channelId'],
            part='contentDetails'
        ).execute()

        uploads_playlist_id = channel_response["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]

        playlist_response = youtube.playlistItems().list(
            playlistId=uploads_playlist_id,
            part='snippet',
            maxResults=1
        ).execute()

        if playlist_response.get("items"):
            latest_video = playlist_response["items"][0]
            video_title = latest_video["snippet"]["title"]
            video_id = latest_video["snippet"]["resourceId"]["videoId"]
            return video_id

        return None

    except Exception as e:
        log_and_send("Error occurred in youtube_search:", e, level="ERROR")
        raise

def get_latest_video_id(config, channel_id=None, channel_name=None):
    log_and_send(f"Attempting to get latest video id. ChannelID={channel_id}, ChannelName={channel_name}")
    try:
        if channel_id is None:
            channel_id = get_channel_id_by_name(channel_name, config)
        video_id = youtube_search({"channelId": channel_id}, config)
        log_and_send("Successfully got latest video id.")
        return video_id

    except Exception as e:
        log_and_send("Error occurred in get_latest_video_id:", e, level="ERROR")
        raise