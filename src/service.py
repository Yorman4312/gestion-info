"""
service.py
Este archivo contiene las funciones CRUD del programa.
"""


# ---------------------------------- IMPORTACIONES ----------------------------------
from validate import validate_customer # Importamos la función de validación desde el archivo validate.py
from file import load_data, save_data # Importamos las funciones para cargar y guardar los datos desde el archivo file.py


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
def register_customer(id, name, email, phone):
    if validate_customer(customers, id, email):
        new_customer = Customer(id, name, email, phone)
        customers.append(new_customer)
        save_data([customer.to_dict() for customer in customers])
        return True
    return False


"""
Función para ver un cliente por ID:
- Se recorre la lista de clientes y se busca un cliente con el ID proporcionado.
- Si se encuentra el cliente, se devuelve el objeto Customer correspondiente.
- Si no se encuentra el cliente, se devuelve None.
"""
def view_customer(id):
    for customer in customers:
        if customer.id == id:
            return customer
    return None


"""
Función para ver todos los clientes:
- Se devuelve la lista completa de clientes almacenada en la variable global customers.
"""
def view_all_customers():
    return customers