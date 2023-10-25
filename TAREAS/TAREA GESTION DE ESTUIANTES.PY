class Estudiante:
    estudiantes = []

    def __init__(self, nombre, edad, carrera):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera

    @classmethod
    def mostrar_estudiantes(cls):
        mensaje = f"Tienes {len(cls.estudiantes)} estudiantes\nLos estudiantes son:\n"
        for estudiante in cls.estudiantes:
            mensaje += f"{estudiante}\n"
        return mensaje

    def registrar_estudiante(self):
        nuevo_id = len(self.estudiantes) + 1
        estudiante_nuevo = {
            "id": nuevo_id,
            "nombre": self.nombre,
            "edad": self.edad,
            "carrera": self.carrera
        }
        self.estudiantes.append(estudiante_nuevo)
        return f"El siguiente estudiante se registró exitosamente: {estudiante_nuevo}"

    @classmethod
    def mostrar_estudiante(cls, id):
        estudiante_buscar = cls.estudiantes[id - 1]
        return estudiante_buscar

    @classmethod
    def eliminar_estudiante(cls, id):
        estudiante_eliminar = cls.estudiantes.pop(id - 1)
        return f"El siguiente estudiante fue eliminado: {estudiante_eliminar}"

    @classmethod
    def actualizar_estudiante(cls, id, nuevo_nombre=None, nueva_edad=None, nueva_carrera=None):
        estudiante_actualizar = cls.estudiantes[id - 1]

        if nuevo_nombre:
            estudiante_actualizar["nombre"] = nuevo_nombre
        if nueva_edad:
            estudiante_actualizar["edad"] = nueva_edad
        if nueva_carrera:
            estudiante_actualizar["carrera"] = nueva_carrera

        return f"El siguiente estudiante fue actualizado: {estudiante_actualizar}"


estudiante1 = Estudiante("Juan Perez",  20, "Ingeniería de Sistemas")
estudiante2 = Estudiante("roger", 23, "informatico")
print(estudiante1.registrar_estudiante())
print(estudiante2.registrar_estudiante())
print(Estudiante.mostrar_estudiantes())
print(Estudiante.mostrar_estudiante(1))
print(Estudiante.eliminar_estudiante(0))
print(Estudiante.mostrar_estudiantes())