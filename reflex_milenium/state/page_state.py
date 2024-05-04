import reflex as rx
from reflex_milenium.api.api import ingreso

class PageState(rx.State):
    
    @rx.background
    async def handle_submit(self, form_data: dict):
        print(form_data)
        resultado = ingreso(form_data)
        if not resultado:
            return rx.redirect(path="/index")
        return rx.redirect(path="/menu-principal")