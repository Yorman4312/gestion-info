"""
integration.py
Contiene la lógica de generación de registros automáticos.
Incluye la creación de clientes aleatorios y su registro en el archivo JSON.
"""

# ---------------------------------- IMPORTACIONES ----------------------------------
import random
import string
from colorama import Fore, Style, Back, init
init(autoreset=True)

from .service import Customer, customers, new_customer


# ---------------------------------- GENERACIÓN ALEATORIA ----------------------------------

# Funciones de soporte para crear datos de clientes sin interacción manual.
# Estas funciones se diseñan para producir valores válidos y evitar duplicados.
def random_name(*args, **kwargs):
  """Genera un nombre completo aleatorio.

  args se usa para incluir nombres o apellidos adicionales.
  kwargs permite activar nombres medios o cambiar el formato.
  """
  first_names = ['Ana', 'Luis', 'Carlos', 'María', 'Sofía', 'Javier', 'Lucía', 'Diego', 'Sara', 'Pedro']
  last_names = ['Gómez', 'Pérez', 'Rodríguez', 'López', 'Martínez', 'Torres', 'Ramírez', 'Hernández', 'García', 'Flores']
  middle_names = ['Alejandro', 'Isabel', 'Fernando', 'Valeria', 'Andrés', 'Camila']

  # Combina nombre y apellido aleatorios.
  parts = [random.choice(first_names), random.choice(last_names)]

  # Si el usuario solicita un segundo nombre, se inserta antes del apellido.
  if kwargs.get('use_middle_name', False):
    parts.insert(1, random.choice(middle_names))

  # Si se pasan args adicionales, se anexan al final del nombre.
  if args:
    parts.extend(str(arg).title() for arg in args)

  return ' '.join(parts)


def random_email(name, **kwargs):
  """Genera un email basado en el nombre y un dominio aleatorio."""
  domain = kwargs.get('domain', 'example.com')
  username = name.lower().replace(' ', '.')
  suffix = random.choice(['', str(random.randint(1, 99))])
  return f'{username}{suffix}@{domain}'


def random_phone(**kwargs):
  """Genera un número de teléfono aleatorio válido."""
  prefix = kwargs.get('phone_prefix', '3')
  digits = ''.join(random.choices(string.digits, k=9))
  return prefix + digits


def random_id(existing_ids, **kwargs):
  """Genera un ID único basado en el conjunto de IDs existentes."""
  prefix = kwargs.get('id_prefix', 'C')
  length = kwargs.get('id_length', 5)
  alphabet = string.ascii_uppercase + string.digits

  # Genera IDs hasta encontrar uno que no exista en el archivo actual.
  while True:
    candidate = prefix + ''.join(random.choices(alphabet, k=length))
    if candidate not in existing_ids:
      return candidate


def create_random_customer(*args, **kwargs):
  """Crea un cliente aleatorio usando args y kwargs para personalizar la generación."""
  current_ids = {c.id for c in customers}

  # Permite sobreescribir valores si se pasan kwargs.
  name = kwargs.get('name') or random_name(*args, **kwargs)
  customer_id = kwargs.get('id') or random_id(current_ids, **kwargs)
  email = kwargs.get('email') or random_email(name, **kwargs)
  phone = kwargs.get('phone') or random_phone(**kwargs)
  return Customer(customer_id, name, email, phone)


def add_random_customers(quantity=10, *args, **kwargs):
  """Genera y agrega clientes aleatorios al archivo JSON.

  Devuelve la lista de clientes creados.
  """
  created_customers = []
  attempts = 0

  # Se intenta crear hasta `quantity` clientes. Se limita la cantidad de intentos para evitar bucles infinitos.
  while len(created_customers) < quantity and attempts < quantity * 5:
    attempts += 1
    customer = create_random_customer(*args, **kwargs)
    if new_customer(customer.id, customer.name, customer.email, customer.phone):
      created_customers.append(customer)

  return created_customers


# ---------------------------------- USO PRINCIPAL ----------------------------------
if __name__ == '__main__':
  added = add_random_customers(10)
  if added:
    print(Fore.GREEN + Style.BRIGHT + f'Se generaron y agregaron {len(added)} clientes aleatorios al archivo JSON.')
  else:
    print(Fore.YELLOW + Style.BRIGHT + 'No se pudieron generar clientes aleatorios. Verifique los datos actuales.')
