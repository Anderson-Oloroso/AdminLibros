import json
from menu import separador

def busTitulo():
    separador()
    print("Buscar por titulo")
    titulo = input("Título: ").lower().strip()

    with open("libros.json", "r") as f:
        datos = json.load(f)
    
    for dato in datos:
        if titulo in dato['Titulo'].lower():
            separador()
            print("Libro encontrado")
            print(f"\nTitulo: {dato['Titulo']}\nAutor: {dato['Autor']}\nGénero: {dato['Genero']}\nValoracion: {dato['Valoracion']}\n")

    with open("peliculas.json", "r") as f:
        datos = json.load(f)
    
    for dato in datos:
        if titulo in dato['Titulo'].lower():
            separador()
            print("Pelicula encontrada")
            print(f"\nTitulo: {dato['Titulo']}\nDirector: {dato['Director']}\nGénero: {dato['Genero']}\nValoracion: {dato['Valoracion']}\n")

    with open("musicas.json", "r") as f:
        datos = json.load(f)
    
    for dato in datos:
        if titulo in dato['Titulo'].lower():
            separador()
            print("Musica encontrada")
            print(f"\nTitulo: {dato['Titulo']}\nArtista: {dato['Artista']}\nGénero: {dato['Genero']}\nValoracion: {dato['Valoracion']}\n")

def busADA():
    separador()
    print("Buscar por Artista/Director/Autor")
    nombre = input("Nombre: ").lower().strip()
    with open("libros.json", "r") as f:
        datos = json.load(f)
    
    for dato in datos:
        if nombre in dato['Autor'].lower():
            separador()
            print("Autor encontrado")
            print(f"\nTitulo: {dato['Titulo']}\nAutor: {dato['Autor']}\nGénero: {dato['Genero']}\nValoracion: {dato['Valoracion']}\n")

    with open("musicas.json", "r") as f:
        datos = json.load(f)
    
    for dato in datos:
        if nombre in dato['Artista'].lower():
            separador()
            print("Artista encontrado")
            print(f"\nTitulo: {dato['Titulo']}\nAutor: {dato['Artista']}\nGénero: {dato['Genero']}\nValoracion:{dato['Valoracion']}\n")

    with open("peliculas.json", "r") as f:
        datos = json.load(f)
    
    for dato in datos:
        if nombre in dato['Director'].lower():
            separador()
            print("Director encontrado")
            print(f"\nTitulo: {dato['Titulo']}\nAutor: {dato['Director']}\nGénero: {dato['Genero']}\nValoracion: {dato['Valoracion']}\n")
    
def busGen():
    separador()
    print("Buscar por Genero")
    genero = input("Género: ").lower().strip()
    with open("libros.json", "r") as f:
        datos = json.load(f)
    
    for dato in datos:
        if genero in dato['Genero'].lower():
            separador()
            print("Genero encontrado")
            print(f"\nTitulo: {dato['Titulo']}\nAutor: {dato['Autor']}\nGénero: {dato['Genero']}\nValoracion: {dato['Valoracion']}\n")

    with open("musicas.json", "r") as f:
        datos = json.load(f)
    
    for dato in datos:
        if genero in dato['Genero'].lower():
            separador()
            print("Genero encontrado")
            print(f"\nTitulo: {dato['Titulo']}\nAutor: {dato['Artista']}\nGénero: {dato['Genero']}\nValoracion: {dato['Valoracion']}\n")

    with open("peliculas.json", "r") as f:
        datos = json.load(f)
    
    for dato in datos:
        if genero in dato['Genero'].lower():
            separador()
            print("Genero encontrado")
            print(f"\nTitulo: {dato['Titulo']}\nAutor: {dato['Director']}\nGénero: {dato['Genero']}\nValoracion: {dato['Valoracion']}\n")
            
            