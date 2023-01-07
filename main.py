from fastapi import FastAPI, Path
import os
app = FastAPI(title='Calculadora', description='Simples calculadora em Python e APIrest',version='1.0.0')

@app.get('/calculadora')
def homepage():
    return {"Bem": "Vindo"}


@app.get('/calculadora/soma/{n1}/{n2}')
def Operacao_soma(n1: int = Path(description='Variavel 1 do tipo inteiro'),  n2: int = Path(description='Variavel 2 do tipo inteiro')):
    soma = n1 + n2
    return soma


@app.get('/calculadora/sub/{n1}/{n2}')
def Operacao_Subtraao(n1: int = Path(description='Variavel 1 do tipo inteiro'),  n2: int = Path(description='Variavel 2 do tipo inteiro')):
    sub = n1 - n2
    return sub


@app.get('/calculadora/mult/{n1}/{n2}')
def Operacao_Multiplicacao(n1: int = Path(description='Variavel 1 do tipo inteiro'),  n2: int = Path(description='Variavel 2 do tipo inteiro')):
    mult = n1 * n2
    return mult


@app.get('/calculadora/div/{n1}/{n2}')
def Operacao_Divisao(n1: int = Path(description='Variavel 1 do tipo inteiro'),  n2: int = Path(description='Variavel 2 do tipo inteiro')):
    div = n1 / n2
    return div
