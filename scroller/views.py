from django.shortcuts import render
from .models import MusicVideo

# Create your views here.
def index(request):
    videos = MusicVideo.objects.all().order_by('-list_date')
    context = {
        "videos": videos
    }
    return render(request, "scroller/index.html", context)
