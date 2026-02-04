tarefas = []

PRIORIDADES = ("Baixa", "Média", "Alta")

categorias = set()


def adicionar_tarefa():
    nome = input("Nome da tarefa: ")
    descricao = input("Descrição da tarefa: ")

    print("\nPrioridades disponíveis:")
    for i, p in enumerate(PRIORIDADES):
        print(f"{i + 1} - {p}")

    prioridade = int(input("Escolha a prioridade (1-3): "))
    categoria = input("Categoria da tarefa: ")

    tarefa = {
        "nome": nome,
        "descricao": descricao,
        "prioridade": PRIORIDADES[prioridade - 1],
        "categoria": categoria,
        "concluida": False
    }

    tarefas.append(tarefa)
    categorias.add(categoria)

    print("\n✅ Tarefa adicionada com sucesso!\n")


def listar_tarefas():
    if not tarefas:
        print("\n⚠ Nenhuma tarefa cadastrada.\n")
        return

    print("\n📋 LISTA DE TAREFAS")
    for i, tarefa in enumerate(tarefas):
        status = "✔ Concluída" if tarefa["concluida"] else "⏳ Pendente"
        print(f"""
{i + 1}. {tarefa['nome']}
   Descrição: {tarefa['descricao']}
   Prioridade: {tarefa['prioridade']}
   Categoria: {tarefa['categoria']}
   Status: {status}
        """)


def marcar_concluida():
    listar_tarefas()
    indice = int(input("Digite o número da tarefa concluída: ")) - 1

    if 0 <= indice < len(tarefas):
        tarefas[indice]["concluida"] = True
        print("\n✅ Tarefa marcada como concluída!\n")
    else:
        print("\n❌ Tarefa inválida.\n")


def listar_por_prioridade():
    prioridade = input("Digite a prioridade (Baixa, Média, Alta): ")

    print(f"\n🔥 Tarefas com prioridade {prioridade}:")
    for tarefa in tarefas:
        if tarefa["prioridade"] == prioridade:
            print(f"- {tarefa['nome']} ({tarefa['categoria']})")


def listar_por_categoria():
    if not categorias:
        print("\n⚠ Nenhuma categoria cadastrada.\n")
        return

    print("\n📂 Categorias disponíveis:", ", ".join(categorias))
    categoria = input("Digite a categoria: ")

    print(f"\n🗂 Tarefas da categoria {categoria}:")
    for tarefa in tarefas:
        if tarefa["categoria"] == categoria:
            print(f"- {tarefa['nome']} ({tarefa['prioridade']})")


def menu():
    while True:
        print("""
========== GERENCIADOR DE TAREFAS ==========
1 - Adicionar tarefa
2 - Listar tarefas
3 - Marcar tarefa como concluída
4 - Listar tarefas por prioridade
5 - Listar tarefas por categoria
0 - Sair
===========================================
        """)

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_tarefa()
        elif opcao == "2":
            listar_tarefas()
        elif opcao == "3":
            marcar_concluida()
        elif opcao == "4":
            listar_por_prioridade()
        elif opcao == "5":
            listar_por_categoria()
        elif opcao == "0":
            print("\n👋 Saindo do programa...\n")
            break
        else:
            print("\n❌ Opção inválida!\n")


menu()
