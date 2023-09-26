from django.shortcuts import render
from angeline.forms import ContatoForm, Ex003Form


def index(request):
    return render(request, 'angeline/index.html')

def ex002(request):
    context = {
        'minha_string': 'Olá, Mundo!',
        'meu_inteiro': 123,
        'meu_booleano': True
    }
    return render(request, 'angeline/ex002.html', context)

def qualquer(x):
    return x * 2

def contato(request):  
    # coletar o endereco IP do client (pessoa que acessado esta view)
    ip_address = request.META.get('REMOTE_ADDR')

    if request.method == 'POST':
        metodo = "*POST*"
        form = ContatoForm(request.POST)
        if form.is_valid():
            assunto = form.cleaned_data['assunto']
            assunto = qualquer(assunto)  
            texto = form.cleaned_data['texto']
            email = form.cleaned_data['email']
            idade = int(form.cleaned_data['idade'])
            print(assunto, texto, email, qualquer(idade))
        

    else:
        metodo = "*GET*"
          # Inicializando o formulário com valores padrão
        initial_data = {
            'assunto': 'Tópico Padrão',
            'texto': 'Texto Padrão',
            'email': 'email@exemplo.com',
            'idade': 30,
        }
        form = ContatoForm(initial=initial_data)

    context = { 
        'titulo' : 'historia do passos',
        'passo' : 'passo 1',
        'metodo' : metodo,
        'ip_address' : ip_address,
        'form' : form,
    }
    
    return render(request, 'angeline/contato.html', context)

def ex003(request):
    if request.method == 'POST':
        form = Ex003Form(request.POST)
        if form.is_valid():
            resposta = form.cleaned_data['resposta']
            if resposta == 'A':  # 'A' significa Paris, que é a resposta correta
                msg = "Parabéns, você acertou!"
            else:
                msg = "Ops, tente novamente."
    else:   
        form = Ex003Form(initial={'pergunta': 'Qual é a capital da França?'})
        msg = ""

    context = { 
        'titulo' : 'historia do passos',
        'resposta': "",
        'form' : form,
    }    

    return render(request, 'angeline/ex003.html', context)