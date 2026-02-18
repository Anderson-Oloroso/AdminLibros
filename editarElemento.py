import json

def ediTitulo():
    mensaje = """ 1.Titulo de Libro
    2. Titulo de Pelicula
    3. Titulo Musica
    4. Volver"""
    print(mensaje)

    op = int(input("Ingrese su opcion: "))
    if op == 1:
        titulo = input("Título: ").lower().strip()

        with open("libros.json", "r") as f:
            datos = json.load(f)
        
        for i, dato in enumerate(datos):
            if titulo in dato['Titulo'].lower():
                print(f"\nTitulo encontrado.")
                nuevo = input("Ingerse el nuevo titulo para el libro: ")
                dato['Titulo'] = nuevo
        
        with open("libros.json", "w") as f:
            json.dump(datos, f, indent=4)

        with open("musicas.json", "r") as f:
            datos = json.load(f)
        
        for i, dato in enumerate(datos):
            if titulo in dato['Titulo'].lower():
                print(f"\nTitulo encontrado.")
                nuevo = input("Ingerse el nuevo titulo para el libro: ")
                dato['Titulo'] = nuevo
        
        with open("musicas.json", "w") as f:
            json.dump(datos, f, indent=4)

        with open("libros.json", "r") as f:
            datos = json.load(f)
        
        for i, dato in enumerate(datos):
            if titulo in dato['Titulo'].lower():
                print(f"\nTitulo encontrado.")
                nuevo = input("Ingerse el nuevo titulo para el libro: ")
                print(i)
                print(nuevo)
                dato['Titulo'] = nuevo
        
        with open("libros.json", "w") as f:
            json.dump(datos, f, indent=4)
