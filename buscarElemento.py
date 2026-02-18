import json

def busTitulo():
    titulo = input("Título: ").lower()

    with open("libros.json", "r") as f:
        datos = json.load(f)
    
    for dato in datos:
        if titulo in dato['Titulo']:
            print(f"Titulo: {dato['Titulo']}\nAutor: {dato['Autor']}\nGénero: {dato['Genero']}\n")
            break
        