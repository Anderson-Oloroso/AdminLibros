import json
from menu import separador

def ediTitulo():
    mensaje = """ 1.Titulo de Libro
    2. Titulo de Pelicula
    3. Titulo Musica
    4. Volver"""
    print(mensaje)

    op = int(input("Ingrese su opcion: "))
    if op == 1:
        titulo = input("Título: ").lower().strip()

        with open("libros.json", "r") as f:
            datos = json.load(f)
        
        for i, dato in enumerate(datos):
            if titulo in dato['Titulo'].lower():
                print(f"\nTitulo encontrado.")
                nuevo = input("Ingerse el nuevo titulo para el libro: ")
                dato['Titulo'] = nuevo
                break
        
        with open("libros.json", "w") as f:
            json.dump(datos, f, indent=4)
            print("Libro modificado correctamente")

    elif op == 2:
        titulo = input("Título: ").lower().strip()

        with open("peliculas.json", "r") as f:
            datos = json.load(f)
        
        for i, dato in enumerate(datos):
            if titulo in dato['Titulo'].lower():
                print(f"\nTitulo encontrado.")
                nuevo = input("Ingerse el nuevo titulo para el libro: ")
                dato['Titulo'] = nuevo
                break

        with open("peliculas.json", "w") as f:
            json.dump(datos, f, indent=4)
            print("Pelicula modificada correctamente")
    
    elif op == 3:
        titulo = input("Título: ").lower().strip()

        with open("musicas.json", "r") as f:
            datos = json.load(f)
        
        for i, dato in enumerate(datos):
            if titulo in dato['Titulo'].lower():
                print(f"\nTitulo encontrado.")
                nuevo = input("Ingerse el nuevo titulo para el libro: ")
                dato['Titulo'] = nuevo
                break
        
        with open("musicas.json", "w") as f:
            json.dump(datos, f, indent=4)
            print("Musica modificada correctamente")
    else:
        print("Opcion invalida")

def editADA():
    mensaje = """ 1.Autor de Libro
    2. Autor de Pelicula
    3. Autor Musica
    4. Volver"""
    print(mensaje)

    op = int(input("Ingrese su opcion: "))
    if op == 1:
        titulo = input("Autor: ").lower().strip()

        with open("libros.json", "r") as f:
            datos = json.load(f)
        
        for i, dato in enumerate(datos):
            if titulo in dato['Autor'].lower():
                print(f"\nAutor encontrado.")
                nuevo = input("Ingerse el nuevo autor para el libro: ")
                dato['Autor'] = nuevo
                break
        
        with open("libros.json", "w") as f:
            json.dump(datos, f, indent=4)
            print("Libro modificado correctamente")

    elif op == 2:
        titulo = input("Director: ").lower().strip()

        with open("peliculas.json", "r") as f:
            datos = json.load(f)
        
        for i, dato in enumerate(datos):
            if titulo in dato['Director'].lower():
                print(f"\nDirector encontrado.")
                nuevo = input("Ingerse el nuevo Director para la pelicula: ")
                dato['Director'] = nuevo
                break

        with open("peliculas.json", "w") as f:
            json.dump(datos, f, indent=4)
            print("Pelicula modificada correctamente")
    
    elif op == 3:
        titulo = input("Artista: ").lower().strip()

        with open("musicas.json", "r") as f:
            datos = json.load(f)
        
        for i, dato in enumerate(datos):
            if titulo in dato['Artista'].lower():
                print(f"\nArtista encontrado.")
                nuevo = input("Ingerse el nuevo Artista para el libro: ")
                dato['Artista'] = nuevo
                break
        
        with open("musicas.json", "w") as f:
            json.dump(datos, f, indent=4)
            print("Musica modificada correctamente")

    else:
        print("Opcion invalida")

def editGen():
    mensaje = """ 1.Genero de Libro
    2. Genero de Pelicula
    3. Genero Musica
    4. Volver"""
    print(mensaje)

    op = int(input("Ingrese su opcion: "))
    if op == 1:
        titulo = input("Género: ").lower().strip()

        with open("libros.json", "r") as f:
            datos = json.load(f)
        
        for i, dato in enumerate(datos):
            if titulo in dato['Genero'].lower():
                print(f"\nGenero encontrado.")
                nuevo = input("Ingerse el nuevo género para el libro: ")
                dato['Genero'] = nuevo
                break
        
        with open("libros.json", "w") as f:
            json.dump(datos, f, indent=4)
            print("Libro modificado correctamente")

    elif op == 2:
        titulo = input("Genero: ").lower().strip()

        with open("peliculas.json", "r") as f:
            datos = json.load(f)
        
        for i, dato in enumerate(datos):
            if titulo in dato['Genero'].lower():
                print(f"\nGenero encontrado.")
                nuevo = input("Ingerse el nuevo Genero para la pelicula: ")
                dato['Genero'] = nuevo
                break

        with open("peliculas.json", "w") as f:
            json.dump(datos, f, indent=4)
            print("Pelicula modificada correctamente")
    
    elif op == 3:
        titulo = input("Genero: ").lower().strip()

        with open("musicas.json", "r") as f:
            datos = json.load(f)
        
        for i, dato in enumerate(datos):
            if titulo in dato['Genero'].lower():
                print(f"\nGenero encontrado.")
                nuevo = input("Ingerse el nuevo Artista para el libro: ")
                dato['Genero'] = nuevo
        
        with open("musicas.json", "w") as f:
            json.dump(datos, f, indent=4)
            print("Musica modificada correctamente")
    else:
        print("Opcion invalida")

def editVal():
    mensaje = """ 1.Valoracion de Libro
    2. Valoracion de Pelicula
    3. Valoracion Musica
    4. Volver"""
    print(mensaje)

    op = int(input("Ingrese su opcion: "))
    if op == 1:
        titulo = input("Libro a Valorar: ").lower().strip()

        with open("libros.json", "r") as f:
            datos = json.load(f)
        
        for i, dato in enumerate(datos):
            if titulo in dato['Titulo'].lower():
                print(f"\nLibro encontrado.")
                nuevo = input("Nueva valoracion para el libro: ")
                dato['Valoracion'] = nuevo
                break
        
        with open("libros.json", "w") as f:
            json.dump(datos, f, indent=4)
            print("Libro modificado correctamente")

    elif op == 2:
        titulo = input("Pelicula a valorar: ").lower().strip()

        with open("peliculas.json", "r") as f:
            datos = json.load(f)
        
        for i, dato in enumerate(datos):
            if titulo in dato['Titulo'].lower():
                print(f"\nPelicula encontrada.")
                nuevo = input("Nueva valoracion para la pelicula: ")
                dato['Valoracion'] = nuevo
                break

        with open("peliculas.json", "w") as f:
            json.dump(datos, f, indent=4)
            print("Pelicula modificada correctamente")
    
    elif op == 3:
        titulo = input("Musica a valorar: ").lower().strip()

        with open("musicas.json", "r") as f:
            datos = json.load(f)
        
        for i, dato in enumerate(datos):
            if titulo in dato['Titulo'].lower():
                print(f"\nMusica encontrada encontrado.")
                nuevo = input("Nueva valoracion para el libro: ")
                dato['Valoracion'] = nuevo
        
        with open("musicas.json", "w") as f:
            json.dump(datos, f, indent=4)
            print("Musica modificada correctamente")
    else:
        print("Opcion invalida")

def editarElemento():
    separador()
    print("       Editar Elemento")
    separador()
    print("¿Qué tipo de cambio deseas realizar?")
    opciones = """    1. Editar Titulo
    2. Editar Autor/Director/Artista
    3. Editar Genero
    4. Editar Valoracion
    5. Regresar al Menu Principal"""
    print(opciones)
    opEditar= int(input("Selecciona una opción (1-5): "))
    
    if opEditar == 1:
        ediTitulo()
    elif opEditar == 2:
        editADA()
    elif opEditar == 3:
        editGen()

    elif opEditar == 5:
        editarElemento()
    else:
        print("Opcion invalida")