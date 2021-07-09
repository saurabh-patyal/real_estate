from django import forms
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm,UserChangeForm
from django.contrib.auth.models import User
from django.forms.fields import CharField
# from django.forms import widget
from django.forms.widgets import EmailInput, TextInput, PasswordInput
class SignupForm(UserCreationForm):
    Email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email address'}),label_suffix='',label='Email-Address*')
    password1= forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'Password'}),label_suffix='',label='Password*',max_length=10,min_length=5)
    password2= forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'Confirm Password'}),label_suffix='',label='Confirm Password*',max_length=10,min_length=5)
    first_name= forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'(Optional)'}),label_suffix='',max_length=10,min_length=1,required=False)
    last_name= forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'(Optional)'}),label_suffix='',max_length=10,min_length=1,required=False)
    username= forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Must be min 3 characters'}),label_suffix='',max_length=10,min_length=3,label='Username*')
    class Meta:
        model = User
        fields=['first_name','last_name','username']
        # No need to give password and confirm pass fields bcz bydefault it comes with UserCreatiionForm

       
       

class ChangePasswordForm(PasswordChangeForm):
    old_password= forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}),label='Your Old Password*',label_suffix='')
    new_password1= forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}),label='Your New Password*',label_suffix='')
    new_password2= forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}),label='Please Confirm*',label_suffix='')
    class Meta:
        model=User
        # fields=['password1','password2']
      


class ChangeUserProile(UserChangeForm):
    password=None
    Email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email address'}),label_suffix='',label='Email-Address*')
    first_name= forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'(Optional)'}),label_suffix='',max_length=10,min_length=1,required=False)
    last_name= forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'(Optional)'}),label_suffix='',max_length=10,min_length=1,required=False)
    username= forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Must be min 3 characters','disabled':'true'}),label_suffix='',max_length=10,min_length=3,label='Username*')
    last_login= forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','disabled':'true'}),label_suffix='',label='You Last Logged At')
    class Meta:
        model=User
        fields=['first_name','last_name','username','Email','last_login']
        