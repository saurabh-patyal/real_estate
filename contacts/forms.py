from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    listing_id = forms.CharField(widget=forms.HiddenInput())
    listing = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'disabled': 'true'}),label_suffix='',label='Property Listing')
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),label_suffix='',label='Your Name*',max_length=12)
    Email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email address'}),label_suffix='',label='Email-Address*')
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your phone Number'}),label_suffix='',label='Your Number*',max_length=12)
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your Message'}),label_suffix='',label='Your Message')
    class Meta:
        model=Contact
        fields='__all__'