from django.urls import path
from albums.views.views import *
from albums.views.actions import *

urlpatterns = [
    path('', index, name='index'),
    path('add-new-album', album, name='album'),
    path('search', search, name='search'),
    path('find/<int:searchparam>/', find, name='find'),
    path('details', details, name='details'),
    path('delete', delete, name='delete'),
    path('edit', edit, name='edit'),
    path('advanced',advanced,name='advanced'),
    path('stats',stats,name='stats')
]