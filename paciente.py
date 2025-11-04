from persona import Persona

class Paciente(Persona):
    def __init__(self, nombre, apellido, dni, fechaNac, email, password, nroDeHistoriaClinica):
        super().__init__(nombre, apellido, dni, fechaNac, email, password)
        self._nroDeHistoriaClinica = nroDeHistoriaClinica
    
    def login(self, email, password):
        if self._email == email and self._password == password:
            return True
        else:
            return False
        
    def registrarse(self):
        print(f"Paciente {self._nombre} registrado correctamente.")

    def mostrarDatos(self):
        return f"Paciente: {self._nombre} {self._apellido} Número de historia clinica: {self._nroDeHistoriaClinica}"