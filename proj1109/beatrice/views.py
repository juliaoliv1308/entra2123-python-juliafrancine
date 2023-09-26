from django.shortcuts import render
from beatrice.forms import Ex001Form

# Create your views here.

def index(request):
    #return HttpResponse("hello world")
    return render(request, 'beatrice/index.html')

def qualquer(valor):
    return valor.upper()
    
def contato(request):
     # coletar o endereco IP do client (pessoa que acessado esta view)
    ip_address = request.META.get('REMOTE_ADDR')

    if request.method == 'POST':
        metodo = "*POST*"
        form = Ex001Form(request.POST)
        if form.is_valid():
            assunto = form.cleaned_data['assunto']
            assunto = qualquer(assunto)
            texto = form.cleaned_data['texto']
            email = form.cleaned_data['email']
            idade = int(form.cleaned_data['idade'])
            print(assunto, texto, email,qualquer(idade)) # O que "qualquer" faz aqui?
        

    else:
        metodo = "*GET*"
        form = Ex001Form()
    # Inicializando o formulário com valores padrão
        initial_data = {
            'assunto': 'Tópico Padrão',
            'texto': 'Texto Padrão',
            'email': 'email@exemplo.com',
            'idade': 30,
        }
        form = Ex001Form(initial=initial_data)

    context = { 
        'titulo' : 'historia do passos',
        'passo' : 'passo 1',
        'metodo' : metodo,
        'ip_address' : ip_address,
        'form' : form,
    }
    return render(request, 'beatrice/contato.html', context)