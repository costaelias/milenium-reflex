import reflex as rx
import reflex_milenium.utils as utils 
from reflex_milenium.components.ant_component import result

@rx.page(
    title="Inicio",
    description="Pagina de inicio",
    image=utils.preview,
    meta=utils.index_meta
)
def index() -> rx.Component:
    click:bool = False
    return rx.box(
            rx.vstack(
               rx.box(
                    rx.image(
                        src="img/Logo-Milenium-01.svg",
                        alt="logo-header",
                        width="100px", 
                        height="auto"
                    ),
                    height= '65px;',
                    width= '50%;',
                    padding= "1em 2em 2em;",
            ),
            rx.spacer(),
            rx.form(
                rx.vstack(
                    rx.input(
                        placeholder="First Name",
                        name="first_name",
                    ),
                    rx.input(
                        placeholder="Last Name",
                        name="last_name",
                    ),
                    rx.button(
                            "Submit", 
                            type="submit",
                            radius="full",
                            margin_left="30%",
                            on_click=rx.redirect(path="/menu-principal",)
                    ),
                
                ),
            ),
            display= "flex",
            justify_content= "center",
            align_items= "center",
            width= "20%",
            margin = '0 auto;',
            background_color= "rgba(222, 170, 197, 0.8)",
            box_shadow= "8px 8px 5px #444;",
            padding= "1em 2em 2em;",
            margin_top='8em'
        ),
    )

