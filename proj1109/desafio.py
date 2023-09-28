# Dicionário de produtos 
produtos = {
 1: {
        'nome': 'Arroz',
        'fornecedor_id': 1,
        'categoria_id': 1,
        'localizacao': 'Prateleira A1',
        'saldo': 50
    },
    2: {
        'nome': 'Televisão',
        'fornecedor_id': 2,
        'categoria_id': 2,
        'localizacao': 'Setor Eletrônicos',
        'saldo': 10
    },
    3: {
        'nome': 'Macarrão',
        'fornecedor_id': 1,
        'categoria_id': 1,
        'localizacao': 'Prateleira B2',
        'saldo': 30
    },
    4: {
        'nome': 'Smartphone',
        'fornecedor_id': 2,
        'categoria_id': 2,
        'localizacao': 'Setor Eletrônicos',
        'saldo': 15
    },
    5: {
        'nome': 'Leite',
        'fornecedor_id': 3,
        'categoria_id': 1,
        'localizacao': 'Prateleira C3',
        'saldo': 40
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

supermercado = {}

for produto_id, produto_info in produtos.items():
    fornecedor_id = produto_info['fornecedor_id']
    categoria_id = produto_info['categoria_id']
    
    print()
    fornecedor_info = fornecedores.get(fornecedor_id, {})
    categoria_info = categorias.get(categoria_id, {})
    print("x"*40)
    print(fornecedor_info)
    print(categoria_info)
    supermercado[produto_id] = {
        'nome': produto_info['nome'],
        'fornecedor': fornecedor_info['nome'],
        'categoria':  categoria_info['nome'],
    }


print(supermercado)  