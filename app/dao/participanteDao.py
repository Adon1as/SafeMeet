from ..model.participanteModel import ParticipanteModel
from .pessoaDao import PessoaDao
from ..conection import mysql

class ParticipanteDao():

    def setParticipante(self, participante:ParticipanteModel):
        PessoaDao().setPessoa(participante)
        cursor = mysql.connection.cursor()
        cursor.execute('insert into participantes (meio_transporte,horario_chegada,horario_saida, pcpf) values(%s ,%s ,%s ,%s)',(participante.meioDeTransporte, participante.horarioChedada, participante.horarioSaida, participante.cpf))
        mysql.connection.commit()
        cursor.close()

    def getParticipante(self,cpf):
        cursor = mysql.connection.cursor()
        cursor.execute('select * from participantes where pcpf = %s',(cpf,))
        result = cursor.fetchone()
        cursor.close()

        if result:
            participante =ParticipanteModel(PessoaDao().getPessoa(cpf))
            participante.meioDeTransporte = result['meio_transporte'] 
            participante.horarioChegada = result['horario_chegada']
            participante.horarioSaida = result['horario_saida'] 
            return participante
