from math import floor
import discogs_client
from django.contrib.auth.models import User
from django.contrib import messages
from albums.secrets import secret_key
from albums.helpers import validate_rate
from albums.models import Album


class DiscogsRequest:
    """Make request to Discogs API, using Discogs client, and using the
    discogs_client search method, using POST data as input"""

    def __init__(self, request):
        self.request = request
        self.user = User.objects.get(id=request.user.id)
        self.user_input = {"commentary": request.POST['comment'],
                           "rate": validate_rate(request)}
        self.__album = request.POST['album']
        self.__artist = request.POST['artist']
        self.__client = discogs_client.Client('PersonalProjectDiscogs/0.1',
                                              user_token=secret_key)
        self.search = self.__client.search(self.__album, artist=self.__artist, type='release,master')

class DiscogsResponse:
    """Populating database with response values from the Discogs API"""

    def __init__(self, request):
        self.__discogs = DiscogsRequest(request)
        self.__response = self.__discogs.search
        self.success = False
        self.__new_album = True
        self.validate_response()

    def validate_response(self):
        """Checking if response can be used to populate database"""
        if len(self.__response.page(0)) > 0:
            print("FOIII")
            if not Album.objects.filter(discogs_id=self.__response[0].id):
                self.insert_records()
            else:
                album_id = Album.objects.get(discogs_id=self.__response[0].id).id
                if self.__discogs.user.user_opinion.filter(album_id=album_id):
                    messages.warning(self.__discogs.request, 'Album already in catalog')
                    print(messages)
                else:
                    self.__new_album = False
                    self.insert_records()
        else:
            print("FOIIIII")
            messages.warning(self.__discogs.request, 'Album not found')

    def insert_records(self):
        """Populating database with values from response"""
        try:
            fields = {
                "discogs_id": self.__response[0].id,
                "artist": self.__response[0].title.split("-")[0].strip(),
                "album": self.__response[0].title.split("-")[1].strip(),
                "year": self.__response[0].main_release.year,
                "decade": floor(self.__response[0].main_release.year / 10) * 10,
                "country": self.__response[0].main_release.country,
                "genres": self.__response[0].genres[0],
                "styles": self.__response[0].styles[0],
                "label": self.__response[0].main_release.labels[0].name,
                "url": self.__response[0].url,
                "image": self.__response[0].images[0]["uri"]
            }
        except:
            messages.warning(self.__discogs.request,
                             'Unable to find a master release for this album, look in discogs for its master name')
        else:
            self.success = True
            if self.__new_album:
                album = Album.objects.create(**fields)
                album.save()
            else:
                album = Album.objects.get(discogs_id=self.__response[0].id)
            self.__discogs.user.albums.add(album, through_defaults=self.__discogs.user_input)
            messages.warning(self.__discogs.request, f'Album {album.album} from {album.artist} added to your catalog!')