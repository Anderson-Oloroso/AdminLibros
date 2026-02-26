import json
from menu import separador

def reporte_por_genero():
    separador()
    with open("libros.json", "r") as file:
        datos = json.load(file)
        
        elemntos = len(datos)
        separador()
        for dato in datos:
            if dato['Genero']:
                print(dato['Genero'])
                print(f"\nTitulo: {dato['Titulo']}\nAutor: {dato['Autor']}\nValoracion: {dato['Valoracion']}\n")

    with open("musicas.json", "r") as file2:
        datos2 = json.load(file2)
        elemntos = len(datos2)
        print(elemntos)
        separador()
        for dato in datos:
            if dato['Genero']:
                print(dato['Genero'])
                print(f"\nTitulo: {dato['Titulo']}\nAutor: {dato['Autor']}\nValoracion: {dato['Valoracion']}\n")

    with open("peliculas.json", "r") as file3:
        datos3 = json.load(file3)
        print(elemntos)
        print("Elementos",elemntos)
        separador()
        for dato in datos:
            elemntos = len(datos3)
            if dato['Genero']:
                print(dato['Genero'])
                print(f"\nTitulo: {dato['Titulo']}\nAutor: {dato['Autor']}\nValoracion: {dato['Valoracion']}\n")
