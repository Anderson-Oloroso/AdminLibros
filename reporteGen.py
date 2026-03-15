import json

def reporte_por_genero(clave_genero="genero"):

    contador = 0

    with open("libros.json", "r") as f:
        datos = json.load(f)  

        for item in datos:
            genero = item.get(clave_genero) 
            nombre = item['Genero']  
            if genero:  
                contador[genero] += 1
                nuevo ={
                    nombre:{
                        "Titulo": item['Titulo'],
                        "Autor": item['Autor'],
                        "Valoracion": item['Valoracion']
                    }
                }
    
    with open("reporte_generos.json", "w") as file:
        file.append(nuevo)