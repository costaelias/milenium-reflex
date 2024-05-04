import reflex as rx
from reflex_milenium.view.header import header

@rx.page(route="/registro-venta")
def registro_ventas():
    return rx.vstack(
            header("Registrar Venta"),
            rx.box(
                rx.text("Registrar venta"),
                padding= "1em 2em 2em;",
                margin_top='1em',
            )                
        )