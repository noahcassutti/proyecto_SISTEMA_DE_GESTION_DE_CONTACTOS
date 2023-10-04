# creacion de la clase constructora

class Contacto:
    def __init__(self, nombre, apellido, num_cel, direccion_email, fecha_nacimiento, ):
        self.nombre = nombre
        self.apellido = apellido
        self.num_cel = num_cel
        self.direccion_email = direccion_email
        self.fecha_nacimiento = fecha_nacimiento
        


class Vehiculo:
    def __init__(self, tipo, marca, cant_puertas, modelo, encendido):
        self.tipo = tipo
        self.marca = marca
        self.cant_puertas = cant_puertas
        self.modelo = modelo
        self.encendido = encendido

    def abrir_puertas(self):
        print("Se abrio una puerta")
    def encender_vehiculo(self):
        if self.encendido == True:
            print("Se encendio el vehiculo")
        return

Honda = Vehiculo("auto", "honda", 5, "civic", True)

print("Tipo:", Honda.tipo)
print("Marca:", Honda.marca)
print("Cantidad de Puertas:", Honda.cant_puertas)
print("Modelo:", Honda.modelo)

Honda.encender_vehiculo()  # Llama al método para encender el vehículo
print("Encendido:", Honda.encendido)  # Imprime el estado del atributo encendido



        
    


