from django.test import TestCase, Client
from django.db.models.query import QuerySet
from django.urls import reverse
from albums.tests.fake_data import albums
from albums.models import Album
from django.contrib.auth.models import User


class IndexViewTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        Album.objects.bulk_create([Album(**i) for i in albums])
        self.all_records = Album.objects.all()

    def test_insert_album_in_database(self):
        """Test if fake_data is inserted into database"""
        self.assertEqual(len(self.all_records),len(albums))
