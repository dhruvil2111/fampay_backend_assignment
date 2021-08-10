import datetime

import requests

from backend_assignment_fampay.youtube_crawler.models import YoutubeData
from config import celery_app

@celery_app.task()
def populate_database_youtube_videos():
    """A Celery task to populate database every 10 seconds asynchronously with youtube videos fetched from Youtube
    Data API."""
    api_keys = get_all_keys()  # get all api keys for youtube
    verified_key = None
    data = None
    youtube_search_api = (
        "https://www.googleapis.com/youtube/v3/search/"  # Youtube search api endpoint
    )
    next_page_token = ""
    existing_vid_ids = YoutubeData.objects.filter().values_list("video_id", flat=True)
    fetched_vid_ids = set()

    for api_key in api_keys:
        publishedAfter = str(datetime.datetime(2020, 1, 1).date()) + "T00:00:00Z"
        youtube_search_api_params = {
            "part": "snippet",
            "maxResults": 50,
            "q": "apple",
            "key": api_key,
            "type": "video",
            "order": "date",
            "publishedAfter": publishedAfter,
            "pageToken": next_page_token,
        }
        response = requests.get(youtube_search_api, params=youtube_search_api_params)
        if str(response) != "<Response [403]>":
            verified_key = api_key
            data = response.json()

        if verified_key is None or data is None:
            return "All keys are expired"
        next_page_token = data["nextPageToken"]

        for video in data["items"]:
            try:
                fetched_vid_ids.add(video["id"]["videoId"])
            except Exception as e:
                print(e)

        bulk_youtube_videos_objs = []

        for fetched_videos in data["items"]:
            try:
                video_id = fetched_videos["id"]["videoId"]

                if video_id not in existing_vid_ids:
                    video_id = fetched_videos["id"]["videoId"]
                    snippet = fetched_videos["snippet"]
                    title = snippet["title"]
                    published_at = snippet["publishedAt"]
                    description = snippet["description"]
                    thumbnail_url = snippet["thumbnails"]["default"]["url"]

                    bulk_youtube_videos_objs.append(
                        YoutubeData(
                            title=title,
                            description=description,
                            published_at=published_at,
                            thumbnail_url=thumbnail_url,
                            video_id=video_id,
                        )
                    )
            except Exception as e:
                print(e)

        YoutubeData.objects.bulk_create(bulk_youtube_videos_objs)

def get_all_keys():
    api_keys_file = open(
        ".envs/.local/.youtube_api_keys"
    )  # read api keys file to fetch keys
    api_keys = api_keys_file.read().split(
        "\n"
    )  # splitting files by new lines and get array of api keys
    return api_keys  # return array of api keys
