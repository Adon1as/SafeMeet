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

    def toDict(self):
        d = {}
        count = 0
        for c in self.contato:
             d.update({count:c.toDict()})
             count = count+1
            
        return {'cpf':self.cpf,'nome':self.nome,'sobrenome':self.sobrenome,'dataNacimento':self.dataNacimento,'instituicao':self.instituicao,'endereco':self.endereco, 'contato':d}        