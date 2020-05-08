from django.db import models
from datetime import datetime

# Create your models here.


class MusicVideo(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=50)
    score = models.IntegerField(default=0)
    # City & State:
    location = models.CharField(max_length=30)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    twitter_handle = models.CharField(max_length=15, blank=True)
    instagram_handle = models.CharField(max_length=30, blank=True)
    fb_page = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=5000, blank=True)
    genre = models.CharField(max_length=30, blank=True)
    published = models.BooleanField(default=True)
    video = models.FileField(upload_to='videos/%Y/%m/%d/', blank=True)

    def __str__(self):
        return self.title
