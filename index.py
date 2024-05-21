import flet as ft

def main(page: ft.Page):

    # Создаем поле ввода
    input_field = ft.TextField(label="Задайте имя вашему помощнику", width=300)

    # Функция-обработчик для кнопки "Далее"
    def show_greeting_page(e):
        name = input_field.value
        if not name:
            page.snack_bar = ft.SnackBar(ft.Text("Введите имя"))
            page.snack_bar.open = True
            page.update()
            return
        greeting_text.value = f"Здравствуйте, {name}! \n Я ваш помощник и создан чтобы помогать вам"
        main_container.visible = False
        greeting_container.visible = True
        page.update()

    # Функция-обработчик для кнопки "Назад"
    def show_main_page(e):
        main_container.visible = True
        greeting_container.visible = False
        page.update()

    # Функция-обработчик для кнопки "Очистить текст"
    def clear_text(e):
        input_field.value = ""
        page.update()

    # Создаем элементы для главной страницы
    next_button = ft.ElevatedButton(text="Далее", on_click=show_greeting_page)
    clear_text_button = ft.ElevatedButton(text="Очистить текст", on_click=clear_text)

    # Создаем контейнер для главной страницы с выравниванием по центру
    main_container = ft.Column(
        controls=[
            input_field,
            ft.Row(
                controls=[next_button, clear_text_button],
                alignment=ft.MainAxisAlignment.CENTER
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        expand=True
    )

    # Создаем элементы для страницы приветствия
    greeting_text = ft.Text("", text_align="center")
    back_button = ft.ElevatedButton(text="Назад", on_click=show_main_page)

    # Создаем контейнер для страницы приветствия с выравниванием по центру
    greeting_container = ft.Container(
        content=ft.Column(
            controls=[
                greeting_text,
                back_button
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True
        ),
        alignment=ft.alignment.center,
        expand=True,
        visible=False  # По умолчанию скрываем контейнер
    )

    # Добавляем оба контейнера на страницу
    page.add(main_container, greeting_container)

# Запускаем приложение
ft.app(target=main)
