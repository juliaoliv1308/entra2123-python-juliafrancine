from django.shortcuts import render

# Create your views here.

def index(request):
    #return HttpResponse("hello world")
    return render(request, 'beatrice/index.html')

def ex001(request):
    #return HttpResponse("hello world")
    return render(request, 'beatrice/ex001.html')