import time
import requests

def saludo():
    return "Hola"

def ingreso(datos):
    request = requests.get('https://www.google.com')
    return request.status_code == 200