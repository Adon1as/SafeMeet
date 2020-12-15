from .model import Model


class ParticipanteEventoModel(Model):
    def __init__(self, cpf, eventoId, hoarario, tratamentoEsp):
        self.cpf = cpf
        self.eventoId = eventoId
        self.horario = hoarario
        self.tratamentoEsp = tratamentoEsp

    def toDict(self):
        return {'cpf': self.cpf, 'eventoId': self.eventoId, 'horario': self.horario, 'tratamentoEsp': self.tratamentoEsp}
