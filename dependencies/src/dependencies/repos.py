import requests
from bs4 import BeautifulSoup  # 👈 Importamos nuestra nueva lupa para HTML


def get_repos(url):
    # 1. Hacemos la petición a la web normal
    respuesta = requests.get(url)

    # 2. Extraemos el texto crudo (el HTML gigante de la página)
    html_puro = respuesta.text

    # 3. Metemos el HTML en BeautifulSoup para poder buscar dentro
    sopa = BeautifulSoup(html_puro, "html.parser")

    # 4. Buscamos la etiqueta <ul> que tenga exactamente esos atributos
    # Le decimos: "Busca un 'ul' cuyos atributos ('attrs') sean estos:"
    lista_repos = sopa.find(
        "ul",
        attrs={
            "data-filterable-for": "your-repos-filter",
            "data-filterable-type": "substring",
        },
    )

    # 5. Comprobamos si la encontró
    if lista_repos:
        print("¡Etiqueta encontrada!")
        print(lista_repos)  # Esto imprimirá el bloque HTML de la lista
    else:
        print("No se encontró la etiqueta en esta página.")


# Llamamos a la función con la URL de tu perfil
get_repos("https://github.com/rodrigo-castilla?tab=repositories")
