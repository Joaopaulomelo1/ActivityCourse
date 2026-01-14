produtos = {}

for i in range(5):
    nome = input(f"Digite o nome do produto {i+1}: ")
    preco = float(input(f"Digite o preço do produto {i+1}: "))
    produtos[nome] = preco

total = sum(produtos.values())

print(f"Valor total da compra: R$ {total:.2f}")
