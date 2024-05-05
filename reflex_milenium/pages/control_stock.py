import reflex as rx
from reflex_milenium.view.header import header

@rx.page(route="/contorl-stock")
def control_stock():
    return rx.vstack(
            header("Registrar Venta"),
            rx.box(
                rx.text("Control Stock"),
                rx.button("Controlar minimo stock"),
                padding= "1em 2em 2em;",
                margin_top='1em',
            )                
        )