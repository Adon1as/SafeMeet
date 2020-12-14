from model import Model

class EnderecoModel(Model):
    def __init__(self,id,rua,numero,bairro,cidade,uf,cep):
        self.id = id
        self.rua = rua
        self.numero = numero
        self.bairro = bairro
        self.cidade = cidade
        self.uf = uf
        self.cep = cep
