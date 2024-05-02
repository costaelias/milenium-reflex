import reflex as rx

class Result(rx.Component):
    library = "antd"
    tag = "Result"
    status= "success"
    title="Ingreso Correcto"

result = Result.create()
