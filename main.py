import flet as ft


def main(page: ft.Page):
    selected_symbols = []

    def toggle_selection(e):
        symbol = e.control.data

        if symbol in selected_symbols:
            # Unselect symbol
            selected_symbols.remove(symbol)
        elif len(selected_symbols) < 6:
            # Select symbol only if under the limit
            selected_symbols.append(symbol)

        update_grid()

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

    page.add(grid)


ft.app(target=main)
