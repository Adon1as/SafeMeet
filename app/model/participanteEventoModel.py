from .model import Model

class ParticipanteEventoModel(Model):
    def __init__(self,cpf,eventoId,hoarario,tratamentoEsp):
        self.cpf = cpf
        self.eventoId = eventoId
        self.horario = hoarario
        self.tratamentoEsp = tratamentoEsp