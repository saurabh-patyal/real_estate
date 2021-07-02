from django.http import response
from django.shortcuts import redirect, render, HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from contacts.models import Contact
from django.contrib import auth
from django.contrib.auth import authenticate, login
import requests
import json
# Create your views here.
def login(request):
   if request.method == 'POST':
     username = request.POST['username']
     password = request.POST['password']
     #logic serverside for google-recaptcha
     clientkey=request.POST['g-recaptcha-response']
     secretkey='6LfX_VYbAAAAAGavFnBkxwVW0V9LMeUH-z64eYpW'
     captchadata={
         'secret': secretkey,               # NOTE In this dictionary Keys should be same as 'secret' & 'response'
         'response': clientkey
     }

     #now make api request to google from its Api url
     r=requests.post('https://www.google.com/recaptcha/api/siteverify',data=captchadata)
     response=json.loads(r.text)    # this is for converting json response to python dictionary
     verify=response['success']
    
    #  if verify:
    #      return HttpResponse('<script> alert("success");</script>')
    #  else:
    #      return HttpResponse('<script> alert("Unverified");</script>')    
     if verify:
        #check username & password of POST request with database username & password
        user = auth.authenticate(username=username,password=password)

        #check if  authenticated user exist in database
        if user is not None:
            auth.login(request,user)
            messages.success(request,'Successfully LoggedIn')
            return redirect('dashboard')
        else:
            messages.error(request,'Invalid Credentials')
            return redirect('login')
     else:  
        messages.error(request,'Please complete captcha')
        return redirect('login')   
    

   else:    
        return render(request,'accounts/login.html')


def register(request):
    if request.method == 'POST':
     #getting form value
     first_name=request.POST['first_name']
     last_name=request.POST['last_name']
     username=request.POST['username']
     email=request.POST['email']
     password=request.POST['password']
     password2=request.POST['password2']
    #logic serverside for google-recaptcha
     clientkey=request.POST['g-recaptcha-response']
     secretkey='6LfX_VYbAAAAAGavFnBkxwVW0V9LMeUH-z64eYpW'
     captchadata={
         'secret': secretkey,               # NOTE In this dictionary Keys should be same as 'secret' & 'response'
         'response': clientkey
     }

     #now make api request to google from its Api url
     r=requests.post('https://www.google.com/recaptcha/api/siteverify',data=captchadata)
     response=json.loads(r.text)    # this is for converting json response to python dictionary
     verify=response['success']
     #validations
     #check password &confirm password match
     if password == password2:
         #check username exist in database
         if User.objects.filter(username=username).exists():
             messages.error(request,'The username Already Taken')
             return redirect('register')
         else:
             if User.objects.filter(email=email).exists():
                messages.error(request,'The email Already Taken')
                return redirect('register')
             else:
                 #register entries to db
                 user=User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                 user.save()
                 #auto login code after signup
                 # auth.login(request,user)   
                 #messages.success(request,'You are Now Successfully Loggedin')
                 #return redirect('/')

                 #redirect to login page after registered
                 messages.success(request,'You are Now Successfully Registered')
                 return redirect('login')
     else:
         messages.error(request,'password & confirm password do match')
         return redirect('register')
        
    else:    
     return render(request,'accounts/register.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request,'You Are Successfully Logout')
        return redirect('home') 


def dashboard(request):
    user_contacts=Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
    context={
        'user_contacts':user_contacts
    }
    return render(request,'accounts/dashboard.html',context)