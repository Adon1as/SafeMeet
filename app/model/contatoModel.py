from .model import Model


class ContatoModel(Model):
    def __init__(self, tipo, contato, descricao):
        self.tipo = tipo
        self.contato = contato
        self.descricao = descricao

    def toDict(self):
        return {'tipo': self.tipo, 'contato': self.contato, 'descricao': self.descricao}
