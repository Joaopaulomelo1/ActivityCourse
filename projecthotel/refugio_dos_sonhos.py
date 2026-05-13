import streamlit as st
import uuid
from datetime import date, timedelta

st.set_page_config(page_title="Refúgio dos Sonhos", page_icon="🏨")


class Pessoa:
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email

    def exibir_informacoes(self):
        return f"{self.nome} | {self.telefone} | {self.email}"


class Cliente(Pessoa):
    def __init__(self, nome, telefone, email):
        super().__init__(nome, telefone, email)
        self.id = str(uuid.uuid4())[:6].upper()

    def exibir_informacoes(self):
        return super().exibir_informacoes() + f" | ID: {self.id}"


class Quarto:
    def __init__(self, numero, tipo, preco):
        self.numero = numero
        self.tipo = tipo
        self.preco = preco
        self.disponivel = True


class Reserva:
    def __init__(self, cliente, quarto, checkin, checkout):
        self.id = str(uuid.uuid4())[:6].upper()
        self.cliente = cliente
        self.quarto = quarto
        self.checkin = checkin
        self.checkout = checkout
        self.ativa = True

    @property
    def total(self):
        return (self.checkout - self.checkin).days * self.quarto.preco

    def cancelar(self):
        self.ativa = False
        self.quarto.disponivel = True


if "quartos" not in st.session_state:
    st.session_state.quartos = [
        Quarto(101, "Single", 180), Quarto(102, "Single", 180),
        Quarto(201, "Double", 280), Quarto(202, "Double", 280),
        Quarto(301, "Suite",  480), Quarto(302, "Suite",  520),
    ]
    st.session_state.clientes = [
        Cliente("Ana Souza",   "(81) 99001-1111", "ana@email.com"),
        Cliente("Bruno Lima",  "(81) 98002-2222", "bruno@email.com"),
        Cliente("Carla Matos", "(81) 97003-3333", "carla@email.com"),
    ]
    st.session_state.reservas = []

quartos  = st.session_state.quartos
clientes = st.session_state.clientes
reservas = st.session_state.reservas

st.sidebar.title("🏨 Refúgio dos Sonhos")
pagina = st.sidebar.radio("Menu", ["🏠 Início", "📋 Reservas", "📂 Ver Reservas", "👥 Clientes"])

if pagina == "🏠 Início":
    st.title("Quartos")
    for q in quartos:
        status = "🟢 Disponível" if q.disponivel else "🔴 Ocupado"
        st.write(f"**Quarto {q.numero}** — {q.tipo} — R$ {q.preco}/dia — {status}")

elif pagina == "📋 Reservas":
    st.title("Nova Reserva")
    livres = [q for q in quartos if q.disponivel]
    if not clientes:
        st.warning("Cadastre um cliente primeiro.")
    elif not livres:
        st.warning("Nenhum quarto disponível.")
    else:
        cliente = st.selectbox("Cliente", clientes, format_func=lambda c: c.nome)
        quarto  = st.selectbox("Quarto",  livres,   format_func=lambda q: f"Quarto {q.numero} ({q.tipo}) - R${q.preco}/dia")
        col1, col2 = st.columns(2)
        checkin  = col1.date_input("Check-in",  date.today())
        checkout = col2.date_input("Check-out", date.today() + timedelta(days=2))
        if st.button("Reservar"):
            if checkout <= checkin:
                st.error("Check-out deve ser após o check-in.")
            else:
                r = Reserva(cliente, quarto, checkin, checkout)
                quarto.disponivel = False
                reservas.append(r)
                st.success(f"Reserva {r.id} criada! Total: R$ {r.total:.2f}")

    st.divider()
    st.subheader("Reservas")
    for r in reservas:
        status = "🟢 Ativa" if r.ativa else "🔴 Cancelada"
        st.write(f"**{r.id}** — {status} | {r.cliente.nome} | Quarto {r.quarto.numero} | {r.checkin} → {r.checkout} | R$ {r.total:.2f}")
        if r.ativa and st.button("Cancelar", key=r.id):
            r.cancelar()
            st.rerun()

elif pagina == "📂 Ver Reservas":
    st.title("Visualização de Reservas")
    ativas     = [r for r in reservas if r.ativa]
    canceladas = [r for r in reservas if not r.ativa]
    col1, col2, col3 = st.columns(3)
    col1.metric("Total",         len(reservas))
    col2.metric("🟢 Ativas",     len(ativas))
    col3.metric("🔴 Canceladas", len(canceladas))
    st.divider()
    filtro = st.radio("Filtrar:", ["Todas", "Ativas", "Canceladas"], horizontal=True)
    lista  = {"Todas": reservas, "Ativas": ativas, "Canceladas": canceladas}[filtro]
    for r in lista:
        cor = "🟢" if r.ativa else "🔴"
        st.write(f"{cor} **{r.id}** | {r.cliente.nome} | Quarto {r.quarto.numero} | {r.checkin} → {r.checkout} | R$ {r.total:.2f}")
        if r.ativa and st.button("Cancelar", key=f"v_{r.id}"):
            r.cancelar()
            st.rerun()

elif pagina == "👥 Clientes":
    st.title("Clientes")
    with st.expander("➕ Novo Cliente"):
        nome     = st.text_input("Nome")
        telefone = st.text_input("Telefone")
        email    = st.text_input("E-mail")
        if st.button("Cadastrar"):
            if nome and telefone and email:
                clientes.append(Cliente(nome, telefone, email))
                st.success("Cliente cadastrado!")
                st.rerun()
            else:
                st.error("Preencha todos os campos.")
    st.divider()
    for c in clientes:
        st.write(c.exibir_informacoes())