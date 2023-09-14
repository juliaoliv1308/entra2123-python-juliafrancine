import random

opcoes = ['pedra', 'papel', 'tesoura']
computador = opcoes[random.randint(0,2)]

usuario = False

while usuario == False:
    usuario = input("Pedra, papel ou tesoura? ")

    if usuario == computador:
        print("Empate!")
    elif usuario == "pedra":
        if computador == "papel":
            print("Você perdeu! Papel embrulha pedra!")
        else:
            print("Você ganhou! Pedra quebra tesoura!")
    elif usuario == "papel":
        if computador == "tesoura":
            print("Você perdeu! Tesoura corta papel!")
        else:
            print("Você ganhou! Papel embrulha pedra!")
    elif usuario == "tesoura":
        if computador == "pedra":
            print("Você perdeu! Pedra quebra tesoura!")
        else:
            print("Você ganhou! Tesoura corta papel!")

    usuario = False
    computador = opcoes[random.randint(0,2)]
