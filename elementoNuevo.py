import json
from menu import separador

def encontrar(id):
    with open("libros.json", "r") as f:
        datos = json.load(f)

    with open("peliculas.json", "r") as f:
        datos = json.load(f)

    with open("musicas.json", "r") as f:
        datos = json.load(f)

    for dato in datos:
        if id == dato['Id']:
            print("Error. El id ya existe, ingrese un id diferente")
            separador()
        else:
            return id
    

def addLibro(id):
    
    titulo = input("Título del libro: ")
    autor = input("Autor: ")
    genero = input("Género: ")
    val = float(input("Valoracion"))

    nuevoLibro = {
        "Id": id,
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
                print("Libro agregado correctamente")
            except json.JSONDecodeError as e:
                print("Error JSON: ", e)
            except ValueError as f:
                print(f)
            else:
                print("Pelicula agregada correctamente")
            finally:
                dato = []

def addPeli():
    id = int(input("Id: "))
    encontrar(id)
    titulo = input("Título de la pelicula: ")
    director = input("Director: ")
    genero = input("Género: ")
    val = int(input("Valoracion"))
    
    nuevoLibro = {
        "Id": id,
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
            except json.JSONDecodeError as e:
                print("Error JSON: ", e)
            except ValueError as f:
                print(f)
            else:
                print("Pelicula agregada correctamente")
            finally:
                dato = []

def addMusic():
    id = int(input("Id: "))
    encontrar(id)
    titulo = input("Título de la musica: ")
    artista = input("Artista: ")
    genero = input("Género: ")
    val = int(input("Valoracion"))

    nuevoLibro = {
        "Id": id,
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
            except json.JSONDecodeError as e:
                print("Error JSON: ", e)
            except ValueError as f:
                print(f)
            else:
                print("Musica agregada correctamente")
            finally:
                dato = []

