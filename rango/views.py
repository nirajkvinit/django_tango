from django.shortcuts import render
# Create your views here.

from django.http import HttpResponse

def index(request):
    #return HttpResponse("Rango says hey there partner")
    context_dict = {'boldmessage': "Crunch, creamy, cookie, candy, cupcake!"}
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    context_dict = {'boldmessage' : "Hello Django Rango"}
    #return HttpResponse("About Django")
    return render(request, 'rango/about.html', context=context_dict)
