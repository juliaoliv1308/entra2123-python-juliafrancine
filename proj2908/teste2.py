import random

numero_aleatorio = random.randint(1,10)

tentativas = 0

while tentativas < 3:
    usuario = int(input("Adivinhe o número de 1 a 10: "))
    tentativas += 1
    if usuario == numero_aleatorio:
        print("Parabéns! Você acertou!")
        break
    else:
        print("Tente novamente!")

if usuario != numero_aleatorio:
    print("Infelizmente você não acertou. O número era ", numero_aleatorio)
