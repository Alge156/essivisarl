from django.http import HttpResponse
from django.shortcuts import render

def home_view(request):
    # return HttpResponse('hello world !')
    return render(request, 'index.html')


def admin_view(request):
    
    # return HttpResponse('contactez-nous')
    return render(request ,'base.html')

   