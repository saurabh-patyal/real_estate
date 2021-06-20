from django.shortcuts import render

# Create your views here.

def realtors(request):
    return render(request,'pages/realtor.html')