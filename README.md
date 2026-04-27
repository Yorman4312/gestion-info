# Sistema de Gestión de Clientes

Un sistema simple de gestión de información de clientes desarrollado en Python. Permite registrar, consultar y gestionar clientes de manera básica, con persistencia de datos en un archivo JSON.

## Instalación

### Clonar el repositorio

En la carpeta donde deseas clonar el repositorio, ejecuta los siguientes comandos en la consola:

```bash
git clone https://github.com/Yorman4312/gestion-info
cd gestion-info
```

### Requisitos

- Python 3.6 o superior
- Instalar dependencias:

```bash
pip install -r requirements.txt
```

Las dependencias principales incluyen:
- `colorama`: Para imprimir mensajes en colores en la consola.

## Uso

1. Ubica el archivo `main.py` en la carpeta `src/` (`gestion-info/src/main.py`).
2. Ejecuta el programa:

```bash
python src/main.py
```

### Funcionalidades

- **Registrar cliente**: Agrega un nuevo cliente con ID, nombre, email y teléfono.
- **Buscar cliente por ID o Email**: Permite encontrar un cliente usando su ID o correo electrónico.
- **Listar clientes**: Muestra todos los clientes registrados.
- **Modificar cliente**: Actualiza el nombre, email o teléfono de un cliente existente.
- **Eliminar cliente**: Borra un cliente del registro.
- **Salir**: Cierra el programa usando la opción 6.

> Nota: La aplicación ahora usa la opción 6 para salir y la actualización de clientes valida correctamente los datos.

## Flujo del Programa

El programa sigue un flujo modular para mantener la separación de responsabilidades. A continuación, se describe el orden de ejecución de los archivos y sus responsabilidades:

1. **`main.py`** (Archivo principal):
   - Punto de entrada del programa.
   - Muestra el mensaje de bienvenida.
   - Importa y ejecuta el menú interactivo desde `menu.py`.
   - Maneja el bucle principal del programa y las excepciones generales.

2. **`menu.py`** (Interfaz de usuario):
   - Gestiona la presentación del menú principal.
   - Solicita la entrada del usuario para seleccionar opciones.
   - Llama a las funciones correspondientes de `service.py` según la opción elegida.
   - Maneja errores específicos de cada opción.

3. **`service.py`** (Lógica de negocio):
   - Contiene las operaciones CRUD (Crear, Leer, Actualizar, Eliminar) para los clientes.
   - Define la clase `Customer` para representar a cada cliente.
   - Gestiona la lista global de clientes en memoria.
   - Convierte entre objetos `Customer` y diccionarios para la persistencia.

4. **`file.py`** (Persistencia de datos):
   - Responsable de cargar y guardar los datos de clientes en un archivo JSON (`data/records.json`).
   - Asegura que el archivo y directorio existan.
   - Maneja errores de lectura/escritura y JSON corrupto.

5. **`validate.py`** (Validación de datos):
   - Valida que los IDs y emails de los clientes sean únicos.
   - Previene duplicados antes de registrar un nuevo cliente.

6. **`integration.py`** (Integraciones futuras):
   - Archivo reservado para posibles integraciones adicionales (actualmente vacío).

### Diagrama de flujo simplificado

```
Usuario ejecuta main.py
    ↓
main.py importa menu.py
    ↓
menu.py muestra menú y llama a service.py
    ↓
service.py usa file.py para cargar/guardar datos
    ↓
validate.py valida entradas
    ↓
Datos persisten en data/records.json
```

## Estructura del Proyecto

```
gestion-info/
├── README.md              # Documentación del proyecto
├── requirements.txt       # Dependencias de Python
├── data/
│   └── records.json       # Archivo de datos JSON
├── src/
│   ├── main.py            # Punto de entrada
│   ├── menu.py            # Interfaz de menú
│   ├── service.py         # Lógica CRUD
│   ├── file.py            # Persistencia de datos
│   ├── validate.py        # Validaciones
│   └── integration.py     # Integraciones (placeholder)
└── test/
    └── tests.py           # Pruebas (placeholder)
```

## Contribución

Si deseas contribuir al proyecto:
1. Haz un fork del repositorio.
2. Crea una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza tus cambios y haz commit (`git commit -am 'Agrega nueva funcionalidad'`).
4. Haz push a la rama (`git push origin feature/nueva-funcionalidad`).
5. Abre un Pull Request.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.