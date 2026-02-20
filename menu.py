def separador():
    print("===========================================")

def opcionesMenu():
    
    menu ="""        1. Añadir un Nuevo Elemento
        2. Ver Todos los Elementos
        3. Buscar un Elemento
        4. Editar un Elemento
        5. Eliminar un Elemento
        6. Ver Elementos por Categoría
        7. Salir"""
    print(menu)

def opc():
    op = int(input("Selecciona una opción (1-7): "))
    return op