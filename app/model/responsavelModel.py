from pessoaModel import PeossoaModel

class ParticipanteModel(PeossoaModel):
    def __init__(self,cpf,nome,sobrenome,dataNacimento,instituicao,endreco,contato,cargo,eventos):
        super.__init__(self,cpf,nome,sobrenome,dataNacimento,instituicao,endreco,contato)
        self.cargo = cargo
        self.eventos = eventos
