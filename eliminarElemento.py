import json

def delNombre():
    titulo = input("Título: ").lower().strip()

    with open("libros.json", "r") as f:
        datos = json.load(f)
    
    for dato in datos:
        if titulo in dato['Titulo'].lower():
            print(f"\nTitulo encontrado\n")
    
    with open("peliculas.json", "r") as f:
        datos = json.load(f)
    
    for dato in datos:
        if titulo in dato['Titulo'].lower():
            print(f"\nTitulo: {dato['Titulo']}\nDirector: {dato['Director']}\nGénero: {dato['Genero']}\n")
    
    with open("musicas.json", "r") as f:
        datos = json.load(f)
    
    for dato in datos:
        if titulo in dato['Titulo'].lower():
            print(f"\nTitulo: {dato['Titulo']}\nArtista: {dato['Artista']}\nGénero: {dato['Genero']}\n")