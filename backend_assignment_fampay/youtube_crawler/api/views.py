from django.contrib.auth import get_user_model
from rest_framework import viewsets, filters
from rest_framework.permissions import AllowAny

from .serializers import YouTubeDataSerializer
from ..models import YoutubeData

User = get_user_model()

class YouTubeDataViewSet(viewsets.ModelViewSet):
    serializer_class = YouTubeDataSerializer
    queryset = YoutubeData.objects.all()
    permission_classes = [AllowAny]
    filter_backends = [filters.SearchFilter]
    search_fields = ["title", "description"]
    def get_queryset(self, *args, **kwargs):
        return self.queryset.filter().order_by("-published_at")
