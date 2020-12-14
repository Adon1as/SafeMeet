from .model import Model

class LocalModel(Model):
    def __init__(self,id,descricao,tipoVentilacao,nivelVentilacao,area,endereco):
        self.id = id
        self.descricao = descricao
        self.tipoVentilacao = tipoVentilacao
        self.nivelVentilacao = nivelVentilacao
        self.area = area
        self.endereco = endereco