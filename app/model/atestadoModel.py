from .model import Model


class AtestadoModel(Model):
    def __init__(self, id, arquivo, cid10):
        self.id = id
        self.arquivo = arquivo
        self.cid10 = cid10

    def toDict(self):
        return {'id': self.id, 'arquivo': self.arquivo, 'cid10': self.cid10}
