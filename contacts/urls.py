
from django.urls import path
from . import views

urlpatterns = [
     path('', views.contacts , name='contacts'),
     # path('inquiry', views.inquiry , name='inquiry'),
     
]