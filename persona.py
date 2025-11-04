class Persona:
    def __init__(self, nombre, apellido, dni, fechaNac, email, password):
        self._nombre = nombre
        self._apellido = apellido
        self._dni = dni
        self._fechaNac = fechaNac
        self._password = password
        self._email= email

    def get_nombre(self):
        return self._nombre
    
    def get_apellido(self):
        return self._apellido
    
    def get_dni(self):
        return self._dni

    def get_email(self):
        return self._email
    
    def set_email(self, nuevo_email):
        if "@" in nuevo_email:
            self._email = nuevo_email
        else:
            print("Email inválido.")

    def set_password(self, nuevo_password):
        if len(nuevo_password) >= 4:
            self._password = nuevo_password
        else:
            print("La contraseña debe tener al menos 4 caracteres.")

    def mostrarDatos(self):
        return f"{self._nombre} {self._apellido} {self._dni} {self._fechaNac} {self._email} {self._password}"