from app.dao.contatoDao import ContatoDao
from app.conection import app
from app.model.contatoModel import ContatoModel
from flask import Flask, render_template, jsonify


@app.route("/")
def index():
    contato = ContatoDao().getContatoContatosPorCpf('001')[0].toDict()

    return render_template('index.html', contato=contato)


if __name__ == '__main__':
    app.run(debug=True)
