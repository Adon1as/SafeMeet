from ..model.participanteEventoModel import ParticipanteEventoModel
from ..model.participanteModel import ParticipanteModel
from ..model.eventoModel import EventoModel
from .participanteDao import ParticipanteDao
from .eventoDao import EventoDao
from ..conection import mysql


class ParticipanteEventoDao():

    def setParticipanteEvento(self, participanteEvento: ParticipanteEventoModel):
        cursor = mysql.connection.cursor()
        cursor.execute('insert into participa (ppcpf,eid_evento,horario,tratamento_especial) values(%s ,%s ,%s ,%s)', (
            participanteEvento.cpf, participanteEvento.eventoId, participanteEvento.horario, participanteEvento.tratamentoEsp))
        mysql.connection.commit()
        cursor.close()

    def getParticipanteEvento(self, id, cpf):
        cursor = mysql.connection.cursor()
        cursor.execute(
            'select * from participa where ppcpf = %s and eid_evento', (id, cpf))
        result = cursor.fetchone()
        cursor.close()

        if result:
            horario = result['horario']
            tratamentoEsp = result['hortratamento_especialario']
            return ParticipanteEventoModel(cpf, id, horario, tratamentoEsp)

    def updateParticipanteEvento(self, participanteEvento: ParticipanteEventoModel):
        pass

    def deleteParticipanteEvento(self, id, cpf):
        cursor = mysql.connection.cursor()
        cursor.execute(
            'delete from participa where ppcpf = %s and eid_evento', (cpf, id))
        mysql.connection.commit()
        cursor.close()

    def getParticipantesDeEvento(self, id):
        pass

    def getEventosDeParticipante(self, cpf):
        pass
