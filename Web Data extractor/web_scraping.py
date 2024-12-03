import bs4
import requests

# Ejemplo 1
# Extraer texto de una pagina web

resultado = requests.get('https://escueladirecta-blog.blogspot.com/2024/07/por-que-se-utiliza-python-en-ciencia-de.html')
sopa = bs4.BeautifulSoup(resultado.text, 'lxml')
print(sopa.select('title')[0].getText())

parrafo_especial = sopa.select('p')[3].getText()
print(parrafo_especial)

columna_lateral = sopa.select('#sidebar_item .snippet-item')
for p in columna_lateral:
    print(p.getText())


# Ejemplo 2
# Extraer imagenes de una pagina web

resultado_img = requests.get('https://www.escueladirecta.com/courses')

soup = bs4.BeautifulSoup(resultado_img.text, 'lxml')

imagenes = soup.select('.course-box-image')[0]['src']
print(imagenes)

imagen_curso = requests.get(imagenes)
f = open('imagen_curso.jpg', 'wb') # wb = write binary
f.write(imagen_curso.content)
f.close()