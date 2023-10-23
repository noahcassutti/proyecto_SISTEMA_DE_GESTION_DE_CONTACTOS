from clases.Registros import *
from utilidades.Funciones import agregar_contacto_input

# función principal
def main():
    nuevo_contacto = agregar_contacto_input()
    agregar_contacto(nuevo_contacto, lista_de_contactos)  # Agregar el contacto a la lista
    cadena = nuevo_contacto.to_string()
    print(cadena)  # Imprimir la representación personalizada del contacto

# inicialización
if __name__ == "__main__":
    main()
