from django.contrib import admin
from .models import MusicVideo

# Register your models here.


class MusicVideoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'artist', 'location', 'list_date', 'score', 'genre', 'published')
    list_filter = ('artist', 'published')
    search_fields = ('id', 'title', 'artist', 'description', 'list_date', 'location', 'twitter_handle',
                     'instagram_handle', 'genre')
    list_per_page = 30

admin.site.register(MusicVideo, MusicVideoAdmin)