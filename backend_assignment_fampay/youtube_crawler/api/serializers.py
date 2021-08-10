from rest_framework import serializers

from backend_assignment_fampay.youtube_crawler.models import YoutubeData


class YouTubeDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = YoutubeData
        fields = ["id", "title", "description", "thumbnail_url", "video_id", "published_at"]
