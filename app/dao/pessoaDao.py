from ..model.pessoaModel import PessoaModel
from ..conection import mysql
from .contatoDao import ContatoDao


class PessoaDao():

    def setPessoa(self,pessoa:PessoaModel):
        cursor = mysql.connection.cursor()
        cursor.execute('insert into pessoas (cpf, nome, sobrenome, data_nascimento, instituicao, endereco) values(%s ,%s ,%s ,%s ,%s,%s)',(pessoa.cpf, pessoa.nome, pessoa.sobrenome, pessoa.dataNacimento, pessoa.instituicao,pessoa.endereco))
        mysql.connection.commit()
        cursor.close()

        ContatoDao().saveContato(pessoa.cpf,pessoa.contato)

    def getPessoa(self,cpf):
        cursor = mysql.connection.cursor()
        cursor.execute('select * from pessoas where cpf = %s ',(cpf,))
        result = cursor.fetchone()
        cursor.close()

        if result: 
            contato = ContatoDao().getContatoContatosPorCpf(cpf)
            cpf = result['cpf']
            nome = result['nome']
            sobrenome = result['sobrenome']
            dataNacimento = result['data_nascimento']
            instituicao = result['instituicao']
            endereco = result['endereco']
            contato =  contato
            return PessoaModel(cpf,nome,sobrenome,dataNacimento,instituicao,endereco,contato)
    
    def updatePessoa(self, pessoa:PessoaModel):
        cursor = mysql.connection.cursor()
        cursor.execute('update pessoas set nome = %s, sobrenome = %s, data_nascimento = %s, instituicao = %s, endereco = %s where cpf = %s',(pessoa.nome, pessoa.sobrenome, pessoa.dataNacimento, pessoa.instituicao,pessoa.endereco,pessoa.cpf))
        mysql.connection.commit()
        cursor.close()

    def deletePessoa(self, cpf):
        cursor = mysql.connection.cursor()
        cursor.execute('delete from pessoa where cpf = %s', (cpf,))
        mysql.connection.commit()
        cursor.close()

