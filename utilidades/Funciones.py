from clases.Registros import Contacto

# metodos

# metodo agregar
def agregar_contacto(contacto, lista_de_contactos):
    lista_de_contactos.append(contacto)


# lista para almacenar contactos

lista_de_contactos = []

# metodo de agregar desde input

def agregar_contacto_input():
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    celular = int(input("Celular: "))
    correo = input("Correo: ")
    fecha_nacimiento = input("Fecha de nacimiento: ")

    nuevo_contacto = Contacto(nombre, apellido, celular, correo, fecha_nacimiento)

    return nuevo_contacto
#metodo mostrar

def to_string(self):
    return f"Nombre: {self.nombre}, Apellido: {self.apellido}, Numero de celular: {self.num_cel}, Direccion email: {self.direccion_email}, Fecha de nacimiento: {self.fecha_nacimiento}"