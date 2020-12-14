from ..model.atestadoModel import AtestadoModel
from ..conection import mysql

class AtestadoDao():

    def setAtestado(self,cpf,atestado:AtestadoModel):
        cursor = mysql.connection.cursor()
        cursor.execute('insert into atestados(arquivo,cid-10,Participante_Pessoa_cpf) velues(%s,%s,%s)',(cpf,atestado.arquivo,atestado.cid10))
        mysql.connection.commit()
        cursor.close()

    def getAtestadosPorCpf(self,cpf):
        
        cursor = mysql.connection.cursor()
        cursor.execute('select id_atestado,arquivo,cid-10 from atestados where Participante_Pessoa_cpf = %s',(cpf,))
        result = cursor.fetchone()
        cursor.close()

        atestados = [] 
        if result:
            for i in result:
                id = i['id_atestado']
                arquivo = i['arquivo']
                cid10 = i['cid-10']
                atestado = AtestadoModel(id,arquivo,cid10)
                atestados.append(atestado)
        
        return atestados
    
    def deletarAtestado(self,id):
        cursor = mysql.connection.cursor()
        cursor.execute('delete from atestados where id_atestado = %s', (id,))
        mysql.connection.commit()
        cursor.close()

    def deletarAtestadosPorCpf(self,cpf):
        cursor = mysql.connection.cursor()
        cursor.execute('delete from atestados where Participante_Pessoa_cpf = %s', (cpf,))
        mysql.connection.commit()
        cursor.close()
    
        