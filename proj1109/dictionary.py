
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

def print_dictionary(dictionary):
    for key, value in dictionary.items():
        print(f'{key}: {value}')

# Chame a função para imprimir o dicionário
print_dictionary(questions)
