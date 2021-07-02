
from django.urls import path
from . import views

urlpatterns = [
     path('login', views.login , name='login'),
     # path('register', views.register , name='register'), #########For custom registration############
     path('logout', views.logout , name='logout'),
     path('dashboard', views.dashboard , name='dashboard'),
     path('registeration', views.registeration , name='registeration'),   ########For Built-In registration###
     path('changepassword', views.changeuserpassword , name='changeuserpassword'),
     path('profileEdit', views.profileEdit , name='profileEdit'),
]