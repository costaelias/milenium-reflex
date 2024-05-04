import reflex as rx

def menu_desplegable(boton:rx.Component, nombre, link):
    return rx.popover.root(
                    rx.popover.trigger(
                        boton,
                    ),
                    rx.popover.content(
                        rx.flex(
                            rx.link(nombre, href=link),
                            direction="column",
                            spacing="3",
                        ),
                    ),
                )