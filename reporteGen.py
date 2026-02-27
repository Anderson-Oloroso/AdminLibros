import json
from menu import separador

def reporte_por_genero():
    separador()
    generos = []
    with open("libros.json", "r") as file:
        datos = json.load(file)
        for _ in datos:
            print(f"{_['Genero']}")
            if _['Genero'] not in generos:
                generos.append(_['Genero'])
        cont = 1
        while cont != len(generos):
            for _ in generos:
                print(_) 
            cont += 1
        
        separador()

    with open("musicas.json", "r") as file2:
        datos2 = json.load(file2)
        for _ in datos2:
            print(f"{_['Genero']}")
        separador()

    with open("peliculas.json", "r") as file3:
        datos3 = json.load(file3)
        for _ in datos3:
            print(f"{_['Genero']}")
        separador()
