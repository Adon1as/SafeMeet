from ..model.localModel import LocalModel
from ..conection import mysql

class LocalDao():

    def saveLocal(self, local:LocalModel):
        cursor = mysql.connection.cursor()
        cursor.execute(' values(%s,%s,%s,%s)',())
        mysql.connection.commit()
        cursor.close()