from .model import Model

class Solicitacao(Model):
    def __init__(self,cpf,eventoId,dataHora,justificativa,aprovado):
        self.cpf = cpf
        self.eventoId = eventoId
        self.dataHora = dataHora
        self.justificativa = justificativa
        self.aprovado = aprovado
        