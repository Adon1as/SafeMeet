from .pessoaModel import PeossoaModel

class ParticipanteModel(PeossoaModel):
    def __init__(self,cpf,nome,sobrenome,dataNacimento,instituicao,endereco,contato,meioDeTransporte,horarioChegada,horarioSaida):
        super().__init__(cpf,nome,sobrenome,dataNacimento,instituicao,endereco,contato)
        self.meioDeTransporte = meioDeTransporte
        self.horarioChedada = horarioChegada
        self.horarioSaida = horarioSaida