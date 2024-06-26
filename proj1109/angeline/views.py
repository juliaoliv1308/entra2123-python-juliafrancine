from django.shortcuts import render, redirect
from angeline.forms import ContatoForm, Ex003Form,  Ex007Form
from datetime import datetime
from .compras import compras

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

def ex004(request):
    questions = {
    '1': {
        'Q': 'Qual a capital da França',
        'A': 'Blumenau',
        'B': 'Brusque',
        'C': 'Floripa',
        'D': 'Paris',
        'R': 'D'
    },
    '2': {
        'Q': 'Qual é o maior planeta do sistema solar?',
        'A': 'Marte',
        'B': 'Vênus',
        'C': 'Terra',
        'D': 'Júpiter',
        'R': 'D'
    },
    '3': {
        'Q': 'Quem escreveu a peça "Romeu e Julieta"?',
        'A': 'William Shakespeare',
        'B': 'Charles Dickens',
        'C': 'Jane Austen',
        'D': 'F. Scott Fitzgerald',
        'R': 'A'
    },
    '4': {
        'Q': 'Qual é o elemento químico mais abundante na crosta terrestre?',
        'A': 'Oxigênio',
        'B': 'Ferro',
        'C': 'Carbono',
        'D': 'Silício',
        'R': 'A'
    },
    '5': {
        'Q': 'Qual é a capital do Japão?',
        'A': 'Pequim',
        'B': 'Tóquio',
        'C': 'Seul',
        'D': 'Bangkok',
        'R': 'B'
    }
}
    print(questions)
    for chave in questions.keys():
        print(chave)

    context = {
        'titulo': 'Dicionário',
        'questions': questions,
    }

    return render(request, 'angeline/ex004.html', context)



def calc_vencimento(data):
    delta = data - datetime.now()
    return delta.days

def ex005(request):
    produtos = {
    1: {
        'nome': 'Arroz',
        'fornecedor_id': 1,
        'categoria_id': 1,
        'localizacao': 'Prateleira A1',
        'saldo_id': 1,
        'data_validade_id': datetime(2024,8,4),
        'dias_vencidos_id': calc_vencimento(datetime(2024,8,4))

    },
    2: {
        'nome': 'Televisão',
        'fornecedor_id': 2,
        'categoria_id': 2,
        'localizacao': 'Setor Eletrônicos',
        'saldo_id': 2,
        'data_validade_id': datetime(2023,11,13),
        'dias_vencidos_id': calc_vencimento(datetime(2023,11,13))
        


    },
    3: {
        'nome': 'Macarrão',
        'fornecedor_id': 1,
        'categoria_id': 1,
        'localizacao': 'Prateleira B2',
        'saldo_id': 3,
        'data_validade_id': datetime(2023,9,15),
        'dias_vencidos_id': calc_vencimento(datetime(2023,9,15))
    },
    4: {
        'nome': 'Smartphone',
        'fornecedor_id': 2,
        'categoria_id': 2,
        'localizacao': 'Setor Eletrônicos',
        'saldo_id': 4,
        'data_validade_id':  datetime(2023,10,3),
        'dias_vencidos_id': calc_vencimento(datetime(2023,10,3))
    },
    5: {
        'nome': 'Leite',
        'fornecedor_id': 3,
        'categoria_id': 1,
        'localizacao': 'Prateleira C3',
        'saldo_id': 5,
        'data_validade_id': datetime(2023,11,10),
        'dias_vencidos_id': calc_vencimento(datetime(2023,11,10))
    }
    }
# Dicionário de fornecedores 
    fornecedores = {
    1: {
        'nome': 'Alimentos do Sul',
        'localizacao': 'Rio Grande do Sul'
    },
    2: {
        'nome': 'Tech Electronics',
        'localizacao': 'São Paulo'
    },
    3: {
        'nome': 'Laticínios ABC',
        'localizacao': 'Minas Gerais'
    },
    4: {
        'nome': 'Fashion Style',
        'localizacao': 'Rio de Janeiro'
    },
    5: {
        'nome': 'Tech Pro',
        'localizacao': 'São Paulo'
    },
}

# Dicionário de categorias 
    categorias = {
    1: {
        'nome': 'Alimentos',
        'texto' : 'blablabla'
    },
    2: {
        'nome': 'Eletrônicos'
    },
    3: {
        'nome': 'Vestuário'
    },
    4: {
        'nome': 'Limpeza'
    },
    5: {
        'nome': 'Móveis'
    },
    
}
    saldo = {
    1: {
  
        'nome':'70'
    },
    2: {
        'nome': '60'
    },
    3: {
        'nome': '50'
    },
    4: {
        'nome': '40'
    },
    5: {
        'nome': '30'
    },
    }

    supermercado = {}
    for produto_id, produto_info in produtos.items():
        fornecedor_id = produto_info['fornecedor_id']
        categoria_id = produto_info['categoria_id']
        saldo_id = produto_info['saldo_id']
        vencimento_id = produto_info['dias_vencidos_id']
        validade_id = produto_info['data_validade_id']
        fornecedor_nome = fornecedores.get(fornecedor_id, {}).get ("nome", "desconhecido")
        categoria_nome = categorias.get(categoria_id, {}).get ("nome", "desconhecido")
        saldo_nome = saldo.get(saldo_id, {}).get ("nome", "desconhecido")

        supermercado[produto_id] = {
            'nome_produto': produto_info['nome'],
            'nome_fornecedor': fornecedor_nome,
            'nome_categoria': categoria_nome,
            'nome_saldo': saldo_nome,
            'nome_validade': validade_id,
            'nome_vencimento': vencimento_id,
        }

    return render(request, 'angeline/ex005.html', {"supermercado":supermercado})


def ex007(request):
    if request.method == 'POST':                                                #se request é post
        form = Ex007Form(request.POST)                                          #chama o forms para a var form

        if form.is_valid():                                                     #se esse forms existir
            id_produto = form.cleaned_data['id_produto']                        #extrai o valor do campo 'id_produto' do formulario apos a validacao e armazena em id_produto
            nome_produto = form.cleaned_data['nome_produto']                    #extrai o valor do campo 'nome_produto' do forms apos a validacao e armazena em nome_produto
            qnt_produto = form.cleaned_data['qnt_produto']                      #extrai o valor do campo 'qnt_produto' do forms apos a validacao e armazena em qnt_produto

            compras[id_produto] = {'nome': nome_produto, 'qnt': qnt_produto}    #cria um registro na estrutura de dados compras usando o id_produto 
                                                                                #como chave e um dicionário contendo 'nome' e 'qnt' como valores associados 
                                                                                #a essa chave

    else:                                                                       #se nao é post
        form = Ex007Form()                                                      #instancia o forms com os dados iniciais
    
    context = {                                                                 #armazena dados que serão passados para o template
    'lista_de_compras': compras, 
    'form': form   
    }
    
    return render(request, 'angeline/ex007.html', context )                   #renderiza o template


def ex007_add(request):
    if request.method == 'POST':
        form = Ex007Form(request.POST)
        if form.is_valid():
            nome_produto = form.cleaned_data['nome_produto']
            qnt_produto = form.cleaned_data['qnt_produto']

            proximo_id = str(len(compras) + 1)                                  #Calcula o próximo ID para o novo registro, adicionando 1 ao 
                                                                                #comprimento atual da estrutura de dados compras

            compras[proximo_id] = {'nome': nome_produto, 'qnt': qnt_produto}    #adiciona um novo item à lista de compras

            return redirect('angeline:ex007')                                 #redireciona o usuário para a view 'ex007' após a 
                                                                                #adição bem-sucedida do item à lista de compras

    else:
        proximo_id = str(len(compras) + 1)
        form = Ex007Form(initial={'id_produto': proximo_id})                    #exibir um valor preenchido no campo ID do produto no 
                                                                                #formulário quando a página é acessada pela primeira vez

    return render(request, 'angeline/ex007_add.html', {'form': form})



def ex007_remove(request, id_produto):
    if request.method == 'POST':
        if id_produto in compras:                                               #verifica se o id_produto existe na estrutura de dados compras
            del compras[id_produto]                                             #deleta do dic compras o id_produto que o user seleciona
    return redirect('angeline:ex007')










