class Asistencia:
    def __init__(self):
        self.alumnos = {}
    
    def agregar_alumno(self, nombre):
        if nombre not in self.alumnos:
            self.alumnos[nombre] = []

    def eliminar_alumno(self, nombre):
        if nombre in self.alumnos:
            del self.alumnos[nombre]

    def tomar_asistencia(self, nombre, fecha):
        if nombre in self.alumnos:
            if fecha not in self.alumnos[nombre]:
                self.alumnos[nombre].append(fecha)
                print(f"Asistencia registrada para {nombre} el {fecha}.")
            else:
                print(f"{nombre} ya ha sido registrado para el {fecha}.")
        else:
            print(f"{nombre} no está en la lista de alumnos.")

    def imprimir_asistencia(self, fecha):
        print(f"Asistencia del {fecha}:")
        for nombre, fechas_asistencia in self.alumnos.items():
            if fecha in fechas_asistencia:
                print(f"{nombre} presente.")
            else:
                print(f"{nombre} ausente.")

def main():
    asistencia = Asistencia()
    
    while True:
        print("\nOpciones:")
        print("1. Agregar alumno")
        print("2. Eliminar alumno")
        print("3. Tomar asistencia")
        print("4. Imprimir asistencia")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            nombre = input("Ingrese el nombre del alumno: ")
            asistencia.agregar_alumno(nombre)
        elif opcion == "2":
            nombre = input("Ingrese el nombre del alumno a eliminar: ")
            asistencia.eliminar_alumno(nombre)
        elif opcion == "3":
            nombre = input("Ingrese el nombre del alumno: ")
            fecha = input("Ingrese la fecha (dd/mm/aaaa): ")
            asistencia.tomar_asistencia(nombre, fecha)
        elif opcion == "4":
            fecha = input("Ingrese la fecha (dd/mm/aaaa) para imprimir la asistencia: ")
            asistencia.imprimir_asistencia(fecha)
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
