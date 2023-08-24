import random
def main():
    numero_secreto= random.randint(1,100)
    tentativas = 0
    limite_tentativas = 6

    print("Bem vindo ao jogo de adivinhação!")
    print("Adivinha um nunmero de 1 a 100")

    while tentativas < limite_tentativas:
        try:
            palpite= int(input("Digite seu palpite"))
        except ValueError: 
            print("Insira um numero válido")
            continue
        tentativas += 1
        if palpite > numero_secreto:
            print("Palpite maior que o numero secreto")
        elif palpite < numero_secreto:
            print("Palpite menor que o numero secreto")
        else:
            print(f"Parabéns! voce acertou em {tentativas}")
            break
    if tentativas >= limite_tentativas: 
        print(f"Ops! Voce ultrapassou o limite de tentativas. Fim de jogo!, o numero secreto era {numero_secreto}" )


main()