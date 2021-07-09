from django.http import response
from django.shortcuts import redirect, render
from django.contrib import messages
from contacts.models import Contact
from .forms import SignupForm,ChangePasswordForm,ChangeUserProile
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
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



def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request,'You Are Successfully Logout')
        return redirect('home') 

@login_required(login_url='login')
def dashboard(request):
    user_contacts=Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
    context={
        'user_contacts':user_contacts
    }
    return render(request,'accounts/dashboard.html',context)

def registeration(request):
    # return render(request,'accounts/dashboard.html')
    if request.method=='POST':
        subject = "Thank you for registering to our site"
        message = "You have succesfully created an account"
        email_from = settings.EMAIL_HOST_USER    #admin mail from where mail triggered
        email = request.POST['Email']           #email address of registered user
        username=request.POST['username']


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
        if verify:
            fm=SignupForm(request.POST)
            if fm.is_valid():
                fm.save()
                recipient_list = [email,]
                send_mail(subject,message,email_from,recipient_list)

                messages.success(request,'You are Now Successfully Registered')
                return redirect('login')
                
            else:
                fm=SignupForm(request.POST)
                return render(request,'accounts/signup.html',{'form':fm})
        else:
            
            messages.error(request,'Please Fill Captcha First')
            fm=SignupForm()
            return redirect('registeration')
            
    else:
        fm=SignupForm()
        return render(request,'accounts/signup.html',{'form':fm})

@login_required(login_url='login')
def changeuserpassword(request):
    if request.method =='POST':
        fm=ChangePasswordForm(user=request.user,data=request.POST)
        if fm.is_valid():
            fm.save()        
            messages.success(request,'Your Password Is Changed Successfully')
            return redirect('login')
        else:
            fm=ChangePasswordForm(user=request.user,data=request.POST)
            return render(request,'accounts/changepassword.html',{'form':fm})
    else:
        fm=ChangePasswordForm(user=request.user)
        return render(request,'accounts/changepassword.html',{'form':fm})


@login_required(login_url='login')
def profileEdit(request):
    if request.method =='POST':
        fm=ChangeUserProile(request.POST,instance=request.user)
        if fm.is_valid():
            fm.save()        
            messages.success(request,'Your Profile Is Changed Successfully')
            return redirect('profileEdit')
        else:
            fm=ChangeUserProile(request.POST,instance=request.user)
            return render(request,'accounts/userprofile.html',{'form':fm})
    else:
        fm=ChangeUserProile(instance=request.user)
        context={
            'form':fm,
            'name':request.user
        }
        
        return render(request,'accounts/userprofile.html',context)        