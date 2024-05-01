from datetime import datetime, timedelta, timezone
# import pytz
import reflex as rx

# Común


def lang() -> rx.Component:
    return rx.script("document.documentElement.lang='es'")

preview = "https://img.freepik.com/foto-gratis/lindo-zorro-rojo-mirando-naturaleza-generado-ai_188544-19724.jpg"

_meta = [
    {"name": "og:type", "content": "website"},
    {"name": "og:image", "content": preview},
    {"name": "twitter:card", "content": "summary_large_image"},
    {"name": "twitter:site", "content": "@mouredev"}
]

# Index

index_title = "MoureDev | Te enseño programación y desarrollo de software"
index_description = "Hola, mi nombre es Brais Moure. Soy ingeniero de software, desarrollador freelance full-stack y divulgador."

index_meta = [
    {"name": "og:title", "content": index_title},
    {"name": "og:description", "content": index_description},
]
index_meta.extend(_meta)