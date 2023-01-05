from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/calculadora')
def homepage():
    boas_vindas = ('Bem vindo!! Exemplo de Operação:http://localhost:5000/calculadora/sum/3/2 =5 ')
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


app.run(port=5000, host='localhost', debug=True)
