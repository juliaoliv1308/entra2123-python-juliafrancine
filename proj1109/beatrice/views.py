from django.shortcuts import render

# Create your views here.

def index(request):
    #return HttpResponse("hello world")
    return render(request, 'beatrice/index.html')