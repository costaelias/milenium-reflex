import reflex as rx

@rx.page(route="/menu-principal")
def menu_principal():
    return rx.vstack(
        rx.hstack(
            rx.box(
                rx.text("Un boton1")
            ),
            rx.box(
                rx.text("Otro Boton1")
            )
        ),
        rx.hstack(
            rx.box(
                rx.text("Un boton")
            ),
            rx.box(
                rx.text("Otro Boton")
            )
        ),
    )