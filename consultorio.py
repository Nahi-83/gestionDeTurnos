class Consultorio:
    def __init__(self, nroDeConsultorio):
        self._nroDeConsultorio = nroDeConsultorio

    def mostrarDatos(self):
        return f"Número de consultorio: {self._nroDeConsultorio}"