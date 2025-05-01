import json

ARCHIVO_TAREAS = "tareas.json"

#Función para cargar las tareas desde el archivo JSON
def cargar_tareas():
    try:
        #Abre el archivo en modo lectura
        with open(ARCHIVO_TAREAS, "r") as f:
            return json.load(f)
        #En caso de que el archivo no exista o esté vacío, devuelve una lista vacía
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return []

#Función para guardar las tareas en el archivo JSON
def guardar_tareas(tareas):
    #Abre el archivo en modo escritura
    with open(ARCHIVO_TAREAS, "w") as f:
        json.dump(tareas, f, indent=4)

#Función para agregar una nueva tarea
def agregar_tarea(descripcion):
    tareas = cargar_tareas()
    tarea = {
        "descripcion": descripcion,
        "completada": False
    }
    tareas.append(tarea)
    guardar_tareas(tareas)
    print("Tarea agregada con éxito.")

#Función para marcar una tarea como completada o pendiente
def listar_tareas():
    tareas = cargar_tareas()
    if not tareas:
        print("No hay tareas registradas.")
        return
    for i, tarea in enumerate(tareas, start=1): #ennumerate devuelve un contador y el elemento de la lista (osea, tarea 1 = 1, tarea 2 = 2, etc)
        #Comprobamos si la tarea está completada o pendiente y lo mostramos en pantalla
        estado = "Completada" if tarea["completada"] else "Pendiente"
        #Imprimimos el índice de la tarea, su descripción y su estado
        print(f"{i}. {tarea['descripcion']} - {estado}")

#Función para marcar una tarea como completada (en este caso, simplemente cambia el estado de la tarea a completada)
def marcar_completada(indice):
    tareas = cargar_tareas()
    #Comprobamos que el índice esté dentro del rango de tareas
    #Si el índice es válido, marcamos la tarea como completada y guardamos los cambios en el archivo JSON
    if 0 <= indice < len(tareas):
        tareas[indice]["completada"] = True
        guardar_tareas(tareas)
        print("Tarea marcada como completada.")
    else:
        print("Índice inválido.")

#Función para eliminar una tarea con su índice correspondiente
def eliminar_tarea(indice):
    tareas = cargar_tareas()
    #Comprobamos que el índice esté dentro del rango de tareas
    #Si el índice es válido, eliminamos la tarea y guardamos los cambios en el archivo JSON
    if 0 <= indice < len(tareas):
        tarea_eliminada = tareas.pop(indice)
        guardar_tareas(tareas)
        print(f"Tarea '{tarea_eliminada['descripcion']}' eliminada.")
    else:
        print("Índice inválido.")

#Función principal que muestra el menú y gestiona la interacción con el usuario
def menu():
    while True:
        print("\nMINI GESTOR DE TAREAS")
        print("1. Agregar tarea.")
        print("2. Listar tareas.")
        print("3. Marcar tarea como completada.")
        print("4. Eliminar tarea.")
        print("5. Salir.")

        opcion = input("Elija una opción (1-5): ").strip() #strip elimina los espacios en blanco al principio y al final de la cadena
        #Validamos la opción ingresada por el usuario
        #Si la opción es 1, se pide la descripción de la tarea y se llama a la función agregar_tarea
        if opcion == "1":
            descripcion = input("Descripción de la tarea: ").strip()
            if descripcion:
                agregar_tarea(descripcion)
            else:
                print("La descripción no puede estar vacía.")
        #Si la opción es 2, se llama a la función listar_tareas para mostrar todas las tareas registradas
        elif opcion == "2":
            listar_tareas()
        #Si la opción es 3, se llama a la función listar_tareas y luego se pide el índice de la tarea a marcar como completada
        elif opcion == "3":
            listar_tareas()
            try:
                indice = int(input("Número de tarea a marcar como completada: ")) - 1
                marcar_completada(indice)
            except ValueError:
                print("Por favor, ingrese un número válido.")
        #Si la opción es 4, se llama a la función listar_tareas y luego se pide el índice de la tarea a eliminar
        elif opcion == "4":
            listar_tareas()
            try:
                indice = int(input("Número de tarea a eliminar: ")) - 1
                eliminar_tarea(indice)
            except ValueError:
                print("Por favor, ingrese un número válido.")
        #Si la opción es 5, se sale del bucle y se cierra el programa
        elif opcion == "5":
            print("Cerrando el gestor de tareas...")
            break
        else:
            print("Opción inválida.")

menu()
