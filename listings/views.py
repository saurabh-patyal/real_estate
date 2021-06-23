from django.core import paginator
from django.shortcuts import get_object_or_404, render
from .models import Listing
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
from .choices import price_choices,bedroom_choices,state_choices 
# Create your views here.
def listings(request):
    #query to select recent listing which are published
    listings=Listing.objects.order_by('-list_date').filter(is_published=True)

#For showing pagination in listing

    paginator=Paginator(listings,3)
    page=request.GET.get('page')
    paged_listings=paginator.get_page(page)

    context={ 
        'listings': paged_listings
    }
    return render(request,'pages/listings.html', context)


def listing(request,listing_id):
    listing = get_object_or_404(Listing,pk=listing_id)
    context={ 
        'listing': listing
    }

    return render(request,'pages/listing.html',context)


def search(request):
    queryset_list=Listing.objects.order_by('-list_date')

    # searching for 'keyword'
    if 'keywords' in request.GET:
        keywords=request.GET['keywords']
        if keywords:
            queryset_list=queryset_list.filter(description__icontains=keywords)

    # searching for 'city'
    if 'city' in request.GET:
        city=request.GET['city']
        if city:
            queryset_list=queryset_list.filter(city__iexact=city)


    # searching for 'state'
    if 'state' in request.GET:
        state=request.GET['state']
        if state:
            queryset_list=queryset_list.filter(state__iexact=state_choices[state])

    # searching for 'bedrooms'
    if 'bedrooms' in request.GET:
        bedrooms=request.GET['bedrooms']
        if bedrooms:
            queryset_list=queryset_list.filter(bedrooms__lte=bedrooms) #lte is lower than equalto


    #searching for 'price'
    if 'price' in request.GET:
        price=request.GET['price']
        if price >= '1000000':
          queryset_list = queryset_list.filter(price__gte=price)  #lte is greater than equalto
        else:
          queryset_list = queryset_list.filter(price__lte=price)
       



    context = {
        'state_choices':state_choices,
        'bedroom_choices':bedroom_choices,
        'price_choices':price_choices,
        'listings':queryset_list
    }
    return render(request,'pages/search.html',context)