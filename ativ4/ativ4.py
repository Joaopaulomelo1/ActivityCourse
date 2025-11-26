inicio = int(input("Digite o início do intervalo: "))
fim = int(input("Digite o fim do intervalo: "))

soma_pares = 0
tem_pares = False

for num in range(inicio, fim + 1):
    if num % 2 == 0:
        soma_pares += num
        tem_pares = True
else:
    if not tem_pares:
        print("Não há números pares no intervalo.")

print(f"Soma dos números pares: {soma_pares}")
