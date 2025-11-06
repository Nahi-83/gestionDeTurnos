from medico import Medico
from paciente import Paciente
from turno import Turno

print("GESTOR DE TURNOS DEL HOSPITAL")

medicos = [
    Medico("Lucía", "Gómez", "33222111", "1980-05-12", "lucia@gmail.com", "1234", "8-16", "Pediatría", "M123"),
    Medico("Marcos", "López", "31222444", "1975-03-20", "marcos@gmail.com", "1234", "9-17", "Clínico", "M456")
]

pacientes = []  
turnos = []     

while True:
    print("\nMENÚ")
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
        print(f"Paciente {nombre} registrado correctamente.")

    elif opcion == "2":
        email = input("Email: ")
        password = input("Contraseña: ")

        pacienteEncontrado = None
        for inicioPaciente in pacientes:
            if inicioPaciente.login(email, password):
                pacienteEncontrado = inicioPaciente
                break

        if pacienteEncontrado:
            print(f"\n¡Bienvenido/a {pacienteEncontrado.get_nombre()}!")
            print("1. Sacar turno")
            print("2. Ver mis turnos")
            print("3. Cerrar sesión")

            gestionTurnos = input("Elegí una opción: ")

            if gestionTurnos == "1":
                print("\nMédicos disponibles")
                for i, medicosDis in enumerate(medicos):
                    print(f"{i+1}. {medicosDis.get_profesion()} - {medicosDis.get_nombre()}")

                seleccion = int(input("Seleccione el médico de su preferencia: ")) - 1

                if 0 <= seleccion < len(medicos):
                    fecha = input("Fecha del turno (dd/mm/aaaa): ")
                    hora = input("Hora del turno: ")
                    turnoSacado = Turno(medicos[seleccion], pacienteEncontrado, hora, fecha)
                    turnos.append(turnoSacado)
                    turnoSacado.confirmarTurno()
                else:
                    print("Opción incorrecta.")

            elif gestionTurnos == "2":
                print("\nTus turnos")
                turnos_paciente = [turnoSacado for turnoSacado in turnos if turnoSacado._paciente == pacienteEncontrado]
                if turnos_paciente:
                    for turnoSacado in turnos_paciente:
                        print(f"- {turnoSacado._fecha} a las {turnoSacado._hora} con {turnoSacado._medico.get_nombre()}")
                else:
                    print("No tenés turnos registrados.")
            
            elif gestionTurnos == "3":
                print("Sesión cerrada.")
            
            else:
                print("Opción incorrecta.")

        else:
            print("Email o contraseña incorrectos.")

    elif opcion == "3":
        print("¡Gracias por usar el sistema de turnos!")
        break

    else:
        print("Opción incorrecta. Intentá otra vez.")
