from app.dao.participanteDao import ParticipanteDao
from app.model.participanteModel import ParticipanteModel
from app.model.contatoModel import ContatoModel
from app.dao.contatoDao import ContatoDao
from app.model.contatoModel import ContatoModel
#from app.model.enderecoModel import EnderecoModel
from app.conection import app


@app.route('/salvar')
def salvar():
    contato = ContatoModel(1,'084','sl')
    
    participante = ParticipanteModel('001','Ze','da Silva','1970-10-10','instituicao','rua 1, numero 2',contato,'1','14:30:00','14:00:00')
    ParticipanteDao.saveParticipante(participante,participante)
    return 'salvo'

@app.route('/pegar')
def pegar():
    cpf = '001'
    participante = ParticipanteDao.getParticipante(cpf,cpf)

    return participante.cpf

@app.route('/getContato')
def getContato():
    cpf = '01'
    contato = ContatoDao.getContatoContatosPorCpf(cpf,cpf)

    return contato[0].contato
    

if __name__ == '__main__':
    app.run(debug=True)
