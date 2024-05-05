from rxconfig import config
import reflex as rx
from reflex_milenium.pages.index import index
from reflex_milenium.pages.menu_principal import menu_principal
from reflex_milenium.pages.registro_venta import registro_ventas
from reflex_milenium.pages.control_stock import control_stock

app = rx.App(
    title="Distrimilenium",
    stylesheets= [
        "https://fonts.googleapis.com/css2?family=Poppins:wght@300;500&display=swap",
        "https://fonts.googleapis.com/css2?family=Comfortaa:wght@500&display=swap",
        "https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css",
        "/css/styles.css"
    ]
)

