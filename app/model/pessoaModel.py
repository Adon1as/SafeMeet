from .model import Model

class PessoaModel(Model):
    def __init__(self,cpf,nome,sobrenome,dataNacimento,instituicao,endereco,contato):
        self.cpf = cpf
        self.nome = nome
        self.sobrenome = sobrenome
        self.dataNacimento = dataNacimento
        self.instituicao = instituicao
        self.endereco = endereco
        self.contato= contato