from .model import Model


class EventoModel(Model):
    particpantes = []

    def __init__(self, id, comeco, fim, tempoMax, quantidade, descricao, local):
        self.id = id
        self.comeco = comeco
        self.fim = fim
        self.tempoMax = tempoMax
        self.quantidade = quantidade
        self.descricao = descricao
        self.local = local

    def toDict(self):
        return {'id': self.id, 'comeco': self.comeco, 'fim': self.fim, 'tempoMax': self.tempoMax, 'quantidade': self.quantidade, 'descricao': self.descricao, 'local': self.local, }
