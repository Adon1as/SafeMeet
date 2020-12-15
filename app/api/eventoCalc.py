from ..model.eventoModel import EventoModel
from ..dao.eventoDao import EventoDao
import datetime
import time

class EventoCalc():
    
    evento = EventoDao().getEventosPorId()
    tipoVentilacoaEnum = {'1':1,'2':1.5}
    
    def calc(self):
        self.evento.quantidade = 1
        if(self.evento.local.area > 14):
            self.quantidade = int ((self.evento.local/14) * self.tipoVentilacoaEnum[self.evento.local.tipoVentilacao])

        for self.particpantes in self.evento.participantes:
            pass
            
    def liberarHoarios(self):
        hoarios = {} 
        comeco = datetime.datetime(self.evento.comeco)
        fim = datetime.datetime(self.evento.fim) 
        skipTime = datetime.time('18:00:00')

        while comeco != fim:
            for i in range(self.quantidade)
                hoarios.update({comeco:None})
            
            comeco += datetime.timedelta(minutes=self.evento.tempoMax)

            if(comeco.time == skipTime):
               comeco.timedelta(hours=14) 
        
        

        


