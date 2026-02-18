import json

def busTitulo():
    titulo = input("Título: ").lower().strip()

    with open("libros.json", "r") as f:
        datos = json.load(f)
    
    for dato in datos:
        if titulo in dato['Titulo'].lower():
            print(f"\nTitulo: {dato['Titulo']}\nAutor: {dato['Autor']}\nGénero: {dato['Genero']}\n")

    with open("peliculas.json", "r") as f:
        datos = json.load(f)
    
    for dato in datos:
        if titulo in dato['Titulo'].lower():
            print(f"\nTitulo: {dato['Titulo']}\nDirector: {dato['Director']}\nGénero: {dato['Genero']}\n")
    
    with open("musicas.json", "r") as f:
        datos = json.load(f)
    
    for dato in datos:
        if titulo in dato['Titulo'].lower():
            print(f"\nTitulo: {dato['Titulo']}\nArtista: {dato['Artista']}\nGénero: {dato['Genero']}\n")
    
def busADA():
    nombre = input("Nombre: ").lower().strip()

    with open("libros.json", "r") as f:
        datos = json.load(f)
    
    for dato in datos:
        if nombre in dato['Autor'].lower():
            print(f"\nTitulo: {dato['Titulo']}\nAutor: {dato['Autor']}\nGénero: {dato['Genero']}\n")

    with open("musicas.json", "r") as f:
        datos = json.load(f)
    
    for dato in datos:
        if nombre in dato['Artista'].lower():
            print(f"\nTitulo: {dato['Titulo']}\nAutor: {dato['Artista']}\nGénero: {dato['Genero']}\n")

    with open("peliculas.json", "r") as f:
        datos = json.load(f)
    
    for dato in datos:
        if nombre in dato['Director'].lower():
            print(f"\nTitulo: {dato['Titulo']}\nAutor: {dato['Director']}\nGénero: {dato['Genero']}\n")
    
def busGen():
    genero = input("Género: ").lower().strip()

    with open("libros.json", "r") as f:
        datos = json.load(f)
    
    for dato in datos:
        if genero in dato['Genero'].lower():
            print(f"\nTitulo: {dato['Titulo']}\nAutor: {dato['Autor']}\nGénero: {dato['Genero']}\n")

    with open("musicas.json", "r") as f:
        datos = json.load(f)
    
    for dato in datos:
        if genero in dato['Genero'].lower():
            print(f"\nTitulo: {dato['Titulo']}\nAutor: {dato['Artista']}\nGénero: {dato['Genero']}\n")

    with open("peliculas.json", "r") as f:
        datos = json.load(f)
    
    for dato in datos:
        if genero in dato['Genero'].lower():
            print(f"\nTitulo: {dato['Titulo']}\nAutor: {dato['Director']}\nGénero: {dato['Genero']}\n")
            
            
            