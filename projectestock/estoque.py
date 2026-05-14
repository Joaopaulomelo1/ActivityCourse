import sqlite3
from datetime import date


class Produto:
    def __init__(self, id, nome, descricao, quantidade, preco):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.quantidade = quantidade
        self.preco = preco

    def __str__(self):
        return (f"[{self.id}] {self.nome} | {self.descricao} | "
                f"Qtd: {self.quantidade} | R$ {self.preco:.2f}")


class Venda:
    def __init__(self, id, id_produto, quantidade_vendida, data_venda):
        self.id = id
        self.id_produto = id_produto
        self.quantidade_vendida = quantidade_vendida
        self.data_venda = data_venda

    def __str__(self):
        return (f"Venda #{self.id} | Produto ID: {self.id_produto} | "
                f"Qtd: {self.quantidade_vendida} | Data: {self.data_venda}")


def conectar():
    return sqlite3.connect("estoque.db")

def criar_tabelas():
    with conectar() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS produtos (
                id          INTEGER PRIMARY KEY AUTOINCREMENT,
                nome        TEXT    NOT NULL,
                descricao   TEXT,
                quantidade  INTEGER NOT NULL DEFAULT 0,
                preco       REAL    NOT NULL
            )
        """)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS vendas (
                id                 INTEGER PRIMARY KEY AUTOINCREMENT,
                id_produto         INTEGER NOT NULL,
                quantidade_vendida INTEGER NOT NULL,
                data_venda         TEXT    NOT NULL,
                FOREIGN KEY (id_produto) REFERENCES produtos(id)
            )
        """)


def cadastrar_produto():
    print("\n── Cadastrar Produto ──")
    nome = input("Nome: ").strip()
    descricao = input("Descrição: ").strip()
    quantidade = int(input("Quantidade: "))
    preco = float(input("Preço (ex: 19.90): "))

    with conectar() as conn:
        conn.execute(
            "INSERT INTO produtos (nome, descricao, quantidade, preco) VALUES (?, ?, ?, ?)",
            (nome, descricao, quantidade, preco)
        )
    print("✅ Produto cadastrado com sucesso!")


def listar_produtos():
    print("\n── Produtos em Estoque ──")
    with conectar() as conn:
        rows = conn.execute("SELECT * FROM produtos").fetchall()

    if not rows:
        print("Nenhum produto cadastrado.")
        return

    for row in rows:
        p = Produto(*row)
        print(p)


def atualizar_quantidade():
    print("\n── Atualizar Quantidade ──")
    listar_produtos()
    id_produto = int(input("\nID do produto: "))
    nova_qtd = int(input("Nova quantidade: "))

    with conectar() as conn:
        alterado = conn.execute(
            "UPDATE produtos SET quantidade = ? WHERE id = ?",
            (nova_qtd, id_produto)
        ).rowcount

    if alterado:
        print("✅ Quantidade atualizada!")
    else:
        print("❌ Produto não encontrado.")


def remover_produto():
    print("\n── Remover Produto ──")
    listar_produtos()
    id_produto = int(input("\nID do produto a remover: "))
    confirma = input(f"Tem certeza que quer remover o produto {id_produto}? (s/n): ")

    if confirma.lower() != "s":
        print("Operação cancelada.")
        return

    with conectar() as conn:
        alterado = conn.execute(
            "DELETE FROM produtos WHERE id = ?", (id_produto,)
        ).rowcount

    if alterado:
        print("✅ Produto removido!")
    else:
        print("❌ Produto não encontrado.")


def registrar_venda():
    print("\n── Registrar Venda ──")
    listar_produtos()
    id_produto = int(input("\nID do produto vendido: "))
    quantidade = int(input("Quantidade vendida: "))

    with conectar() as conn:
        row = conn.execute(
            "SELECT quantidade FROM produtos WHERE id = ?", (id_produto,)
        ).fetchone()

        if not row:
            print("❌ Produto não encontrado.")
            return

        if row[0] < quantidade:
            print(f"❌ Estoque insuficiente! Disponível: {row[0]}")
            return

        conn.execute(
            "INSERT INTO vendas (id_produto, quantidade_vendida, data_venda) VALUES (?, ?, ?)",
            (id_produto, quantidade, str(date.today()))
        )
        conn.execute(
            "UPDATE produtos SET quantidade = quantidade - ? WHERE id = ?",
            (quantidade, id_produto)
        )
    print("✅ Venda registrada e estoque atualizado!")


def listar_vendas():
    print("\n── Histórico de Vendas ──")
    with conectar() as conn:
        rows = conn.execute("""
            SELECT v.id, p.nome, v.quantidade_vendida, v.data_venda
            FROM vendas v
            JOIN produtos p ON v.id_produto = p.id
        """).fetchall()

    if not rows:
        print("Nenhuma venda registrada.")
        return

    for row in rows:
        print(f"Venda #{row[0]} | Produto: {row[1]} | Qtd: {row[2]} | Data: {row[3]}")


def menu():
    criar_tabelas()
    opcoes = {
        "1": ("Cadastrar produto",      cadastrar_produto),
        "2": ("Listar produtos",        listar_produtos),
        "3": ("Atualizar quantidade",   atualizar_quantidade),
        "4": ("Remover produto",        remover_produto),
        "5": ("Registrar venda",        registrar_venda),
        "6": ("Histórico de vendas",    listar_vendas),
        "0": ("Sair",                   None),
    }

    while True:
        print("\n══════════════════════════════")
        print("   SISTEMA DE ESTOQUE")
        print("══════════════════════════════")
        for chave, (descricao, _) in opcoes.items():
            print(f"  [{chave}] {descricao}")
        print("══════════════════════════════")

        escolha = input("Opção: ").strip()

        if escolha == "0":
            print("Até mais! 👋")
            break
        elif escolha in opcoes:
            opcoes[escolha][1]()
        else:
            print("❌ Opção inválida.")


if __name__ == "__main__":
    menu()