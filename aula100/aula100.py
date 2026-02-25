import flet as ft

def main(page: ft.Page):
    page.title = "Formulário de Contato"
    page.vertical_alignment = ft.MainAxisAlignment.START

    nome_input = ft.TextField(label="Nome", width=300)
    email_input = ft.TextField(label="Email", width=300)
    mensagem_input = ft.TextField(label="Mensagem", width=300, multiline=True, min_lines=3)
    confirm_label = ft.Text("")

    def enviar_formulario(e):
        nome = nome_input.value.strip()
        email = email_input.value.strip()
        mensagem = mensagem_input.value.strip()
        if nome and email and mensagem:
            confirm_label.value = f"Formulário enviado com sucesso! Obrigado, {nome}."
            nome_input.value = ""
            email_input.value = ""
            mensagem_input.value = ""
        else:
            confirm_label.value = "Por favor, preencha todos os campos."
        page.update()

    enviar_button = ft.ElevatedButton(text="Enviar", on_click=enviar_formulario)

    page.add(
        nome_input,
        email_input,
        mensagem_input,
        enviar_button,
        confirm_label
    )

ft.app(target=main)