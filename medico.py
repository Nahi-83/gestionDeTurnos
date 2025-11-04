from persona import Persona 

class Medico(Persona):
    def __init__(self, nombre, apellido, dni, fechaNac, email, password, horarioDeAtencion, profesion, matricula):
        super().__init__(nombre, apellido, dni, fechaNac, email, password)
        self._horarioDeAtencion = horarioDeAtencion
        self._profesion = profesion
        self._matricula = matricula
    
    def get_profesion(self):
        return self._profesion

    def get_matricula(self):
        return self._matricula
    
    def mostrarDatos(self):
        datosPrincipales = super().mostrarDatos()
        return f"{datosPrincipales} Profesión: {self._profesion} Matrícula: {self._matricula}"