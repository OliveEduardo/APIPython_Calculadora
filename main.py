import os
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)

cors = CORS(app, resource={r'/*':{'origins':'*'}})
@app.route('/calculadora')
def homepage():
    boas_vindas = ('Bem vindo!! Exemplo de Operacao:https://api-calculadorapython.herokuapp.com/calculadora/sum/3/2')
    return jsonify(boas_vindas)


@app.route('/calculadora/sum/<int:n1>/<int:n2>', methods=['GET'])
def soma(n1, n2):
    soma = n1 + n2
    return jsonify(soma)


@app.route('/calculadora/sub/<int:n1>/<int:n2>', methods=['GET'])
def subtracao(n1, n2):
    sub = n1 - n2
    return jsonify(sub)


@app.route('/calculadora/div/<int:n1>/<int:n2>', methods=['GET'])
def divisao(n1, n2):
    divisao = n1 / n2
    return jsonify(divisao)


@app.route('/calculadora/mult/<int:n1>/<int:n2>', methods=['GET'])
def multiplicar(n1, n2):
    mult = n1 * n2
    return jsonify(mult)


def main():
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

if __name__ == '__main__':
    main()