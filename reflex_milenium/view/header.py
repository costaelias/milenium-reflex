import reflex as rx


def header(ubicacion:str):
    return rx.hstack(
        rx.box(rx.image(
                src="/img/Logo-Milenium-01.svg",
                alt="logo-header",
                width="100px", 
                height="3em"            
        ),padding="1% 1.5%;"),
        rx.spacer(),
        rx.box(
            rx.text(ubicacion),
            padding="1em",
            height="3em"
        ),
        rx.spacer(),
        bg="rgba(39, 112, 245, 0.8)",
        height="5em",
        width="100%",
    )