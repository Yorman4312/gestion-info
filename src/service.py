"""
service.py
Este archivo contiene las funciones CRUD del programa.
"""

# ---------------------------------- IMPORTACIONES ----------------------------------
from colorama import Fore, Style, Back, init # Para imprimir mensajes en colores
init(autoreset=True) # Para que los colores se restablezcan automáticamente después de

from validate import validate_customer # Importamos la función de validación desde el archivo validate.py

# ---------------------------------- CÓDIGO PRINCIPAL ----------------------------------
# Listado de clientes
customers = []

# Módelo de cliente
class Customer:
  def __init__(self, id, name, email, phone):
    self.id = id
    self.name = name
    self.email = email
    self.phone = phone

# ----- Función para registrar un cliente -----
def register_customer(id, name, email, phone):
  if validate_customer(customers, id, email): # Si la validación es exitosa, se registra el cliente
    new_customer = Customer(id, name, email, phone)
    customers.append(new_customer)
    return True
  return False

# ----- Función para ver un cliente por ID -----
def view_customer(id):
  for customer in customers:
    if customer.id == id:
      return customer
  return None

# ----- Función para ver todos los clientes -----
def view_all_customers():
  return customers