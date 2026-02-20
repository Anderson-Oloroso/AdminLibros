import json
from menu import separador

def addLibro():
    separador
    print("Agregar un nuevo libro")
    titulo = input("Título del libro: ")
    autor = input("Autor: ")
    genero = input("Género: ")
    val = float(input("Valoracion"))

    nuevoLibro = {
        "Titulo": titulo,
        "Autor": autor,
        "Genero": genero,
        "Valoracion": val
    }
    with open("libros.json", "r") as file:
        dato = json.load(file)

        dato.append(nuevoLibro)

    with open("libros.json", "w") as f:
            try:
                json.dump(dato, f, indent=4)
            except Exception as e:
                 print("Error: ", e)
            else:
                print("Pelicula agregada correctamente")

def addPeli():
    separador()
    print("Agregar nueva pelicula")
    titulo = input("Título de la pelicula: ")
    director = input("Director: ")
    genero = input("Género: ")
    val = int(input("Valoracion: "))
    
    nuevoLibro = {
        "Titulo": titulo,
        "Director": director,
        "Genero": genero,
        "Valoracion": val
    }
    with open("peliculas.json", "r") as file:
        dato = json.load(file)

        dato.append(nuevoLibro)

    with open("peliculas.json", "w") as f:
            try:
                json.dump(dato, f, indent=4)
            except Exception as e:
                 print("Error: ", e)
            else:
                print("Pelicula agregada correctamente")

def addMusic():
    separador()
    print("Agregar nueva musica")
    titulo = input("Título de la musica: ")
    artista = input("Artista: ")
    genero = input("Género: ")
    val = int(input("Valoracion: "))

    nuevoLibro = {
        "Titulo": titulo,
        "Artista": artista,
        "Genero": genero,
        "Valoracion": val
    }
    with open("musicas.json", "r") as file:
        dato = json.load(file)

        dato.append(nuevoLibro)

    with open("musicas.json", "w") as f:
            try:
                json.dump(dato, f, indent=4)
            except Exception as e:
                 print("Error: ", e)
            else:
                print("Pelicula agregada correctamente")

