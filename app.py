from flask import Flask
from pip._vendor import requests
app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)

r = requests.get(
    'http://localhost:3000/consultaInformacoesUsuariosPorPerfil/2' # mudar rota
).json()


@app.route('/')
def __init__(self):
    self.ticket = []


@app.route('/insere')
def entrar_na_fila(self):
    if(prioridade == 1):
        self.ticket.insert(0, elemento)
    elif(prioridade == 0):
        self.ticket.append(elemento)
    else:
        return "Prioridade inválida"


@app.route('/fila')
def fila_json(self):
    return fila.json()


@app.route('/proximo')
def chamar_proximo(self):
    return self.ticket.pop(0)
