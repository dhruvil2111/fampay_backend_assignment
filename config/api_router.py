from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from backend_assignment_fampay.users.api.views import UserViewSet
from backend_assignment_fampay.youtube_crawler.api.views import YouTubeDataViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("videos", YouTubeDataViewSet)

app_name = "api"
urlpatterns = router.urls
