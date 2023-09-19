from django.shortcuts import render
from beatrice.forms import Ex001Form

# Create your views here.

def index(request):
    #return HttpResponse("hello world")
    return render(request, 'beatrice/index.html')

def ex001(request):
     
    ip_address = request.META.get('REMOTE_ADDR')

    if request.method == 'POST':
        metodo = "*POST*"
        form = Ex001Form(request.POST)
        if form.is_valid():
            assunto = form.cleaned_data['assunto']
            texto = form.cleaned_data['texto']
            email = form.cleaned_data['email']
            idade = int(form.cleaned_data['idade'])
            print(assunto, texto, email, qualquer(idade))
        

    else:
        metodo = "*GET*"
        form = Ex001Form()

    context = { 
        'titulo' : 'historia do passos',
        'passo' : 'passo 1',
        'metodo' : metodo,
        'ip_address' : ip_address,
        'form' : form,
    }
    return render(request, 'beatrice/ex001.html', context)