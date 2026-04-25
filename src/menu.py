"""
menu.py
Proporciona el menú interactivo y redirige las opciones del usuario a la lógica de negocio.
"""


# ---------------------------------- IMPORTACIONES ----------------------------------
from colorama import Fore, Style, Back, init # Para imprimir mensajes en colores
init(autoreset=True) # Inicializa colorama para restablecer estilos automáticamente

from service import new_customer, search_customer, list_customers, update_customer, delete_customer


# ---------------------------------- CÓDIGO PRINCIPAL ----------------------------------

def show_menu():
  print(Fore.BLUE + Style.BRIGHT + '============================== Menú Principal ==============================')
  print(Fore.BLUE + Style.BRIGHT + '1. Registrar cliente')
  print(Fore.BLUE + Style.BRIGHT + '2. Buscar cliente')
  print(Fore.BLUE + Style.BRIGHT + '3. Listar los clientes')
  print(Fore.BLUE + Style.BRIGHT + '4. Modificar cliente')
  print(Fore.BLUE + Style.BRIGHT + '5. Eliminar cliente')
  print(Fore.BLUE + Style.BRIGHT + '6. Salir')
  print(Fore.BLUE + Style.BRIGHT + '==========================================================================\n')


def handle_option(option):
  """Ejecuta la acción correspondiente según la opción seleccionada."""
  # Opción 1: Registrar cliente
  if option == '1':
    try:
      print(Fore.BLUE + Style.BRIGHT + '\nRegistrando un nuevo cliente...')
      id = input('Ingrese el ID del cliente (ej. 001): ')
      name = str(input('Ingrese el nombre del cliente (ej. María): '))
      email = str(input('Ingrese el email del cliente (ej. maria@example.com): '))
      phone = input('Ingrese el teléfono del cliente (ej. 3001234567): ')

      if new_customer(id, name, email, phone): # Si el registro es exitoso, se muestra un mensaje de éxito
        print(Fore.GREEN + Style.BRIGHT + 'Cliente registrado exitosamente.\n')
      else:
        print(Fore.RED + Style.BRIGHT + 'Error al registrar el cliente.\n')
    except Exception as e:
      print(Fore.RED + Style.BRIGHT + f'Error al registrar el cliente: {e}\n')

# Opción 2: Buscar cliente por ID o Email
  elif option == '2':
    try:
      print(Fore.BLUE + Style.BRIGHT + '\nBuscando cliente por ID o Email...')
      data = input('Ingrese el ID o Email del cliente: ')
      customer = search_customer(data)

      if customer: # Si el cliente es encontrado, se muestra su información
        print(Fore.GREEN + Style.BRIGHT + f'Cliente encontrado: {customer.name} - {customer.email} - {customer.phone}\n')
      else:
        print(Fore.RED + Style.BRIGHT + 'Cliente no encontrado.\n')
    except Exception as e:
      print(Fore.RED + Style.BRIGHT + f'Error al buscar el cliente: {e}\n')

  # Opción 3: Listar los clientes
  elif option == '3':
    try:
      print(Fore.BLUE + Style.BRIGHT + '\nMostrando todos los clientes...')
      customers = list_customers()

      if customers: # Si hay clientes registrados, se muestra la información de cada uno
        for customer in customers:
          print(Fore.GREEN + Style.BRIGHT + f'Cliente: {customer.name} - {customer.email} - {customer.phone}\n')
      else:
        print(Fore.RED + Style.BRIGHT + 'No hay clientes registrados.\n')
    except Exception as e:
      print(Fore.RED + Style.BRIGHT + f'Error al mostrar los clientes: {e}\n')

  # Opción 4: Modificar cliente
  elif option == '4':
    try:
      print(Fore.BLUE + Style.BRIGHT + '\nModificando un cliente...')

      # Identificar primero el cliente a modificar
      data = input('Ingrese el ID o Email del cliente a modificar: ')
      customer = search_customer(data)
      if customer: # Si el cliente es encontrado, se muestra su información
        data = customer.id # Usamos el ID del cliente encontrado para la actualización
        print(Fore.GREEN + Style.BRIGHT + f'Cliente encontrado: {customer.name} - {customer.email} - {customer.phone}\n')
      else:
        print(Fore.RED + Style.BRIGHT + 'Cliente no encontrado.\n')
        return
      
      # Solicitar los nuevos datos del cliente
      name = input('Ingrese el nuevo nombre del cliente (deje vacío para mantener el actual): ')
      email = input('Ingrese el nuevo email del cliente (deje vacío para mantener el actual): ')
      phone = input('Ingrese el nuevo teléfono del cliente (deje vacío para mantener el actual): ')
      if update_customer(data, name, email, phone, current_id=customer.id): # Si la actualización es exitosa, se muestra un mensaje de éxito
        print(Fore.GREEN + Style.BRIGHT + 'Cliente modificado exitosamente.\n')
      else:
        print(Fore.RED + Style.BRIGHT + 'Error al modificar el cliente.\n')
    except Exception as e:
      print(Fore.RED + Style.BRIGHT + f'Error al modificar el cliente: {e}\n')

  # Opción 5: Eliminar cliente
  elif option == '5':
    try:
      print(Fore.BLUE + Style.BRIGHT + '\nEliminando un cliente...')

      # Identificar primero el cliente a eliminar
      data = input('Ingrese el ID o Email del cliente a eliminar: ')
      customer = search_customer(data)
      if customer: # Si el cliente es encontrado, se muestra su información
        data = customer.id # Usamos el ID del cliente encontrado para la eliminación
        print(Fore.GREEN + Style.BRIGHT + f'Cliente encontrado: {customer.name} - {customer.email} - {customer.phone}\n')
      else:
        print(Fore.RED + Style.BRIGHT + 'Cliente no encontrado.\n')
        return

      # Confirmar la eliminación
      confirm = input('¿Está seguro de que desea eliminar este cliente? (s/n): ')
      if confirm.lower() == 's':
        if delete_customer(data): # Si la eliminación es exitosa, se muestra un mensaje de éxito
          print(Fore.GREEN + Style.BRIGHT + 'Cliente eliminado exitosamente.\n')
        else:
          print(Fore.RED + Style.BRIGHT + 'Error al eliminar el cliente.\n')
      else:
        print(Fore.BLUE + Style.BRIGHT + 'Eliminación cancelada.\n')
    except Exception as e:
      print(Fore.RED + Style.BRIGHT + f'Error al eliminar el cliente: {e}\n')

  # Opción 6: Salir del programa
  elif option == '6':
    print(Fore.BLUE + Style.BRIGHT + 'Saliendo del programa...\n')

  else:
    print(Fore.RED + Style.BRIGHT + 'Opción no válida. Por favor, seleccione una opción del menú.\n')