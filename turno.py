class Turno: 
    def __init__(self, medico, paciente, hora, fecha):
        self._medico = medico
        self._paciente = paciente
        self._hora = hora
        self._fecha = fecha

    def confirmarTurno(self):
        print(f"Turno confirmado con {self._medico._nombre} para {self._paciente._nombre}")

    def cancelarTurno(self):
        print(f"Turno de {self._paciente._nombre} cancelado")

    def darTurno(self):
        print(f"Turno dado para {self._paciente._nombre} con el médico {self._medico._nombre}")