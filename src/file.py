"""
file.py
Encargado de guardar y cargar los registros de los clientes desde un archivo JSON.
Se maneja la persistencia real de los datos y se usan rutas absolutas basadas en el proyecto.
"""


# ---------------------------------- IMPORTACIONES ----------------------------------
import json # Para trabajar con archivos JSON
from pathlib import Path
from colorama import Fore, Style, Back, init # Para imprimir mensajes en colores
init(autoreset=True) # Para que los colores se restablezcan automáticamente después de cada impresión


# ---------------------------------- CONFIGURACIÓN DE RUTA ----------------------------------
DATA_FILE = Path(__file__).resolve().parent.parent / 'data' / 'records.json'


def ensure_data_file():
    """Asegura que el directorio y el archivo de datos existan."""
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    if not DATA_FILE.exists():
        DATA_FILE.write_text('[]', encoding='utf-8')


# ---------------------------------- CÓDIGO PRINCIPAL ----------------------------------
"""
Función para cargar los clientes desde un archivo JSON:
- Si el archivo no existe, el programa lo crea con una lista vacía.
- Si el archivo está dañado, se muestra un mensaje de error y devuelve una lista vacía.
- El archivo se aloja en /gestion-info/data/records.json
"""
def load_data():
    ensure_data_file()
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as file:
            return json.load(file)
    except json.JSONDecodeError:
        print(Fore.RED + Style.BRIGHT + 'Error: El archivo de datos está dañado. Se creará un nuevo archivo.')
        with open(DATA_FILE, 'w', encoding='utf-8') as file:
            json.dump([], file, indent=4, ensure_ascii=False)
        return []
    except Exception as e:
        print(Fore.RED + Style.BRIGHT + f'Error al leer los datos: {e}')
        return []


"""
Función para guardar los clientes en el archivo JSON:
- Se guarda la lista de datos en formato JSON con indentación.
- El archivo se aloja en /gestion-info/data/records.json
"""
def save_data(data):
    ensure_data_file()
    try:
        with open(DATA_FILE, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
    except Exception as e:
        print(Fore.RED + Style.BRIGHT + f'Error al guardar los datos: {e}')
