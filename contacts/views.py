from django.shortcuts import redirect, render
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact
import requests
import json
# Create your views here.
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
        #captcha validation
        #logic serverside for google-recaptcha
        clientkey=reqeust.POST['g-recaptcha-response']
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
            send_mail(
                'Property Listing Enquery',  #subject
                'There has been enquiry for  property' +listing,  #message
                'saurabh.patyal@gmail.com',  #from
                [realtor_email,'saurabh.patyal@gmail.com'], #to
                fail_silently=False
            )
            messages.success(reqeust,'Your message has been sent,we will contact you soon')
            return redirect('/listings/'+listing_id)
        else:
            messages.error(reqeust,'Please fill Captcha')
            return redirect('/listings/'+listing_id)