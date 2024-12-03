import bs4
import requests


# URL sin numero de pagina
url = 'https://books.toscrape.com/catalogue/page-{}.html'


# Lista de titulos con 4 o 5 estrellas
titulos_4_5_estrellas = []


# Iterar sobre las paginas
for n in range(1,51):

    # Obtener la pagina
    url_pagina = url.format(n)
    res = requests.get(url_pagina)

    # Crear un objeto soup
    soup = bs4.BeautifulSoup(res.text, 'lxml')

    # Seleccionar datos de los libros
    libros = soup.select('.product_pod')

    # Iterar sobre los libros
    for libro in libros:

            # Verificar si tiene 4 o 5 estrellas
            if len(libro.select('.star-rating.Four')) != 0 or len(libro.select('.star-rating.Five')) != 0:

                # Obtener el titulo
                titulo = libro.select('a')[1]['title']

                # Agregar a la lista
                titulos_4_5_estrellas.append(titulo)


# Imprimir la lista
for titulo in titulos_4_5_estrellas:
    print(titulo)