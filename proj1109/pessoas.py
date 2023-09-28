# Dicionário de pessoas com ID único, nomes brasileiros e sobrenomes italiano e alemão.
pessoas = {
    1: {'nome': 'Lucas Ferrari', 'cep': '89000'},
    2: {'nome': 'Rafaela Weiss', 'cep': '89010'},
    3: {'nome': 'Ana Rossi', 'cep': '89020'},
    4: {'nome': 'Carlos Müller', 'cep': '89030'},
    5: {'nome': 'Fernanda Schmidt', 'cep': '89040'},
    6: {'nome': 'Gabriela Bianchi', 'cep': '89050'},
    7: {'nome': 'Rodrigo Meier', 'cep': '89060'},
    8: {'nome': 'Isabela Romano', 'cep': '89070'},
    9: {'nome': 'Mateus Klein', 'cep': '89080'},
    10: {'nome': 'Juliana Martini', 'cep': '89090'},
}

# Dicionário de cidades de Santa Catarina.
cidades = {
    '89000': {'nome': 'Gaspar', 'estado': 'SC'},
    '89010': {'nome': 'Ilhota', 'estado': 'SC'},
    '89020': {'nome': 'Rodeio', 'estado': 'SC'},
    '89030': {'nome': 'Ascurra', 'estado': 'SC'},
    '89040': {'nome': 'Blumenau', 'estado': 'SC'},
    '89050': {'nome': 'Indaial', 'estado': 'SC'},
    '89060': {'nome': 'Timbó', 'estado': 'SC'},
    '89070': {'nome': 'Pomerode', 'estado': 'SC'},
    '89080': {'nome': 'Brusque', 'estado': 'SC'},
    '89090': {'nome': 'Guabiruba', 'estado': 'SC'},
}

# Cria um novo dicionário para armazenar o ID da pessoa e suas informações correspondentes.
pessoas_com_cidades = {}

for id_pessoa, info in pessoas.items():
    cep = info['cep']
    cidade_info = cidades.get(cep, "Cidade não encontrada")
    
    if cidade_info != "Cidade não encontrada":
        pessoas_com_cidades[id_pessoa] = {
            'nome': info['nome'],
            'cidade': cidade_info['nome'],
            'estado': cidade_info['estado']
        }
    else:
        pessoas_com_cidades[id_pessoa] = {
            'nome': info['nome'],
            'cidade': 'Desconhecida',
            'estado': 'Desconhecido'
        }

print(pessoas_com_cidades)