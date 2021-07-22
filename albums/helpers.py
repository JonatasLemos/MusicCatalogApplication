from collections import Counter
from django.core.paginator import Paginator
from django.db.models import Count
from django.contrib import messages
from albums.filters import UserFilter
from albums.models import UserOpinion


def filter_distinct(field,request):
    """Function that returns all distinct values of a given field"""
    userFilter = UserFilter(request)
    user_albums = userFilter.all_albums
    return user_albums.values_list(field, flat=True).distinct().order_by(field)

def pagination(request,all_albums,n_of_pages):
    """Function that paginates a view given a queryset and a breakpoint"""
    paginator = Paginator(all_albums,n_of_pages)
    page = request.GET.get('page')
    return paginator.get_page(page)

def validate_rate(request):
    """Function to validate rate in case no input is given"""
    rate = request.POST['rate']
    try:
        int(rate)
    except:
        rate = None
    return rate

def rate_to_queryset(request, user_albums, case=1):
    """Insert rate values from UserOpinion model into another context: Album queryset"""
    user_opinion = UserOpinion.objects.filter(user_id=request.user.id)
    if case == 1:
        user_opinion = user_opinion.order_by("date").values_list("rate", flat=True)
    elif case == 2:
        ids = user_albums.values_list("id", flat=True)
        user_opinion = user_opinion.filter(album_id__in=ids).order_by("date").values_list("rate", flat=True)
    elif case == 3:
        user_opinion = user_opinion.filter(album_id=request.GET['id'])[0]
        user_rate = user_opinion.rate
        user_comment =user_opinion.commentary
        for i in range(len(user_albums)):
            user_albums[i].rate = user_rate
            user_albums[i].commentary = user_comment
    if not case == 3:
        for i in range(len(user_albums)):
            user_albums[i].rate = user_opinion[i]

def validate_search(request,catalog):
    """Function to validate search in case no input is given or search is invalid"""
    if all(len(request.GET.get(i)) == 0 for i in request.GET.keys()) or len(catalog) == 0:
        messages.warning(request, "No album matched your criteria")
        return False
    return True

def annotate_values(group,category_count,request,is_distinct=False):
    """Function that groups by and aggregates a given field to see its Statistics"""
    userFilter = UserFilter(request)
    user_albums = userFilter.all_albums
    if not is_distinct:
        return user_albums.values(group).annotate(values_count=Count(category_count)).order_by('-values_count')
    values = user_albums.values_list(group, flat=True).distinct(category_count)
    values_dict = {k: v for k, v in sorted(dict(Counter(values)).items(), key=lambda item: item[1],reverse=True)}
    return values_dict
