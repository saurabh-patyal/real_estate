from django.shortcuts import render

# Create your views here.
def contacts(reqeust):
    return render(reqeust,'pages/contacts.html')