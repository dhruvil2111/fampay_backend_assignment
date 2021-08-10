import uuid

from django.db import models

# Create your models here.
class YoutubeData(models.Model):
    id = models.UUIDField(
        primary_key=True, unique=True, editable=False, default=uuid.uuid4, db_index=True
    )
    title = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    published_at = models.DateTimeField(null=True, blank=True)
    thumbnail_url = models.URLField(max_length=200)
    video_id = models.CharField(max_length=200, db_index=True)
    def __str__(self):
        return self.title
    @property
    def video_url(self):
        return " ".join(["https://www.youtube.com/watch?v=", self.video_id])
