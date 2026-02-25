import json
from menu import separador

def addLibro():
    separador
    print("Agregar un nuevo libro")
    titulo = input("Título del libro: ").strip()
    autor = input("Autor: ").strip()
    genero = input("Género: ")
    val = float(input("Valoracion: "))
    encontrado = False
    nuevoLibro = {
        "Titulo": titulo,
        "Autor": autor,
        "Genero": genero,
        "Valoracion": val
    }
    with open("libros.json", "r") as file:
        datos = json.load(file)

        for dato in datos:
            if titulo.lower() in dato['Titulo'].lower() and autor.lower() in dato['Autor'].lower():
                encontrado = True
                break
    
    if encontrado:
        separador()
        print("El libro que intenta agregar ya existe\n")
    else:
        datos.append(nuevoLibro)
        with open("libros.json", "w") as f:
            try:
                json.dump(datos, f, indent=4)
            except Exception as e:
                 print("Error: ", e)
            else:
                print("\nLibro agregado correctamente")

def addPeli():
    separador()
    print("Agregar nueva pelicula")
    titulo = input("Título de la pelicula: ").strip()
    director = input("Director: ").strip()
    genero = input("Género: ")
    val = float(input("Valoracion: "))
    encontrado = False
    nuevaPeli= {
        "Titulo": titulo,
        "Director": director,
        "Genero": genero,
        "Valoracion": val
    }
    with open("peliculas.json", "r") as file:
        datos = json.load(file)
        for dato in datos:
            if titulo.lower() in dato['Titulo'].lower() and director.lower() in dato['Director'].lower():
                encontrado = True
                break
    
    if encontrado:
        separador()
        print("La pelicula que intenta agregar ya existe\n")
    else:
        datos.append(nuevaPeli)
        with open("peliculas.json", "w") as f:
            try:
                json.dump(datos, f, indent=4)
            except Exception as e:
                 print("Error: ", e)
            else:
                print("\nPelicula agregada correctamente")

def addMusic():
    separador()
    print("Agregar nueva musica")
    titulo = input("Título de la musica: ").strip()
    artista = input("Artista: ").strip()
    genero = input("Género: ")
    val = float(input("Valoracion: "))
    encontrado = True
    nuevaMusica = {
        "Titulo": titulo,
        "Artista": artista,
        "Genero": genero,
        "Valoracion": val
    }
    with open("musicas.json", "r") as file:
        datos = json.load(file)
        for dato in datos:
            if titulo.lower() in dato['Titulo'].lower() and artista.lower() in dato['Artista'].lower():
                encontrado = True
                break
    
    if encontrado:
        separador()
        print("La música que intenta agregar ya existe\n")
    else:
        datos.append(nuevaMusica)
        with open("musicas.json", "w") as f:
            try:
                json.dump(datos, f, indent=4)
            except Exception as e:
                 print("Error: ", e)
            else:
                print("\nPelicula agregada correctamente")
