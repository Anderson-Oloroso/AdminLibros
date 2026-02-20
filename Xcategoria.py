import json

def catLibro():
    mensaje = '''  1. Por Autor
    2. Por Genero
    3. Por puntuación
    4. Volver
    '''

    print(mensaje)
    with open("libros.json", "r") as f:
        datos = json.load(f)
    
    op = int(input("Ingrese una opcion: "))
    if op == 1:
        autor = input("Autor: ").strip().lower()
        existe = False
        for dato in datos:
            if autor in dato['Autor'].lower():
                print(f"\nTitulo: {dato['Titulo']}\nGénero: {dato['Genero']}\nPuntuación: {dato['Puntuacion']}\n")
                existe = True
        if not existe:
            print("No hay coincidencias")
    elif op == 2:
        genero = input("Genero: ").strip().lower()
        for dato in datos:
            if genero in dato['Genero'].lower():
                print(f"Titulo: {dato['Titulo']}\nAutor: {dato['Autor']}\nPuntuacion: {dato['Puntuacion']}\n")
    elif op == 3:
        puntuacion = input("Puntuacion: ").strip()
        for dato in datos:
            if puntuacion in dato['Puntuacion'].lower():
                print(f"Titulo: {dato['Titulo']}\nGénero: {dato['Genero']}\nAutor: {dato['Autor']}\n")
    else:
        print("Opcion invalida")

def catPeli():
    with open("peliculas.json", "r") as f:
        datos = json.load(f)
    
    mensaje = '''  1. Por Director
    2. Por Genero
    3. Por puntiación
    4. Volver
    '''

    print(mensaje)

    for dato in datos:
        print(f"Titulo: {dato['Titulo']}\nDirector: {dato['Director']}\nGénero: {dato['Genero']}\n")

def catMusic():
    with open("musicas.json", "r") as f:
        datos = json.load(f)
    
    mensaje = '''  1. Por Artista
    2. Por Genero
    3. Por puntiación
    4. Volver
    '''

    print(mensaje)
    op = int(input("Ingrese una opcion: "))
    for dato in datos:
        print(f"Titulo: {dato['Titulo']}\nArtista: {dato['Artista']}\nGénero: {dato['Genero']}\n")