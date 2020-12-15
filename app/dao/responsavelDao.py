from ..model.responsavelModel import ResponsavelModel
from .pessoaDao import PessoaDao
from ..conection import mysql


class ResponsavelDao():

    def setResponsavel(self, reponsavel: ResponsavelModel):
        cursor = mysql.connection.cursor()
        cursor.execute('insert into respnsaveis (pcpf, cargo) values(%s ,%s)',
                       (reponsavel.cpf, reponsavel.cargo))
        mysql.connection.commit()
        cursor.close()

        PessoaDao.setPessoa(reponsavel)

    def getResponsavel(self, cpf):
        cursor = mysql.connection.cursor()
        cursor.execute('select * from responsaveis where pcpf = %s ', (cpf,))
        result = cursor.fetchone()
        cursor.close()
        if result:
            resposavel: ResponsavelModel
            resposavel = PessoaDao.getPessoa(cpf)
            resposavel.cargo = result['cargo']
            return resposavel

    def updateResponsavel(self, reponsavel: ResponsavelModel):
        cursor = mysql.connection.cursor()
        cursor.execute('update respnsaveis set cargo = %s where pcpf = %s)',
                       (reponsavel.cargo, reponsavel.cpf))
        mysql.connection.commit()
        cursor.close()

        PessoaDao.updatePessoa(reponsavel)

    def deleteResponsavel(self, cpf):
        cursor = mysql.connection.cursor()
        cursor.execute('delete from responsaveis where cpf = %s', (cpf,))
        mysql.connection.commit()
        cursor.close()
        PessoaDao.deletePessoa(cpf)

    def deleteApenasResponsavel(self, cpf):
        cursor = mysql.connection.cursor()
        cursor.execute('delete from responsaveis where cpf = %s', (cpf,))
        mysql.connection.commit()
        cursor.close()
