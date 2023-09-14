from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.http import HttpResponse

def index (request):
    return HttpResponse("Olá, mundo!")

def ex002(request):
    context = {
        'minha_string': 'Olá, Mundo!',
        'meu_inteiro': 123,
        'meu_booleano': True
    }
    return render(request, 'angeline/ex002.html', context)