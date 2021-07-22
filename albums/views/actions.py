from django.shortcuts import render, redirect
from django.contrib import messages
from albums.models import UserOpinion
from albums.discogs import DiscogsResponse
from albums.filters import Filter,AdvancedFilter
from albums.helpers import pagination,validate_search,validate_rate,rate_to_queryset

def search(request):
    if request.method == 'POST':
        result = DiscogsResponse(request)
        if result.success:
            return redirect('index')
    return redirect('album')

def find(request,searchparam):

    if searchparam == 1:
        filter = AdvancedFilter(request)
        user_albums = filter.album.intersection(filter.style,filter.genres,filter.label,
                            filter.year_decade,filter.country).order_by('date')
        rate_to_queryset(request, user_albums, case=2)
    else:
        filter = Filter(request)
        user_albums = filter.album.order_by('date')
        rate_to_queryset(request, user_albums, case=2)

    request_copy = request.GET.copy()
    parameters = request_copy.pop('page', True) and request_copy.urlencode()

    catalog = pagination(request, user_albums, 12)

    album_count = user_albums.count()
    # FORM VALIDATION
    if not validate_search(request,user_albums):
        return redirect('index')

    elements = {
        'catalog':catalog,
        'parameters':parameters,
        'album_count':album_count
    }
    return render(request, 'find.html',elements)

def delete(request):
    if request.method == 'POST':
        UserOpinion.objects.filter(album_id=request.POST['id']).filter(user_id=request.user.id).delete()
        messages.warning(request, "Album successfully deleted")
        return redirect('index')
    return redirect ('index')

def edit(request):
    if request.method == 'POST':
        album_edit = UserOpinion.objects.filter(user_id=request.user.id).get(album_id=request.POST['id'])
        album_edit.commentary = request.POST['commentary']
        album_edit.rate = validate_rate(request)
        album_edit.save()
        messages.warning(request, "Album successfully edited")
        return redirect(request.META.get('HTTP_REFERER'))