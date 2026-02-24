import json
from menu import separador
def delNombre():
    separador()
    titulo = input("Titulo: ").lower().strip()
    encontrado = False
    try:
        i = 0
        with open("libros.json", "r") as f:
            datos = json.load(f)

        while i < len(datos):
            if 'Titulo' in datos[i] and titulo in datos[i]['Titulo'].lower():
                datos.pop(i)
                encontrado = True
            i+=1
        with open("libros.json", "w") as f:
            datos = json.dump(datos, f, indent=4)
        
    except: pass

    try:
        i = 0
        with open("musicas.json", "r") as f:
            datos = json.load(f)

        while i < len(datos):
            if 'Titulo' in datos[i] and titulo in datos[i]['Titulo'].lower():
                datos.pop(i)
                encontrado = True
            i += 1
        
        with open("musicas.json", "w") as f:
            datos = json.dump(datos, f, indent=4)
        
    except: pass

    try:
        i = 0
        with open("peliculas.json", "r") as f:
            datos = json.load(f)
        
        while i < len(datos):
            if 'Titulo' in datos[i] and titulo in datos[i]['Titulo'].lower():
                datos.pop(i)
                encontrado = True
            i += 1
            
        with open("peliculas.json", "w") as f:
            datos = json.dump(datos, f, indent=4)
        
    except: pass

    if not encontrado:
        print("Titulo no encontrado")
    else:
        print("Eliminacion completada")