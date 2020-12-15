from app.dao.atestadoDao import AtestadoDao
from app.dao.contatoDao import ContatoDao
from app.dao.eventoDao import EventoDao
from app.dao.localDao import LocalDao
from app.dao.participanteDao import ParticipanteDao

from app.model.atestadoModel import AtestadoModel
from app.model.contatoModel import ContatoModel
from app.model.eventoModel import EventoModel
from app.model.localModel import LocalModel
from app.model.participanteModel import ParticipanteModel


from app.conection import mysql
from app.conection import app
import random

nome = ['Iago','Adonias','Zé','João','Maria','Lucia','Fabia','Xuxa','Daniela','Mario']
sobrenome = ['da Silva','Araújo Galvão','Mercedes Benz','Barreto','Roussef','Meirelles','Garcia','Medeiros','Araújo','Abdias']
nascimento = ['1980-11-30','1972-09-12','2001-02-01','2005-11-01','1999-08-10',]
instituição = ['IFRN','IMD','UFRN','AABB','Valve']
endereço = ['Rua do Berilo, 122','Av. Tungstenio, 03','Rua Gervasio Souto, 1002','Rua do Topázio, 09','Rua do Galo, 643']

@app.route('/popular')
def popular():        
    cursor = mysql.connection.cursor()
    cursor.execute('DELETE FROM participantes')
    cursor.execute('DELETE FROM contatos')
    cursor.execute('DELETE FROM locais')
    cursor.execute('DELETE FROM pessoas')
    cursor.close()    
    
    for i in range(0, 10):
        x = random.randint(0,9)
        y = random.randint(0,4)
        z = random.randint(1,3)
        k = random.randint(1,5)
        
        participante = ParticipanteModel('00' + str(i),nome[x],sobrenome[x],nascimento[y],instituição[y],endereço[y],ContatoModel('1','00000000' + str(i),'Isso é uma descrição'), z,'1'+ str(x) +':30:00','14:00:00')
        ParticipanteDao.saveParticipante(participante,participante)
        
        localizacao = LocalModel('Isso é a descrição do local',z,k,(x + 2)*(y + 2),'Endereço ' + str(i))
        LocalDao.setLocal(localizacao,localizacao)
        
    return 'Done.'

if __name__ == '__main__':
    app.run(debug=True)