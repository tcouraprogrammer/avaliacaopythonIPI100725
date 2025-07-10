import random
def jogar():
    numero_secreto = random.randint(1, 10)
    tentativas = 5
    tentativa_atual = 0

    print("\nSeja Bem-Vindo ao Jogo de Adivinhação!")
    print("Tente adivinhar o número entre 1 e 10.")
    print(f"Você tem {tentativas} tentativas.\n")

    while tentativa_atual < tentativas:
        palpite = int(input(f"Tentativa {tentativa_atual + 1}: "))
        tentativa_atual += 1

        if palpite == numero_secreto:
            print("Parabéns! Você acertou o número!\n")
            return  
        else:
            print("Errado!", end=' ')
            if palpite < numero_secreto:
                print("Dica: o número é maior.")
            else:
                print("Dica: o número é menor.")

    print(f"\nSuas tentativas acabaram. O número era {numero_secreto}.\n")

while True:
    jogar()
    resposta = input("Deseja tentar novamente? (sim/não): ").strip().lower()
    if resposta != "sim":
        print("Obrigado por jogar! Até a próxima.")
        break