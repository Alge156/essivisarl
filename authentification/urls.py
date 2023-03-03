 # from django.contrib import admin
from django.urls import path
from essivisarl import views
from . import views




urlpatterns = [
    path('login_user/',views.login_user,name='login_user'),
    path('index/',views.index, name='index')
    
]
 