from persona import Persona 

class Medico(Persona):
    def __init__(self, nombre, apellido, dni, fechaNac, email, password, horarioDeAtencion,):
        super().__init__(nombre, apellido, dni, fechaNac, email, password)
        self._horarioDeAtencion