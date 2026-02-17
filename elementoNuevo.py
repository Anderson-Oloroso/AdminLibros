import json
from main import nuevoElemento

def libro():
    id = int(input("Id: "))
    titulo = input("Título del libro: ")
    autor = input("Autor: ")
    genero = input("Género: ")

    
op = nuevoElemento    

if op == 1:
    with open("libros.json", "r") as f:
        dato = json.load(f)
        _ = 0
        for _ in dato:
            print(dato)
