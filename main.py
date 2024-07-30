import os
import json
import pathlib

def clear_screen():
    if os.name == 'nt':  # 'nt' indica Windows
        os.system('cls')
    else:  # Unix/Linux/macOS tienen 'posix'
        os.system('clear')


def crear_leer_json(Archivo):
    if not pathlib.Path(Archivo).exists():
        with open(Archivo, 'w') as file:
            json.dump({}, file, indent=4)
            print(Archivo, "Se creo en la nube.")
            print("~"*100) 
    with open(Archivo, 'r') as file:
        print(Archivo, "Saltó de la nube y se estrello aqui.")
        print("~"*100) 
        return json.load(file)


def guardar_JSON (Diccionario,Archivo):
    try:
        with open(Archivo, 'w') as file:
            json.dump(Diccionario, file, indent=4)
            print("Datos guardados exitosamente!!")
            print("~"*100) 
    except Exception:
        print("Error al guardar datos")
        print("~"*100) 












