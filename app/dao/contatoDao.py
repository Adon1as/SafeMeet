from ..model.contatoModel import ContatoModel
from ..conection import mysql


class ContatoDao():

    def saveContato(self, cpf, contato: ContatoModel):
        cursor = mysql.connection.cursor()
        cursor.execute('insert into contatos (tipo,ccontato,cdescricao, pcpf) values(%s,%s,%s,%s)',
                       (contato.tipo, contato.contato, contato.descricao, cpf))
        mysql.connection.commit()
        cursor.close()

    def getContatoContatosPorCpf(self, cpf):
        cursor = mysql.connection.cursor()
        cursor.execute(
            'select tipo, ccontato, cdescricao from contatos where pcpf = %s', (cpf,))
        result = cursor.fetchall()
        cursor.close()

        contatos = []
        if result:
            for i in result:
                tipo = i['tipo']
                ccontato = i['ccontato']
                cdescricao = i['cdescricao']
                contato = ContatoModel(tipo, ccontato, cdescricao)
                contatos.append(contato)

        return contatos

    def deletContato(self, ccontato):
        cursor = mysql.connection.cursor()
        cursor.execute('delete from contatos where ccontato = %s', (ccontato,))
        mysql.connection.commit()
        cursor.close()

    def deletContatosPorCpf(self, cpf):
        cursor = mysql.connection.cursor()
        cursor.execute('delete from contatos where pcpf = %s', (cpf,))
        mysql.connection.commit()
        cursor.close()

    def updateContato(self, cpf, contato: ContatoModel):
        cursor = mysql.connection.cursor()
        cursor.execute('update contatos set tipo = %s, ccontato = %s, cdescricao = %s where pcpf = %s and ccontato = contato.contato',
                       (contato.tipo, contato.contato, contato.descricao, cpf))
        mysql.connection.commit()
        cursor.close()
