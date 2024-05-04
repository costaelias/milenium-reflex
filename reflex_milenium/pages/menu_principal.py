import reflex as rx
from reflex_milenium.view.grilla import secciones
from reflex_milenium.view.header import header

@rx.page(route="/menu-principal")
def menu_principal():
    return rx.vstack(
            header("Menu Principal"),
            rx.box(
                secciones(), 
                padding= "1em 2em 2em;",
                margin_top='1em',
            ),
            width="100%",             
        )