from app.dao.contatoDao import ContatoDao
from app.conection import app
from flask import Flask, render_template

@app.route("/")
def index():
    contato = ContatoDao().getContatoContatosPorCpf('001')

    return render_template('index.html', contato = contato)


if __name__ == '__main__':
    app.run(debug=True)
