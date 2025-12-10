usuario_correto = "admin"
senha_correta = "1234"

tentativas = 3

for i in range(tentativas):
    usuario = input("Digite o usuário: ")
    senha = input("Digite a senha: ")

    if usuario == usuario_correto and senha == senha_correta:
        print("Bem-vindo!")
        break
    else:
        restantes = tentativas - (i + 1)
        if restantes > 0:
            print(f"Credenciais incorretas. Tentativas restantes: {restantes}")
        else:
            print("Credenciais incorretas.")

if usuario != usuario_correto or senha != senha_correta:
    for _ in range(3):
        print("Acesso bloqueado")
