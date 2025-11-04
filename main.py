def menu():
    pacientes = []
    medico = []
    turno = []

    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Registro de usuario")
        print("2. Iniciar sesión")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            dni = input("DNI: ")
            fecha_nac = input("Fecha de nacimiento: ")
            email = input("Email: ")
            password = input("Contraseña: ")
            hc = input("N° Historia Clínica: ")
            paciente = paciente(nombre, apellido, dni, fecha_nac, email, password, hc)
            pacientes.append(paciente)
            print("Registro exitoso!")

        elif opcion == "2":
            email = input("Email: ")
            password = input("Contraseña: ")
            paciente_encontrado = None
            for p in pacientes:
                if p.login(email, password):
                    paciente_encontrado = p
                    break
            if paciente_encontrado:
                print(f"Bienvenido {paciente_encontrado._nombre}")
            else:
                print("Credenciales incorrectas.")
        elif opcion == "3":
            break
