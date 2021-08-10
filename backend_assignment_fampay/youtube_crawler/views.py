from django.core.paginator import Paginator
from django.shortcuts import render

# Create your views here.
from backend_assignment_fampay.youtube_crawler.models import YoutubeData

def index(request):
    get_videos = YoutubeData.objects.all().order_by(
        "-published_at"
    )  # get latest videos first

    paginator = Paginator(
        get_videos, 10
    )  # added paginator to get videos in 10 on each page

    page = request.GET.get("page")  # get page number from query params

    videos = paginator.get_page(page)

    return render(request, "pages/home.html", {"videos": videos})
