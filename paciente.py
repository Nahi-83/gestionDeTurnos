from persona import Persona

class Paciente(Persona):
    def __init__(self, nombre, apellido, dni, fechaNac, email, password, nroDeHistoriaClinica):
        super().__init__(nombre, apellido, dni, fechaNac, email, password)
        self._nroDeHistoriaClinica = nroDeHistoriaClinica

    def mostrarDatos(self):
        return super().mostrarDatos()
    
    def login(self):
        return
    
    def registrarse(self):
        return