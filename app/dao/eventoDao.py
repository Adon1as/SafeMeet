from ..model.eventoModel import EventoModel
from ..conection import mysql

class eventoModel():

    def setEvento(self, id_local, evento:EventoModel):
        cursor = mysql.connection.cursor()
        cursor.execute('insert into eventos(comeco, fim, duracao, quantidade, descricao, local_id_local) values(%s,%s,%s,%s,%s,%s)',(evento.comeco,evento.fim,evento.duracao, evento.quantidade, evento.descricao, id_local))
        mysql.connection.commit()
        cursor.close()

    def getEventosPorLocal(self,id_local):    
        cursor = mysql.connection.cursor()
        cursor.execute('select * from eventos where local_id_local = %s',(id_local))
        result = cursor.fetchall()
        cursor.close()

        eventos = [] 
        if result:
            for i in result:
                id = i['id_evento']
                comeco = i['comeco']
                fim = i['fim']
                duracao = i['fim']
                quantidade = i['quantidade']
                descricao = i['descricao']
                id_local = i['local_id_local']
                
                evento = eventoModel(id, comeco, fim, duracao, quantidade, descricao, id_local)
                eventos.append(evento)

        return eventos

    def updateEventos(self, evento:EventoModel):
        cursor = mysql.connection.cursor()
        cursor.execute('update eventos set comeco = %s, fim = %s, duracao = %s, quantidade = %s, descricao = %s, id_local = %s where id_evento = %s', (evento.comeco, evento.fim, evento.duracao, evento.quantidade, evento.descricao, evento.id_local, evento.id))
        mysql.connection.commit()
        cursor.close()

    def deletarEvento(self,id):
        cursor = mysql.connection.cursor()
        cursor.execute('delete from eventos where id_evento = %s', (id,))
        mysql.connection.commit()
        cursor.close()
        