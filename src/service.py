"""
service.py
Contiene la lógica de negocio para el CRUD de clientes.
Incluye el modelo Customer y las operaciones de persistencia en memoria y JSON.
"""


# ---------------------------------- IMPORTACIONES ----------------------------------
from colorama import Fore, Style, Back, init # Para imprimir mensajes en colores
init(autoreset=True) # Inicializa colorama para restablecer estilos automáticamente

from validate import validate_customer
from file import load_data, save_data


# ---------------------------------- MODELO DE DATOS ----------------------------------
class Customer:
  """Representa un cliente con sus campos básicos."""

  def __init__(self, id, name, email, phone):
    self.id = id
    self.name = name
    self.email = email
    self.phone = phone

  def to_dict(self):
    """Convierte el objeto Customer a un diccionario listo para serializar."""
    return {
      'id': self.id,
      'name': self.name,
      'email': self.email,
      'phone': self.phone,
    }

  @staticmethod
  def from_dict(data):
    """Crea un objeto Customer a partir de un diccionario."""
    return Customer(
      data.get('id', ''),
      data.get('name', ''),
      data.get('email', ''),
      data.get('phone', ''),
    )


# ---------------------------------- CARGA INICIAL ----------------------------------
"""
Listado de clientes:
- Se traen los clientes desde el archivo JSON utilizando la función load_data() del archivo file.py.
- Cada registro JSON se convierte a un objeto Customer.
"""
raw_customers = load_data()
customers = [Customer.from_dict(item) for item in raw_customers if isinstance(item, dict)]


# ---------------------------------- FUNCIONES CRUD ----------------------------------
"""
Función para registrar un nuevo cliente:
- Se valida el cliente utilizando la función validate_customer() del archivo validate.py.
- Si la validación es exitosa, se crea un nuevo objeto Customer y se agrega a la lista de clientes.
- Se guarda la lista de clientes actualizada en el archivo JSON utilizando la función save_data().
"""
def new_customer(id, name, email, phone):
  if validate_customer(customers, id, name, email, phone):
    customer = Customer(id, name, email, phone)
    customers.append(customer)
    save_data([c.to_dict() for c in customers]) # Guardamos la lista de clientes actualizada en el archivo JSON
    return True
  return False


"""
Función para ver un cliente por ID o Email:
- Se recorre la lista de clientes y se busca un cliente con el ID o Email proporcionado.
- Si se encuentra el cliente, se devuelve el objeto Customer correspondiente.
- Si no se encuentra el cliente, se devuelve None.
- Se usan funciones lambda y filter para buscar el cliente de manera más eficiente.
- Uso de next() para obtener el primer resultado de la búsqueda o None si no se encuentra ningún cliente con el ID o Email proporcionado.
"""
def search_customer(data):
  return next((c for c in customers if c.id == data or c.email == data), None)


"""
Función para ver todos los clientes:
- Se devuelve la lista completa de clientes almacenada en la variable global customers.
"""
def list_customers():
  return customers


"""
Función para actualizar/modificar un cliente:
- Se recorre la lista de clientes y se busca un cliente con el ID proporcionado.
- Se imprimen los datos actuales del cliente seleccionado.
- Se solicitan los nuevos datos al usuario (si el usuario deja un campo vacío, se mantiene el valor actual).
- Se valida el cliente utilizando la función validate_customer() del archivo validate.py.
"""
def update_customer(id, name, email, phone, current_id=None):
  customer = next((c for c in customers if c.id == id), None)
  if customer:
    print(f'{Fore.BLUE + Style.BRIGHT}Cliente encontrado: {customer.name} - {customer.email} - {customer.phone}')
    new_name = name if name.strip() else customer.name
    new_email = email if email.strip() else customer.email
    new_phone = phone if phone.strip() else customer.phone

    if validate_customer(customers, id, new_name, new_email, new_phone, current_id=current_id):
      customer.id = id
      customer.name = new_name
      customer.email = new_email
      customer.phone = new_phone
      save_data([c.to_dict() for c in customers]) # Guardamos la lista de clientes actualizada en el archivo JSON
      return True
  return False


"""
Función para eliminar un cliente:
- Se recorre la lista de clientes y se busca un cliente con el ID proporcionado.
"""
def delete_customer(id):
  customer = next((c for c in customers if c.id == id), None)
  if customer:
    customers.remove(customer)
    save_data([c.to_dict() for c in customers]) # Guardamos la lista de clientes actualizada en el archivo JSON
    return True
  return False