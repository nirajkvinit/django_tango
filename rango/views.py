from django.shortcuts import render
# Create your views here.

from django.http import HttpResponse

def index(request):
    #return HttpResponse("Rango says hey there partner")
    context_dict = {'boldmessage': "Crunch, creamy, cookie, candy, cupcake!"}
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    return HttpResponse("About Django")
