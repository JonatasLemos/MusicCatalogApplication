from django.contrib import admin
from albums.models import Album

class AlbumList(admin.ModelAdmin):
    # list_display = ('id', 'artist', 'album')
    # list_display_links = ('id','artist','album')
    # search_fields = ('artist','album')
    # list_filter = ('country','decade','styles')
    list_per_page = 10

admin.site.register(Album,AlbumList)