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

