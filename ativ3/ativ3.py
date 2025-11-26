numero_secreto = 7
tentativas = 0

while tentativas < 3:
    palpite = int(input("Tente adivinhar o número: "))
    tentativas += 1

    if palpite == numero_secreto:
        print("Parabéns! Você acertou o número!")
        break
else:
    print("Suas tentativas acabaram. Não foi dessa vez, tente novamente!")
