import flet as ft


def main(page: ft.Page):
    selected_symbols = []

    def toggle_selection(e):
        nonlocal selected_symbols
        symbol = e.control.data

        if symbol in selected_symbols:
            selected_symbols.remove(symbol)
        elif len(selected_symbols) < 6:
            selected_symbols.append(symbol)

        update_grid()
        update_selected_row()

    def update_grid():
        for container in grid.controls:
            symbol = container.data
            number_label = container.content.controls[1]
            if symbol in selected_symbols:
                order = selected_symbols.index(symbol) + 1
                container.border = ft.border.all(ft.Colors.RED)
                number_label.value = str(order)
                number_label.visible = True
            else:
                container.border = ft.border.all(ft.Colors.TRANSPARENT)
                number_label.visible = False
            container.update()

    def update_selected_row():
        selected_row.controls.clear()
        for symbol in selected_symbols:
            selected_row.controls.append(ft.Image(src=symbol, width=50, height=50))
        selected_row.update()

    def reset_selection(_):
        nonlocal selected_symbols
        selected_symbols = []
        update_grid()
        update_selected_row()

    # Define the symbols
    symbols = [f"Alchemy-{i}.png" for i in range(1, 21)]

    grid = ft.GridView(
        expand=True,
        max_extent=100,
        child_aspect_ratio=1.0,
        spacing=10,
        run_spacing=10,
    )
    for symbol in symbols:
        img = ft.Image(src=symbol, width=80, height=80)

        stack = ft.Stack(
            [
                img,
                ft.Text(
                    value="",
                    size=16,
                    color=ft.Colors.RED,
                    weight=ft.FontWeight.BOLD,
                    bottom=5,
                    left=5,
                    visible=False,
                ),
            ]
        )
        grid.controls.append(
            ft.Container(
                stack,
                border=ft.border.all(ft.Colors.TRANSPARENT),
                data=symbol,
                on_click=toggle_selection,
            )
        )

    reset_button = ft.IconButton(
        icon=ft.Icons.RESTART_ALT,
        icon_size=24,
        tooltip="Reset",
        on_click=reset_selection,
    )

    selected_row = ft.Row(
        controls=[],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=10,
    )

    layout = ft.Column(
        [
            grid,
            selected_row,
            ft.Row(
                [reset_button],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
        ],
        alignment=ft.MainAxisAlignment.START,
        spacing=10,
    )

    page.add(layout)

    update_grid()
    update_selected_row()


ft.app(target=main)
