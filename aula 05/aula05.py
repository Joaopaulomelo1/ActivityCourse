num_alunos = int(input("Digite o número de alunos: "))

soma_medias = 0

for i in range(num_alunos):
    print(f"\nAluno {i + 1}:")
    
    nome = input("Nome: ")
    notas = []

    for j in range(3):
        nota = float(input(f"Digite a nota {j + 1}: "))
        notas.append(nota)

    media = sum(notas) / 3
    soma_medias += media

    if media >= 7.0:
        status = "Aprovado"
    else:
        status = "Reprovado"

    print(f"\nNome: {nome}")
    print(f"Notas: {notas}")
    print(f"Média: {media:.2f}")
    print(f"Situação: {status}")

media_geral = soma_medias / num_alunos

print("\n===============================")
print(f"Média geral da turma: {media_geral:.2f}")
print("===============================")
