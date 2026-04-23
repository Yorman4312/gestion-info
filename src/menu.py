"""
menu.py
Este archivo contiene el menú interactivo para el programa.
Se utiliza try-except para manejar los errores
"""


# ---------------------------------- IMPORTACIONES ----------------------------------
from colorama import Fore, Style, Back, init # Para imprimir mensajes en colores
init(autoreset=True) # Para que los colores se restablezcan automáticamente después de cada impresión

from service import register_customer, view_customer, view_all_customers # Importamos las funciones del archivo service.py


# ---------------------------------- CÓDIGO PRINCIPAL ----------------------------------
# Función para mostrar el menú principal
def show_menu():
  print(Fore.BLUE + Style.BRIGHT + '============================== Menú Principal ==============================')
  print(Fore.BLUE + Style.BRIGHT + '1. Registrar cliente')
  print(Fore.BLUE + Style.BRIGHT + '2. Ver cliente por ID')
  print(Fore.BLUE + Style.BRIGHT + '3. Ver todos los clientes')
  print(Fore.BLUE + Style.BRIGHT + '4. Salir')
  print(Fore.BLUE + Style.BRIGHT + '==========================================================================\n')

  # Función para manejar la opción seleccionada por el usuario
def handle_option(option):
  # Opción 1: Registrar cliente
  if option == '1':
    try:
      print(Fore.BLUE + Style.BRIGHT + '\nRegistrando un nuevo cliente...')
      id = input('Ingrese el ID del cliente: ')
      name = input('Ingrese el nombre del cliente: ')
      email = input('Ingrese el email del cliente: ')
      phone = input('Ingrese el teléfono del cliente: ')

      if register_customer(id, name, email, phone): # Si el registro es exitoso, se muestra un mensaje de éxito
        print(Fore.GREEN + Style.BRIGHT + 'Cliente registrado exitosamente.\n')
      else:
        print(Fore.RED + Style.BRIGHT + 'Error al registrar el cliente.\n')
    except Exception as e:
      print(Fore.RED + Style.BRIGHT + f'Error al registrar el cliente: {e}\n')

# Opción 2: Ver cliente por ID
  elif option == '2':
    try:
      print(Fore.BLUE + Style.BRIGHT + '\nBuscando cliente por ID...')
      id = input('Ingrese el ID del cliente a buscar: ')
      customer = view_customer(id)

      if customer: # Si el cliente es encontrado, se muestra su información
        print(Fore.GREEN + Style.BRIGHT + f'Cliente encontrado: {customer.name} - {customer.email} - {customer.phone}\n')
      else:
        print(Fore.RED + Style.BRIGHT + 'Cliente no encontrado.\n')
    except Exception as e:
      print(Fore.RED + Style.BRIGHT + f'Error al buscar el cliente: {e}\n')

  # Opción 3: Ver todos los clientes
  elif option == '3':
    try:
      print(Fore.BLUE + Style.BRIGHT + '\nMostrando todos los clientes...')
      customers = view_all_customers()

      if customers: # Si hay clientes registrados, se muestra la información de cada uno
        for customer in customers:
          print(Fore.GREEN + Style.BRIGHT + f'Cliente: {customer.name} - {customer.email} - {customer.phone}\n')
      else:
        print(Fore.RED + Style.BRIGHT + 'No hay clientes registrados.\n')
    except Exception as e:
      print(Fore.RED + Style.BRIGHT + f'Error al mostrar los clientes: {e}\n')

  # Opción 4: Salir del programa
  elif option == '4':
    print(Fore.BLUE + Style.BRIGHT + 'Saliendo del programa...\n')

  else:
    print(Fore.RED + Style.BRIGHT + 'Opción no válida. Por favor, seleccione una opción del menú.\n')