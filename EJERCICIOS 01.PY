# haciendo uso de la POO crear un objeto para la entidad celular T
class Celular:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color

    def llamar(self, numero):
        print(f"Llamando al número {numero} desde un celular {self.marca} {self.modelo} de color {self.color}.")

# Crear una instancia de Celular
celular_t = Celular("T", "Modelo T", "Negro")

# Utilizar el objeto celular_t
celular_t.llamar("123456789")

#haciendo uso de la POO crear un objeto para la entidad vehiculo
class Avion:
    def __init__(self, marca, modelo, capacidad):
        self.marca = marca
        self.modelo = modelo
        self.capacidad = capacidad

    def despegar(self):
        print(f"El avión {self.marca} {self.modelo} con capacidad de {self.capacidad} despegó.")

# Crear una instancia de Avion
avion = Avion("Boeing", "747", 300)

# Utilizar el objeto avion
avion.despegar()

#haciendo uso de la POO crear un objeto para la entidad avion

class Avion:
    def __init__(self, marca, modelo, capacidad):
        self.marca = marca
        self.modelo = modelo
        self.capacidad = capacidad

    def despegar(self):
        print(f"El avión {self.marca} {self.modelo} con capacidad de {self.capacidad} despegó.")

# Crear una instancia de Avion
avion = Avion("Boeing", "747", 300)

# Utilizar el objeto avion
avion.despegar()

#haciendo uso de la POO crear un objeto para un heroe de dota
class HeroeDota:
    def __init__(self, nombre, tipo, habilidad_principal):
        self.nombre = nombre
        self.tipo = tipo
        self.habilidad_principal = habilidad_principal

    def usar_habilidad(self):
        print(f"El héroe {self.nombre} está usando su habilidad principal: {self.habilidad_principal}.")

# Crear una instancia de HeroeDota
heroe = HeroeDota("Invoker", "Inteligencia", "Sun Strike")

# Utilizar el objeto heroe
heroe.usar_habilidad()
#Aquí tienes un ejemplo de cómo crear una clase en Python para representar un objeto de una PC:

class PC:
    def __init__(self, marca, modelo, ram, almacenamiento):
        self.marca = marca
        self.modelo = modelo
        self.ram = ram
        self.almacenamiento = almacenamiento
        
    def encender(self):
        print("La PC se ha encendido.")
        
    def apagar(self):
        print("La PC se ha apagado.")
        
    def mostrar_especificaciones(self):
        print(f"Especificaciones de la PC:\nMarca: {self.marca}\nModelo: {self.modelo}\nRAM: {self.ram}GB\nAlmacenamiento: {self.almacenamiento}")
 
# Aquí tienes un ejemplo de cómo crear una clase en Python para representar un objeto de impresora:

python
class Impresora:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        
    def imprimir(self, documento):
        print(f"Imprimiendo {documento}...")
        
    def escanear(self):
        print("Escaneando documento...")
        
    def copiar(self, cantidad):
        print(f"Copiando {cantidad} copias...")


# Aquí tienes un ejemplo de cómo crear un objeto para emitir una factura utilizando programación orientada a objetos en Python:

python
class Factura:
    def __init__(self, numero, cliente, total):
        self.numero = numero
        self.cliente = cliente
        self.total = total

    def imprimir_factura(self):
        print("Factura número:", self.numero)
        print("Cliente:", self.cliente)
        print("Total:", self.total)

# Crear una instancia de la clase Factura
factura1 = Factura(001, "Cliente A", 100.50)

# Llamar al método imprimir_factura para mostrar los detalles de la factura
factura1.imprimir_factura()

