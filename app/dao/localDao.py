from ..model.localModel import LocalModel
from ..conection import mysql

class LocalDao():

    def setLocal(self, local:LocalModel):
        cursor = mysql.connection.cursor()
        cursor.execute('insert into locais (descricao, tipoventilacao, nivelventilacao, area, endereco) values(%s,%s,%s,%s,%s)',(local.descricao,local.tipoVentilacao,local.nivelVentilacao,local.area,local.endereco))
        mysql.connection.commit()
        cursor.close()
        
    def getLocal(self, id):
        cursor = mysql.connection.cursor()
        cursor.execute('select * from locais where id_local = %s',(id,))
        mysql.connection.commit()
        cursor.close()
        
    def updateLocal(self, local:LocalModel):
        cursor = mysql.connection.cursor()
        cursor.execute('update locais set descricao = %s, tipoVentilacoa = %s, nivelVentilacao = %s, area = %s, endereco = %s where id_local = %s',(local.descricao,local.tipoVentilacao,local.nivelVentilacao,local.area,local.endereco, local.id_local))
        mysql.connection.commit()
        cursor.close()
        
    def deleteLocal(self, id):
        cursor = mysql.connection.cursor()
        cursor.execute('delete from locais where id_local = %s', (id,))
        mysql.connection.commit()
        cursor.close()