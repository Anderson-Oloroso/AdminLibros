import json

mensaje = """ 1.Titulo de Libro
    2. Titulo de Pelicula
    3. Titulo Musica
    4. Volver"""

def ediTitulo():
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
        
        with open("libro.json", "w") as f:
            json.dump(datos, f, indent=4)
            print("Libro modificado correctamente")

    elif op == 2:
        titulo = input("Título: ").lower().strip()

        with open("peliculas.json", "r") as f:
            datos = json.load(f)
        
        for i, dato in enumerate(datos):
            if titulo in dato['Titulo'].lower():
                print(f"\nTitulo encontrado.")
                nuevo = input("Ingerse el nuevo titulo para el libro: ")
                dato['Titulo'] = nuevo

        with open("peliculas.json", "w") as f:
            json.dump(datos, f, indent=4)
            print("Pelicula modificada correctamente")
    
    elif 3:
        titulo = input("Título: ").lower().strip()

        with open("musicas.json", "r") as f:
            datos = json.load(f)
        
        for i, dato in enumerate(datos):
            if titulo in dato['Titulo'].lower():
                print(f"\nTitulo encontrado.")
                nuevo = input("Ingerse el nuevo titulo para el libro: ")
                dato['Titulo'] = nuevo
        
        with open("musicas.json", "w") as f:
            json.dump(datos, f, indent=4)
            print("Musica modificada correctamente")
    else:
        print("Opcion invalida")

def editADA():
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
        
        with open("libro.json", "w") as f:
            json.dump(datos, f, indent=4)
            print("Libro modificado correctamente")

    elif op == 2:
        titulo = input("Título: ").lower().strip()

        with open("peliculas.json", "r") as f:
            datos = json.load(f)
        
        for i, dato in enumerate(datos):
            if titulo in dato['Titulo'].lower():
                print(f"\nTitulo encontrado.")
                nuevo = input("Ingerse el nuevo titulo para el libro: ")
                dato['Titulo'] = nuevo

        with open("peliculas.json", "w") as f:
            json.dump(datos, f, indent=4)
            print("Pelicula modificada correctamente")
    
    elif 3:
        titulo = input("Título: ").lower().strip()

        with open("musicas.json", "r") as f:
            datos = json.load(f)
        
        for i, dato in enumerate(datos):
            if titulo in dato['Titulo'].lower():
                print(f"\nTitulo encontrado.")
                nuevo = input("Ingerse el nuevo titulo para el libro: ")
                dato['Titulo'] = nuevo
        
        with open("musicas.json", "w") as f:
            json.dump(datos, f, indent=4)
            print("Musica modificada correctamente")
    else:
        print("Opcion invalida")