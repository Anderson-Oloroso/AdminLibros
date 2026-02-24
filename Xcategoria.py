import json
from menu import separador

def catLibro():
    mensaje = '''   1. Por Autor
    2. Por Genero
    3. Por Valoracion
    4. Volver
    '''
    separador()
    print(mensaje)
    with open("libros.json", "r") as f:
        datos = json.load(f)
    existe = False
    op = int(input("Ingrese una opcion: "))
    if op == 1:
        separador()
        autor = input("Autor: ").strip().lower()
        separador()
        for dato in datos:
            if autor in dato['Autor'].lower():
                print(f"\nTitulo: {dato['Titulo']}\nGénero: {dato['Genero']}\nValoracion: {dato['Valoracion']}\n")
                existe = True
        if not existe:
            print("Autor no encontrado")
    elif op == 2:
        separador()
        genero = input("Genero: ").strip().lower()
        separador()
        for dato in datos:
            if genero in dato['Genero'].lower():
                print(f"Titulo: {dato['Titulo']}\nAutor: {dato['Autor']}\nValoracion: {dato['Valoracion']}\n")
                existe = True
        if not existe:
            print("Genero no encontrado")
    elif op == 3:
        separador()
        valoracion = float(input("Valoracion: "))
        separador()
        for dato in datos:
            if dato['Valoracion'] == valoracion:
                print(f"Titulo: {dato['Titulo']}\nGénero: {dato['Genero']}\nAutor: {dato['Autor']}\n")
                existe = True
        if not existe:
            print("Valoracion no encontrada")
    elif op == 4:
        return
    else:
        separador()
        print("Opcion invalida")

def catPeli():
    mensaje = '''  1. Por Director
    2. Por Genero
    3. Por Valoracion
    4. Volver
    '''
    separador()
    print(mensaje)

    with open("peliculas.json", "r") as f:
        datos = json.load(f)

    existe = False
    op = int(input("Ingrese una opcion: "))
    if op == 1:
        separador()
        director = input("Director: ").strip().lower()
        separador()
        for dato in datos:
            if director in dato['Director'].lower():
                print(f"\nTitulo: {dato['Titulo']}\nGénero: {dato['Genero']}\nValoracion: {dato['Valoracion']}\n")
                existe = True
        if not existe:
            print("Director no encontrado")
    elif op == 2:
        separador()
        genero = input("Genero: ").strip().lower()
        separador()
        for dato in datos:
            if genero in dato['Genero'].lower():
                print(f"Titulo: {dato['Titulo']}\nDirector: {dato['Director']}\nValoracion: {dato['Valoracion']}\n")
                existe = True
        if not existe:
            print("Genero no encontrado")
    elif op == 3:
        separador()
        valoracion = float(input("Valoracion: "))
        separador()
        for dato in datos:
            if dato['Valoracion'] == valoracion:
                print(f"Titulo: {dato['Titulo']}\nGénero: {dato['Genero']}\nDirector: {dato['Director']}\n")
                existe = True
        if not existe:
            print("Valoracion no encontrada")
    elif op == 4:
        return
    else:
        separador
        print("Opcion invalida")

def catMusic():
    mensaje = '''  1. Por Artista
    2. Por Genero
    3. Por Valoracion
    4. Volver'''
    separador()
    print(mensaje)
    with open("musicas.json", "r") as f:
        datos = json.load(f)

    existe = False
    op = int(input("Ingrese una opcion: "))
    if op == 1:
        separador()
        artista = input("Artista: ").strip().lower()
        separador()
        for dato in datos:
            if artista in dato['Artista'].lower():
                print(f"\nTitulo: {dato['Titulo']}\nGénero: {dato['Genero']}\nValoracion: {dato['Valoracion']}\n")
                existe = True
        if not existe:
            print("Artista no encontrado")
    elif op == 2:
        separador()
        genero = input("Genero: ").strip().lower()
        separador()
        for dato in datos:
            if genero in dato['Genero'].lower():
                print(f"Titulo: {dato['Titulo']}\nArtista: {dato['Artista']}\nValoracion: {dato['Valoracion']}\n")
                existe = True
        if not existe:
            print("Genero no encontrado")
    elif op == 3:
        separador()
        valoracion = float(input("Valoracion: "))
        separador()
        for dato in datos:
            if dato['Valoracion'] == valoracion:
                print(f"Titulo: {dato['Titulo']}\nGénero: {dato['Genero']}\nArtista: {dato['Artista']}\n")
                existe = True
        if not existe:
            print("Valoracion no encontrada")
    elif op == 4:
        return
    else:
        separador()
        print("Opcion invalida")
        