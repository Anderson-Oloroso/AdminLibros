from menu import *
from json import *
from elementoNuevo import *
from verElemento import *
from editarElemento import *
from buscarElemento import *


def nuevoElemento():
    separador()
    print("       Añadir nuevo Elemento")
    separador()
    print("¿Qué tipo de elemento desea añadir?")
    opciones = """    1. Libro
    2. Pelicula
    3. Musica
    4. Regresar al Menu Principal"""
    print(opciones)
    opNuevo = int(input("Selecciona una opción (1-4): "))

    separador()
    print("Agregar un nuevo elemento\n")
    if opNuevo == 1:
        addLibro()
    elif opNuevo == 2:
        addPeli()
    elif opNuevo == 3:
        addMusic()
    elif opNuevo == 4:
        main()

def verElementos():
    separador()
    print("       Ver todos los Elementos")
    separador()
    print("¿Qué categoria deseas ver?")
    opciones = """    1. Ver todos los Libros
    2. Ver todas las Peliculas
    3. Ver toda la Musica
    4. Regresar al Menu Principal"""
    print(opciones)
    opVer = int(input("Selecciona una opción (1-4):"))
    separador()
    print("Ver todos los registros\n")
    if opVer == 1:
        verLibro()
    elif opVer == 2:
        verPeli()
    elif opVer == 3:
        verMusic()
    elif opVer == 4:
        main()

def buscarElemento():
    separador()
    print("       Buscar un Elemento")
    separador()
    print("¿Qué deseas buscar?")
    opciones = """    1. Buscar por Titulo
    2. Buscar por Autor/Director/Artista
    3. Buscar por Genero
    4. Regresar al Menu Principal"""
    print(opciones)
    opBuscar = int(input("Selecciona una opción (1-4):"))
    if opBuscar == 1:
        busTitulo()
    elif opBuscar == 2:
        busADA()
    elif opBuscar == 3:
        busGen()
    elif opBuscar == 4:
        main()
    else:
        print("Opcion inválida")

def eliminarElemento():
    separador()
    print("       Eliminar Elemento")
    separador()
    print("¿Que deseas eliminar?")
    opciones = """    1. Eliminar por Titulo
    2. Eliminar por Identificador único
    3. Regresar al Menu Principal"""
    print(opciones)
    opEliminar = int(input("Selecciona una opción (1-3):"))
    try:
        return(opEliminar)
    except Exception:
        print("Opción inválida")

def elementoXcategoria():
    separador()
    print("       Ver Elementos por Categoria")
    separador()
    print("¿Que deseas ver?")
    opciones = """    1. Ver Libros
    2. Ver Películas
    3. Ver Música
    4. Regresar al Menu Principal"""
    print(opciones)
    opCategoria = int(input("Selecciona una opción (1-4):"))
    try:
        return(opCategoria)
    except Exception:
        print("Opción inválida")

def guardarCargar():
    separador()
    print("       Guardar y Cargar Colección")
    separador()
    print("¿Que deseas hacer")
    opciones = """    1. Guardar la Colección Actual
    2. Cargar una colección Guardada
    3. Regresar al Menu Principal"""
    print(opciones)
    opCategoria = int(input("Selecciona una opción (1-3):"))
    try:
        return(opCategoria)
    except Exception:
        print("Opción inválida")

def main():
    separador()
    print("       Administrador de coleccion")
    separador()
    opcionesMenu()
    separador()
    op = opc()
    while True:
        if op == 1:
            print("")
            nuevoElemento()
        elif op == 2:
            print("")
            verElementos()
        elif op == 3:
            print("")
            buscarElemento()
        elif op == 4:
            print("")
            editarElemento()
        elif op == 5:
            print("")
            eliminarElemento()
        elif op == 6:
            print("")
            elementoXcategoria()
        elif op == 7:
            print("")
            guardarCargar()
        elif op == 8:
            break
        else:
            print("")
            print("Opción inválida")
            main()

main()    

