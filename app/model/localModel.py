from .model import Model

class LocalModel(Model):
    def __init__(self,descricao,tipoVentilacao,nivelVentilacao,area,endereco):
        self.descricao = descricao
        self.tipoVentilacao = tipoVentilacao
        self.nivelVentilacao = nivelVentilacao
        self.area = area
        self.endereco = endereco