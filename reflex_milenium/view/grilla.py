import reflex as rx
from reflex_milenium.components.icono_menu import icono
from reflex_milenium.components.sub_menu import menu_desplegable

def secciones():
    return rx.hstack( #
            rx.flex(
                menu_desplegable(icono("file", "Ventas"), 'Registrar Venta', '/registro-venta'),
                icono("file", "Ventas"),
                icono("shopping-cart", "Compras"),
                icono("landmark", "Caja-Bco"),
                icono("store", "Egresos"),
                icono("database", "Stock"),
                icono("book-user", "Clientes"),
                icono("folder-open", "Contable"),
                icono("square-activity", "Varios"),
                wrap="wrap",
                spacing="5",
                width="100%",
                class_name="animate__animated animate__bounceIn",
            ),
            align="end",
            justify="end",
            width="100%",
            margin_x="5%"
        )