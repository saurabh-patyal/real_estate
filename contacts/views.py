from django.shortcuts import redirect, render
from django.contrib import messages
from django.core.mail import send_mail
from requests.api import request
from .models import Contact
from .forms import ContactForm
import requests
import json
# Create your views here Contact with no validations OR normal form with captcha.
def contacts(reqeust):
    if reqeust.method=='POST':
        listing_id=reqeust.POST['listing_id']
        listing=reqeust.POST['listing']
        name=reqeust.POST['name']
        email=reqeust.POST['email']
        phone=reqeust.POST['phone']
        message=reqeust.POST['message']
        user_id=reqeust.POST['user_id']
        realtor_email=reqeust.POST['realtor_email']
        clientkey=reqeust.POST['g-recaptcha-response']
        
        #captcha validation
        #logic serverside for google-recaptcha
        
        secretkey='6LfX_VYbAAAAAGavFnBkxwVW0V9LMeUH-z64eYpW'
        captchadata={
            'secret': secretkey,               # NOTE In this dictionary Keys should be same as 'secret' & 'response'
            'response': clientkey
        }

        #now make api request to google from its Api url
        r=requests.post('https://www.google.com/recaptcha/api/siteverify',data=captchadata)
        response=json.loads(r.text)    # this is for converting json response to python dictionary
        verify=response['success']
        if verify:
            contact=Contact(listing=listing, listing_id=listing_id, name=name,  email=email, phone=phone, message=message, user_id=user_id)
            contact.save()
            
            messages.success(reqeust,'Your message has been sent,we will contact you soon')
            return redirect('/listings/'+listing_id)
        else:
            messages.error(reqeust,'Please fill Captcha')
            return redirect('/listings/'+listing_id)



        





# CContactview with validations OR with Build-In Modelform with captchaNOTE:The issue is passing modal in popup window:solution is o click modal button automatically with javascript.
# def inquiry(reqeust):
#     if reqeust.method=='POST':
#         listing_id=reqeust.POST['listing_id']
        
#         clientkey=reqeust.POST['g-recaptcha-response']
#         secretkey='6LfX_VYbAAAAAGavFnBkxwVW0V9LMeUH-z64eYpW'
#         captchadata={
#             'secret': secretkey,               
#             'response': clientkey
#         }

        

#         r=requests.post('https://www.google.com/recaptcha/api/siteverify',data=captchadata)
#         response=json.loads(r.text)    
#         verify=response['success']
#         if verify:
        
#            contact=ContactForm(request.POST)
#            if contact.is_valid():
#                 contact.save()
#                 messages.success(reqeust,'Your message has been sent,we will contact you soon')
#                 return redirect('/listings/'+listing_id,{'contact':contact})
#         else:
#             messages.error(reqeust,'Please fill Captcha')
#             return redirect('/listings/'+listing_id)
#     else:
#         contact=ContactForm()
#         return render(request,'listing.html',{'contact':'contact'})