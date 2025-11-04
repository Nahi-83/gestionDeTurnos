from consultorio import Consultorio

class Hospital:
    def __init__(self, nombre, direccion, cantConsultorios):
        self._nombre = nombre 
        self._direccion = direccion
        self._cantConsultorios = cantConsultorios

    def mostrarDatos(self):
        return f"{self._nombre} Dirección:{self._direccion} Cuenta con {self._cantConsultorios} consultorios"