"""Módulo de gestión de tareas.

Permite crear, listar, completar y eliminar tareas, y guardarlas
y cargarlas desde un archivo JSON.
"""

import json
import os

ARCHIVO = "tareas.json"


def cargar_tareas(ruta=ARCHIVO):
    """Carga las tareas desde un archivo JSON.

    Args:
        ruta (str): Ruta del archivo JSON.

    Returns:
        list: Lista de tareas (diccionarios). Vacía si el archivo no existe.
    """
    if not os.path.exists(ruta):
        return []
    with open(ruta, "r", encoding="utf-8") as f:
        return json.load(f)


def guardar_tareas(tareas, ruta=ARCHIVO):
    """Guarda la lista de tareas en un archivo JSON.

    Args:
        tareas (list): Lista de tareas a guardar.
        ruta (str): Ruta del archivo JSON.
    """
    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(tareas, f, indent=4, ensure_ascii=False)


def anadir_tarea(tareas, titulo):
    """Añade una nueva tarea pendiente.

    Args:
        tareas (list): Lista actual de tareas.
        titulo (str): Título de la nueva tarea.

    Returns:
        dict: La tarea creada.
    """
    nueva = {"id": len(tareas) + 1, "titulo": titulo, "completada": False}
    tareas.append(nueva)
    return nueva


def completar_tarea(tareas, id_tarea):
    """Marca una tarea como completada.

    Args:
        tareas (list): Lista actual de tareas.
        id_tarea (int): Identificador de la tarea.

    Returns:
        bool: True si se encontró y completó la tarea, False si no existe.
    """
    for tarea in tareas:
        if tarea["id"] == id_tarea:
            tarea["completada"] = True
            return True
    return False


def eliminar_tarea(tareas, id_tarea):
    """Elimina una tarea por su identificador.

    Args:
        tareas (list): Lista actual de tareas.
        id_tarea (int): Identificador de la tarea.

    Returns:
        bool: True si se eliminó, False si no existe.
    """
    for tarea in tareas:
        if tarea["id"] == id_tarea:
            tareas.remove(tarea)
            return True
    return False