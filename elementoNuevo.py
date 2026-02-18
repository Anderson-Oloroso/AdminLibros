import json

def addLibro():
    id = int(input("Id: "))
    titulo = input("Título del libro: ")
    autor = input("Autor: ")
    genero = input("Género: ")

    nuevoLibro = {
        "Id": id,
        "Titulo": titulo,
        "Autor": autor,
        "Genero": genero
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
    titulo = input("Título de la pelicula: ")
    director = input("Director: ")
    genero = input("Género: ")

    nuevoLibro = {
        "Id": id,
        "Titulo": titulo,
        "Director": director,
        "Genero": genero
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
    titulo = input("Título de la musica: ")
    artista = input("Artista: ")
    genero = input("Género: ")

    nuevoLibro = {
        "Id": id,
        "Titulo": titulo,
        "Artista": artista,
        "Genero": genero
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

