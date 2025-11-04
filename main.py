from hospital import Hospital
from medico import Medico
from paciente import Paciente
from turno import Turno

def main():
    hospital = Hospital("Hospital Zonal Esquel", "Av. Fontana 555")

    medicos = [
        Medico("Lucía", "Gómez", "33222111", "1980-05-12", "lucia@gmail.com", "1234", "8-16", "Pediatría", "M123")]
    pacientes = []
    turnos = []

    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Registrar paciente")
        print("2. Iniciar sesión")
        print("3. Salir")

        opcion = input("Opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            dni = input("DNI: ")
            fecha = input("Fecha de nacimiento: ")
            email = input("Email: ")
            password = input("Contraseña: ")
            historiaClinica = input("Historia clínica: ")
            nuevo = Paciente(nombre, apellido, dni, fecha, email, password, historiaClinica)
            pacientes.append(nuevo)
            print(f"Paciente {nombre} registrado.")

        