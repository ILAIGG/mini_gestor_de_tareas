import json
from datetime import datetime

ARCHIVO_TAREAS = "tareas.json"

def cargar_tareas():
    try:
        with open(ARCHIVO_TAREAS, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return []

def guardar_tareas(tareas):
    with open(ARCHIVO_TAREAS, "w") as f:
        json.dump(tareas, f, indent=4)
