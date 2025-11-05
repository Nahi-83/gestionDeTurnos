from hospital import Hospital
from medico import Medico
from paciente import Paciente
from turno import Turno

def main():
    hospital = Hospital("Hospital Zonal Esquel", "Av. Fontana 555", 5)

    medicos = [
        Medico("Lucía", "Gómez", "33222111", "1980-05-12", "lucia@gmail.com", "1234", "8-16", "Pediatría", "M123"),
        Medico("Marcos", "López", "31222444", "1975-03-20", "marcos@gmail.com", "4567", "9-17", "Clínico", "M456")
    ]

    pacientes = []
    turnos = []

    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Registrar paciente")
        print("2. Iniciar sesión")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            dni = input("DNI: ")
            fecha = input("Fecha de nacimiento: ")
            email = input("Email: ")
            password = input("Contraseña: ")
            historiaClinica = input("Número de historia clínica: ")

            nuevoPaciente = Paciente(nombre, apellido, dni, fecha, email, password, historiaClinica)
            pacientes.append(nuevoPaciente)
            nuevoPaciente.registrarse()

        elif opcion == "2":
            email = input("Email: ")
            password = input("Contraseña: ")

            pacienteEncontrado = None
            for paciente in pacientes:
                if paciente.login(email, password):
                    pacienteEncontrado = paciente
                    break

            if pacienteEncontrado:
                print(f"\nBienvenido {pacienteEncontrado.get_nombre()}!")
                print("1. Agendar turno")
                print("2. Ver mis turnos")

                gestionTurnos = input("Seleccione una opción: ")

                if gestionTurnos == "1":
                    print("\n--- MÉDICOS DISPONIBLES ---")
                    for i, listaMedicos in enumerate(medicos):
                        print(f"{i+1}. {listaMedicos.get_profesion()} - {listaMedicos.get_nombre()}")

                    try:
                        seleccion = int(input("Seleccione médico: ")) - 1
                        if seleccion < 0 or seleccion >= len(medicos):
                            print("Opción inválida.")
                            continue
                    except ValueError:
                        print("Debe ingresar un número.")
                        continue

                    fecha = input("Fecha del turno (dd/mm/aaaa): ")
                    hora = input("Hora del turno: ")
                    turnoDado = Turno(medicos[seleccion], pacienteEncontrado, hora, fecha)
                    turnos.append(turnoDado)
                    turnoDado.confirmarTurno()

                elif gestionTurnos == "2":
                    print("\n--- TUS TURNOS ---")
                    turnos_encontrados = False
                    for turnoDado in turnos:
                        if turnoDado._paciente == pacienteEncontrado:
                            print(f"- {turnoDado._fecha} a las {turnoDado._hora} con {turnoDado._medico.get_nombre()}")
                            turnos_encontrados = True
                    if not turnos_encontrados:
                        print("No tenés turnos registrados.")

            else:
                print("Email o contraseña incorrectos.")

        elif opcion == "3":
            print("¡Que tengas un buen día!")
            break

        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()
