import reflex as rx

def icono(nombre_icono:str, texto:str):
    return rx.card(
        rx.vstack(
            rx.icon(
                tag=nombre_icono,
                size=64,
                align="center",
                margin_x="0.8em",
            ),
            rx.text(
                texto,
                margin_x="1em",
                align="center"
            ),
            justify="center"            
        )
    )