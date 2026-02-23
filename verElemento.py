import json

def verLibro():
    with open("libros.json", "r") as f:
        datos = json.load(f)
    
    for dato in datos:
        print(f"Titulo: {dato['Titulo']}\nAutor: {dato['Autor']}\nGénero: {dato['Genero']}\nValoracion: {dato['Valoracion']}\n")

def verPeli():
    with open("peliculas.json", "r") as f:
        datos = json.load(f)
    
    for dato in datos:
        print(f"Titulo: {dato['Titulo']}\nDirector: {dato['Director']}\nGénero: {dato['Genero']}\nValoracion {dato['Valoracion']}\n")

def verMusic():
    with open("musicas.json", "r") as f:
        datos = json.load(f)
    
    for dato in datos:
        print(f"Titulo: {dato['Titulo']}\nArtista: {dato['Artista']}\nGénero: {dato['Genero']}\nValoracion: {dato['Valoracion']}")