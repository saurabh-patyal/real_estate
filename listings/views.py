from django.core import paginator
from django.shortcuts import render
from .models import Listing
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
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
    return render(request,'pages/listing.html')


def search(request):
    return render(request,'pages/search.html')