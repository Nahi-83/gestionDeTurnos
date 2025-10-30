class Persona:
    def __init__(self, nombre, apellido, dni, fechaNac, email, password):
        self._nombre = nombre
        self._apellido = apellido
        self._dni = dni
        self._fechaNac = fechaNac
        self._password = password
        self._email= email

    def mostrarDatos(self):
        return f"{self._nombre} {self._apellido} {self._dni} {self._fechaNac} {self._email} {self._password}"