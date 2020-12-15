from ..model.participanteEventoModel import ParticipanteEventoModel
from ..model.participanteModel import ParticipanteModel
from ..model.eventoModel import EventoModel
from .participanteDao import ParticipanteDao
from .eventoDao import EventoDao

class ParticipanteEventoDao():

    def setParticipanteEvento(self, participanteEvento:ParticipanteEventoModel):

    def getParticipanteEvento(self,eid_local,ppcpf):

    def updateParticipanteEvento(self, participanteEvento:ParticipanteEventoModel):

    def deleteParticipanteEvento(self,id,cpf):

    def getParticipantesDeEvento(self,id):

    def getEventosDeParticipante(self,cpf):