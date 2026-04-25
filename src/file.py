"""
file.py
Gestiona la persistencia de clientes en JSON.
Contiene funciones para leer y escribir el archivo de datos en el directorio data/.
"""


# ---------------------------------- IMPORTACIONES ----------------------------------
import json # Para trabajar con archivos JSON
from pathlib import Path
from colorama import Fore, Style, Back, init # Para imprimir mensajes en colores
init(autoreset=True) # Inicializa colorama para restablecer estilos automáticamente


# ---------------------------------- CONFIGURACIÓN DE RUTA ----------------------------------
DATA_FILE = Path(__file__).resolve().parent.parent / 'data' / 'records.json'


def ensure_data_file():
  """Asegura que el directorio y el archivo JSON existen antes de leer o escribir."""
  DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
  if not DATA_FILE.exists():
    DATA_FILE.write_text('[]', encoding='utf-8')


def load_data():
  """Carga los datos de clientes desde records.json y devuelve una lista de diccionarios."""
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


def save_data(data):
  """Guarda la lista de clientes en el archivo JSON con indentación legible."""
  ensure_data_file()
  try:
    with open(DATA_FILE, 'w', encoding='utf-8') as file:
      json.dump(data, file, indent=4, ensure_ascii=False)
  except Exception as e:
    print(Fore.RED + Style.BRIGHT + f'Error al guardar los datos: {e}')
