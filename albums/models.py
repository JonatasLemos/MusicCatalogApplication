from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Album(models.Model):

    user = models.ManyToManyField(User,related_name="albums",through="UserOpinion")
    discogs_id = models.IntegerField()
    artist = models.CharField(max_length=75)
    album = models.CharField(max_length=75)
    year = models.IntegerField()
    decade = models.IntegerField()
    country = models.CharField(max_length=35)
    genres = models.CharField(max_length=55)
    styles = models.CharField(max_length=55)
    label = models.CharField(max_length=60)
    url = models.URLField(max_length=400)
    image = models.URLField(max_length=400)
    date = models.DateTimeField(default=timezone.now)

class UserOpinion(models.Model):
    class Rate(models.IntegerChoices):
        TERRIBLE = 1
        BAD = 2
        AVERAGE = 3
        GOOD = 4
        EXCELLENT = 5

    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="user_opinion")
    album = models.ForeignKey(Album, on_delete=models.CASCADE,related_name="user_opinion")
    rate = models.IntegerField(choices=Rate.choices, null=True)
    commentary = models.TextField(blank=True)
    date = models.DateTimeField(default=timezone.now)