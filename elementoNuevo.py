from json import *

def libro(op):
    id = int(input("Id: "))
    titulo = input("Título del libro: ")
    autor = input("Autor: ")
    genero = input("Género: ")

    if op == 1:
        with open("libros.json", "r") as f:
            dato = load(f)
            for _ in dato:
                print(_)

