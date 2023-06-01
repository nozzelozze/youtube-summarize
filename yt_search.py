from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from youtube_transcript_api import YouTubeTranscriptApi

YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"


def get_channel_id_by_name(name, config):
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

    return search_response["items"][0]["id"]["channelId"]

def get_transcript(video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return " ".join([segment['text'] for segment in transcript])
    except Exception as e:
        print("An error occurred:", e)

def youtube_search(options, config):
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

def get_newest_video_id(config, channel_id=None, channel_name=None):
    if channel_id is None and channel_name is None:
        pass     #NADOHIAOISDHAOISHDo
    try:
        if channel_id is None:
            channel_id = get_channel_id_by_name(channel_name, config)
        video_id = youtube_search({"channelId": channel_id}, config)
        return video_id
    except HttpError as e:
        print("An HTTP error %d occurred:\n%s" % (e.resp.status, e.content))