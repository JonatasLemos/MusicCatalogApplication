from django.contrib.auth.models import User
from django.db.models import Q
from albums.models import Album

class UserFilter:
    """Filtering albums from a given user"""
    def __init__(self, request):
        self.request = request

    @property
    def all_albums(self):
        user = User.objects.get(id=self.request.user.id)
        ids = user.user_opinion.all().values_list("album_id",flat=True)
        return Album.objects.filter(pk__in=ids)


class Filter:
    """Filter used in simple search (only album and artist)"""
    def __init__(self, request):
        self.request = request
        self.user_filter = UserFilter(request)
        self.albums = self.user_filter.all_albums

    @property
    def album(self):
        title = self.request.GET['album']
        return self.albums.filter(Q(album__icontains=title) | Q(artist__icontains=title))


class AdvancedFilter(Filter):
    """Filter used in advanced search"""
    @property
    def style(self):
        return self.albums.filter(styles__icontains=self.request.GET['style'])

    @property
    def genres(self):
        return self.albums.filter(genres__icontains=self.request.GET['genres'])

    @property
    def label(self):
        return self.albums.filter(label__icontains=self.request.GET['label'])

    @property
    def country(self):
        return self.albums.filter(country__icontains=self.request.GET['country'])

    @property
    def year_decade(self):
        if len(self.request.GET['year']) == 0:
            return self.albums.filter(decade__icontains=self.request.GET['decade'])
        if len(self.request.GET['decade']) == 0:
            return self.albums.filter(year__icontains=self.request.GET['year'])
        return self.albums.filter(Q(year__icontains=self.request.GET['year']) |
                                      Q(decade__icontains=self.request.GET['decade']))
