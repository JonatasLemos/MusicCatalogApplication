from django.shortcuts import render, redirect
from albums.models import Album,UserOpinion
from albums.helpers import pagination,annotate_values,filter_distinct,rate_to_queryset
from albums.filters import UserFilter
from itertools import chain
from django.contrib.auth.models import User

def album(request):
    rates = UserOpinion.Rate.choices
    elements = {
        "rates":rates
    }
    return render(request,'album.html',elements)

def index(request):
    if request.user.is_authenticated:
        userFilter = UserFilter(request)
        user_albums = userFilter.all_albums.order_by("date")
        rate_to_queryset(request, user_albums, case=1)
        album_count = user_albums.count()
        catalog = pagination(request,user_albums,9)
        elements = {
            'catalog':catalog,
            'album_count':album_count,
        }
        return render(request, 'index.html',elements)
    return render(request,'index.html')

def stats(request):
    elements = {
        'fields':{
        'country': annotate_values('country','album',request),
        'artist': annotate_values('artist','album',request),
        'decade':annotate_values('decade','album',request),
        'style': annotate_values('styles','album',request),
        'genres': annotate_values('genres','album',request)
        },
        'artists_per_country':annotate_values('country','artist',request,is_distinct=True)
    }
    return render(request, 'stats.html',elements)

def advanced(request):
    style = filter_distinct('styles',request)
    genres = filter_distinct('genres',request)
    year = filter_distinct('year',request)
    decade = filter_distinct('decade',request)
    label = filter_distinct('label',request)
    country = filter_distinct('country',request)
    elements = {'filters': {
            'style': style, 'genres': genres,'year': year,
            'decade': decade, 'label': label,'country':country}
    }
    return render(request, 'advanced.html',elements)

def details(request):
    rates = UserOpinion.Rate.choices
    if request.method == 'GET':
        if 'id' in request.GET:
            user_albums = Album.objects.filter(id=request.GET['id'])
            rate_to_queryset(request,user_albums,case=3)
            elements = {
                'user_albums':user_albums,
                'rates':rates,
            }
            return render(request, 'details.html',elements)
        return redirect('index')

