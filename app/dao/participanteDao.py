from ..model.participanteModel import ParticipanteModel
from ..model.contatoModel import ContatoModel
from ..conection import mysql

class ParticipanteDao():

    def getParticipante(self,cpf):

        cursor = mysql.connection.cursor()
        cursor.execute('select * from pessoas, participantes, contatos where cpf = %s and cpf = pessoa_cpf and cpf = pessoas_cpf',(cpf,))
        result = cursor.fetchall()
        cursor.close()

        if result: 
            contato =  ContatoModel(result['tipo'] ,result['contato'],result['cdescricao'] )  
            cpf = result['cpf']
            nome = result['nome']
            sobrenome = result['sobrenome']
            dataNacimento = result['data_nascimento']
            instituicao = result['instituicao']
            endereco = result['endereco']
            contato =  contato
            meioDeTransporte = result['meio_transporte'] 
            horarioChegada = result['horario_chegada']
            horarioSaida = result['horario_saida'] 
            return ParticipanteModel(cpf,nome,sobrenome,dataNacimento,instituicao,endereco,contato,meioDeTransporte,horarioChegada,horarioSaida)

    def saveParticipante(self, participante:ParticipanteModel):

        cursor = mysql.connection.cursor()
        cursor.execute('insert into pessoas (cpf, nome, sobrenome, data_nascimento, instituicao, endereco) values(%s ,%s ,%s ,%s ,%s,%s)',(participante.cpf, participante.nome, participante.sobrenome, participante.dataNacimento, participante.instituicao,participante.endereco))
        cursor.execute('insert into participantes (meio_transporte,horario_chegada,horario_saida, pcpf) values(%s ,%s ,%s ,%s)',(participante.meioDeTransporte, participante.horarioChedada, participante.horarioSaida, participante.cpf))
        cursor.execute('insert into contatos (tipo,ccontato,cdescricao, pcpf) values(%s,%s,%s,%s)',(participante.contato.tipo,participante.contato.contato,participante.contato.descricao,participante.cpf))
        mysql.connection.commit()
        cursor.close()