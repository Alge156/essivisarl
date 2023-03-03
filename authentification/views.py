from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.http import HttpResponse
from authentification.models import *
from essivisarl.views import *
from essivisarl.urls import *




# Create your views here.

def login_user(request):
    if request.method == "POST":
        username= request.POST['username']
        password= request.POST['password']
        user = Utilisateur.objects.get(username=username)
        #user=authenticate(request, username='username', password='password')
        if user is not None:
            if user.password != password:
                erreur = 'Mauvaise tentative'
                return render(request,'login.html',context={'message':erreur})
            else:
                login(request, user)
                return redirect('index') 
        else:
            messages.success(request, ('Mauvaise tentative'))
            return redirect('login_user')       




    else:
        return render(request,'base.html')
    



def index(request):
      return render(request ,'index.html')
