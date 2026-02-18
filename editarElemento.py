import json

def ediTitulo():
    mensaje = """ 1.Titulo de Libro
    2. Titulo de Pelicula
    3. Titulo Musica
    4. Volver"""
    print(mensaje)

    op = int(input("Ingrese su opcion: "))
    if op == 1:
        with open("libros.json", "r") as f:
            datos = json.load(f)
        for dato in datos:
            print(f"Titulo: {dato['Titulo']}\n")

        nuevoTitulo = input("Nuevo titulo: ")
        with open("libros.json", "w") as f:
            dato['Titulo'] = nuevoTitulo
            json.dump(dato, f, indent=4)

