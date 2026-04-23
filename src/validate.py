"""
validate.py
Este archivo contiene las funciones de validación para los datos de los clientes.
"""

# ---------------------------------- IMPORTACIONES ----------------------------------
from colorama import Fore, Style, Back, init # Para imprimir mensajes en colores
init(autoreset=True) # Para que los colores se restablezcan automáticamente después de cada impresión

# ---------------------------------- CÓDIGO PRINCIPAL ----------------------------------
# Función Set para validar que los IDs y Correos no se dupliquen
def validate_customer(customers, id, email):
  for c in customers:
    if c.id == id:
      print(Fore.RED + Style.BRIGHT + 'Error: El ID del cliente ya existe. Por favor, ingrese un ID único.')
      return False
    if c.email == email:
      print(Fore.RED + Style.BRIGHT + 'Error: El email del cliente ya existe. Por favor, ingrese un email único.')
      return False
  return True