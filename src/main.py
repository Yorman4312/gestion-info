"""
main.py
Este es el archivo principal.
Aquí se importan las funciones necesarias para el funcionamiento del programa.
Se utiliza try-except para manejar errores.
"""


# ---------------------------------- IMPORTACIONES ----------------------------------
from colorama import Fore, Style, Back, init # Para imprimir mensajes en colores
init(autoreset=True) # Para que los colores se restablezcan automáticamente después de cada impresión

from menu import show_menu, handle_option # Importamos las funciones del archivo menu.py


# ---------------------------------- CÓDIGO PRINCIPAL ----------------------------------
def run():
    # Mensaje de bienvenida
    print(Fore.BLUE + Style.BRIGHT + '===========================================================================================================')
    print(Fore.BLUE + Style.BRIGHT + '=============================== Bienvenido al Sistema de Gestión de Clientes ==============================')
    print(Fore.BLUE + Style.BRIGHT + '===========================================================================================================\n')

    # Bucle principal del programa
    while True:
        try:
            show_menu() # Mostramos el menú principal
            option = input('Seleccione una opción: ') # Solicitamos al usuario que seleccione una opción
            handle_option(option) # Manejar la opción seleccionada por el usuario

            if option == '4': # Si el usuario selecciona la opción de salir, se muestra un mensaje de despedida y se rompe el bucle
                print(Fore.BLUE + Style.BRIGHT + '============================================================================================')
                print(Fore.BLUE + Style.BRIGHT + '======================== Gracias por usar el sistema. ¡Hasta luego! ========================')
                print(Fore.BLUE + Style.BRIGHT + '============================================================================================\n')
                break
        except Exception as e:
            print(Fore.RED + Style.BRIGHT + f'Error inesperado: {e}')


if __name__ == '__main__': # Si este archivo se ejecuta directamente, se llama a la función run()
    run()