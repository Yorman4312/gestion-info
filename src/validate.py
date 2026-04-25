"""
validate.py
Contiene las reglas de validación para los campos de cliente.
Verifica unicidad de ID/email y formatea los datos antes de guardarlos.
"""


# ---------------------------------- IMPORTACIONES ----------------------------------
from colorama import Fore, Style, Back, init # Para imprimir mensajes en colores
init(autoreset=True) # Inicializa colorama para restablecer estilos automáticamente

import re # Para usar expresiones regulares en la validación de correo electrónico


# ---------------------------------- CÓDIGO PRINCIPAL ----------------------------------
# Función Set para validar los datos de los clientes:
def validate_customer(customers, id, name, email, phone, current_id=None):
  # ----- Validación de IDs y Emails -----
  set_ids = set() # Creamos un conjunto para almacenar los IDs únicos de los clientes
  set_emails = set() # Creamos un conjunto para almacenar los emails únicos de los clientes

  for c in customers: # Recorremos la lista de clientes y agregamos sus IDs y emails a los conjuntos correspondientes
    set_ids.add(c.id) # Agregamos el ID del cliente al conjunto de IDs
    set_emails.add(c.email) # Agregamos el email del cliente al conjunto de emails
    # Ignorar el mismo cliente en caso de actualización
    if current_id and c.id == current_id: # Si se está actualizando un cliente, ignoramos su propio ID y email en la validación
      set_ids.remove(c.id) # Eliminamos el ID del cliente actual del conjunto de IDs para permitir que se mantenga igual
      set_emails.remove(c.email) # Eliminamos el email del cliente actual del conjunto de emails para permitir que se mantenga igual

  # ----- Validaciones básicas -----
  # ID: No puede estar vacío, debe ser único y no puede contener espacios.
  if not id.strip(): # Verificamos que el ID no esté vacío o solo contenga espacios
    print(Fore.RED + Style.BRIGHT + 'Error: El ID no puede estar vacío.') # Imprimimos un mensaje de error en rojo
    return False
  if id in set_ids: # Si el ID ya existe en el conjunto de IDs, se muestra un mensaje de error y se retorna False
    print(Fore.RED + Style.BRIGHT + f'Error: El ID del cliente {id} ya existe. Por favor, ingrese un ID único.')
    return False
  
  # Name: No puede estar vacío, no puede contener solo espacios y no puede contener números
  if not name.strip(): # Verificamos que el nombre no esté vacío o solo contenga espacios
    print(Fore.RED + Style.BRIGHT + 'Error: El nombre no puede estar vacío.') # Imprimimos un mensaje de error en rojo
    return False
  if not name.replace(" ", "").isalpha(): # Verificamos que el nombre no contenga números
    print(Fore.RED + Style.BRIGHT + 'Error: El nombre no puede contener números.') # Imprimimos un mensaje de error en rojo
    return False

  # Email: No puede estar vacío, debe ser único, no puede contener espacios y debe tener un formato válido (@, .com, etc.)
  regex = r'^[\w\.-]+@[\w\.-]+\.\w+$' # Expresión regular para validar el formato del email
  if not email.strip(): # Verificamos que el email no esté vacío o solo contenga espacios
    print(Fore.RED + Style.BRIGHT + 'Error: El email no puede estar vacío.') # Imprimimos un mensaje de error en rojo
    return False
  if email in set_emails: # Si el email ya existe en el conjunto de emails, se muestra un mensaje de error y se retorna False
    print(Fore.RED + Style.BRIGHT + f'Error: El email del cliente {email} ya existe. Por favor, ingrese un email único.')
    return False
  if not re.match(regex, email): # Verificamos que el email tenga un formato válido
    print(Fore.RED + Style.BRIGHT + f'Error: El email del cliente {email} no tiene un formato válido.') # Imprimimos un mensaje de error en rojo
    return False
  
  # Phone: No puede estar vacío, no puede contener solo espacios, debe contener solo números y debe tener una longitud mínima de 7 dígitos
  if not phone.strip(): # Verificamos que el teléfono no esté vacío o solo contenga espacios
    print(Fore.RED + Style.BRIGHT + 'Error: El teléfono no puede estar vacío.') # Imprimimos un mensaje de error en rojo
    return False
  if not phone.isdigit(): # Verificamos que el teléfono contenga solo números
    print(Fore.RED + Style.BRIGHT + 'Error: El teléfono solo puede contener números.') # Imprimimos un mensaje de error en rojo
    return False
  if len(phone) < 7: # Verificamos que el teléfono tenga una longitud mínima de 7 dígitos
    print(Fore.RED + Style.BRIGHT + 'Error: El teléfono debe tener al menos 7 dígitos.') # Imprimimos un mensaje de error en rojo
    return False
    
  return True