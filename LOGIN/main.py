from bd import usuarios  # Importa la lista de usuarios desde un módulo llamado 'bd'

class usuarios:
    def __init__(self, dni, nombre, edad, f_nacimiento, usuario, password):
        self.dni = dni
        self.nombre = nombre
        self.edad = edad
        self.f_nacimiento = f_nacimiento
        self.usuario = usuario
        self.password = password

    def actualizar_edad(self, nueva_edad):
        self.edad = nueva_edad

    def verificar_registro(self, usuario, password):
        for usuario_registrado in usuarios:
            if usuario_registrado["usuario"] == usuario and usuario_registrado["password"] == password:
                return True
        return False

# Buscar datos del usuario 'moises' en la lista de usuarios
moises_data = None
for usuario_data in usuarios:
    if usuario_data["usuario"] == "moises":
        moises_data = usuario_data
        break

# Crear una instancia de Usuario si se encontraron datos
moises = None
if moises_data:
    moises = usuarios(moises_data["dni"], moises_data["nombre"], moises_data["edad"], moises_data["f_nacimiento"], moises_data["usuario"], moises_data["password"])

# Actualizar la edad de Moises si se encontró
if moises:
    moises.actualizar_edad(33)

# Verificar si Moises está registrado
if moises.verificar_registro("moises", "12345"):
    print("Moises está registrado.")
else:
    print("Moises no está registrado.")
