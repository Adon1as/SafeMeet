from .pessoaModel import PessoaModel
import datetime


class ParticipanteModel(PessoaModel):
    def __init__(self, cpf, nome, sobrenome, dataNacimento, instituicao, endereco, contato, meioDeTransporte, horarioChegada, horarioSaida):
        super().__init__(cpf, nome, sobrenome, dataNacimento, instituicao, endereco, contato)
        self.meioDeTransporte = meioDeTransporte
        self.horarioChedada = horarioChegada
        self.horarioSaida = horarioSaida

    def __init__(self, pessoa: PessoaModel):
        super().__init__(pessoa.cpf, pessoa.nome, pessoa.sobrenome,
                         pessoa.dataNacimento, pessoa.instituicao, pessoa.endereco, pessoa.contato)
        self.meioDeTransporte = None
        self.horarioChedada = None
        self.horarioSaida = None

    def toDict(self):
        d = super().toDict()
        d.update({'meioDeTransporte': int(self.meioDeTransporte), 'horarioChegada': str(
            self.horarioChedada), 'horarioSaida': str(self.horarioSaida)})
        return d

    def getTempoViagem(self):
        return datetime.time(self.horarioChedada) - datetime.time(self.horarioChedada)
