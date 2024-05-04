import reflex as rx
import reflex_milenium.utils as utils 
from reflex_milenium.components.ant_component import result
from reflex_milenium.state.page_state import PageState

@rx.page(
    title="Inicio",
    description="Pagina de inicio",
    image=utils.preview,
    meta=utils.index_meta
)
def index() -> rx.Component:
    return rx.vstack(
               rx.box(
                    rx.image(
                        src="/img/Logo-Milenium-01.svg",
                        alt="logo-header",
                        width="auto", 
                        height="auto"
                    ),
                    height= '8em',
                    width= '8em',
                    padding= "1em 0 0 0",
            ),
            rx.form( #revisar/rehacer este form porque ingresa a 
                rx.vstack(
                    rx.input(
                        placeholder="Usuario",
                        name="usuario",
                        required=True,
                        color_scheme="red"
                    ),
                    rx.input(
                        placeholder="Clave",
                        name="password",
                        type="password",
                        required=True,
                        color_scheme="red"
                    ),
                    rx.button(
                            "Submit", 
                            type="submit",
                            radius="full",
                            margin_left="30%",
                    ),
                
                ),
                on_submit=PageState.handle_submit,
                reset_on_submit=True,
            ),
            display= "flex",
            justify_content= "center",
            align_items= "center",
            width= "20%",
            margin = '0 auto;',
            background_color= "rgba(39, 112, 245, 0.8)",
            box_shadow= "8px 8px 5px #444;",
            padding= "1em 2em 2em;",
            margin_top='8em',
            min_width="200px"
        )

