import flet as ft

def main(page: ft.Page):
    page.title = "Lista de Tarefas"
    page.vertical_alignment = ft.MainAxisAlignment.START

    task_input = ft.TextField(
        label="Digite uma tarefa",
        width=300
    )

    task_list = ft.Column()

    def add_task(e):
        if task_input.value.strip() != "":
            task_list.controls.append(
                ft.Text(f"• {task_input.value}")
            )
            task_input.value = ""
            page.update()

    add_button = ft.ElevatedButton(
        text="Adicionar",
        on_click=add_task
    )

    page.add(
        task_input,
        add_button,
        ft.Divider(),
        task_list
    )

ft.app(target=main)