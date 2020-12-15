from .model import Model


class SolicitacaoModel(Model):
    def __init__(self, cpf, eventoId, dataHora, justificativa, aprovado):
        self.cpf = cpf
        self.eventoId = eventoId
        self.dataHora = dataHora
        self.justificativa = justificativa
        self.aprovado = aprovado

    def toDict(self):
        return {'cpf': self.cpf, 'eventoId': self.eventoId, 'dataHora': self.dataHora, 'justificativa': self.justificativa, 'aprovado': self.aprovado}
