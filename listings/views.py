from django.shortcuts import render

# Create your views here.
def listings(request):
    return render(request,'pages/listings.html')


def listing(request):
    return render(request,'pages/listing.html')


def search(request):
    return render(request,'pages/search.html')