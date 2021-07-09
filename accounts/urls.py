
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
     path('login', views.login , name='login'),
     # path('register', views.register , name='register'), #########For custom registration############
     path('logout', views.logout , name='logout'),
     path('dashboard', views.dashboard , name='dashboard'),
     path('registeration', views.registeration , name='registeration'),   ########For Built-In registration###
     path('changepassword', views.changeuserpassword , name='changeuserpassword'),
     path('profileEdit', views.profileEdit , name='profileEdit'),
###########################################Forget password urls###############################
     path('password_reset/$', auth_views.PasswordResetView.as_view(), name='password_reset'),
     path('password_reset/done/$', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
     path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
     path('reset/done/$', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]