"""
tests.py
Pruebas básicas para el CRUD de clientes.
"""

# ---------------------------------- IMPORTACIONES ----------------------------------
import sys
import os

# Añade la carpeta raíz al buscador de Python
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.service import Customer, new_customer, search_customer, delete_customer, customers as service_customers
from src.validate import validate_customer
from src.file import load_data

"""
Listado de clientes:
- Se traen los clientes desde el archivo JSON utilizando la función load_data() del archivo file.py.
"""
raw_customers = load_data()
local_customers = [Customer.from_dict(item) for item in raw_customers if isinstance(item, dict)]


# Datos de prueba
customer_valido = {
    "id": "9999",
    "name": "ClienteTest",
    "email": "test@test.com",
    "phone": "1234567890"
}

customer_invalido = {
    "id": "", # Cambiado de None a "" para evitar error con .strip() en validate.py
    "name": "",
    "email": "correo-malo",
    "phone": "abcde"
}


# ---------------------------------- PRUEBAS ----------------------------------

# TEST 1: Crear cliente
def test_new_customer():
    # Asegurar estado limpio
    delete_customer(customer_valido["id"])

    resultado = new_customer(**customer_valido)
    assert resultado is True

    # search_customer devuelve un objeto Customer, no una lista
    cliente = search_customer(customer_valido["id"])
    assert cliente is not None
    assert cliente.id == customer_valido["id"]


# TEST 2: Buscar cliente
def test_search_customer():
    delete_customer(customer_valido["id"])
    new_customer(**customer_valido)

    cliente = search_customer(customer_valido["id"])

    # Verificamos que sea un objeto individual y tenga el nombre correcto
    assert cliente is not None
    assert not isinstance(cliente, list) 
    assert cliente.name == "ClienteTest"


# TEST 3: Eliminar cliente
def test_delete_customer():
    # Asegurar que existe antes de borrar
    if not search_customer(customer_valido["id"]):
        new_customer(**customer_valido)

    resultado = delete_customer(customer_valido["id"])
    assert resultado is True

    # Al no existir, search_customer devuelve None (según tu lógica con next)
    cliente = search_customer(customer_valido["id"])
    assert cliente is None


# TEST 4: Validación
def test_validate_customer():
    # Usamos la lista de clientes cargada al inicio
    assert validate_customer(local_customers, **customer_valido) is True
    assert validate_customer(local_customers, **customer_invalido) is False
