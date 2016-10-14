from flask import Flask
from pip._vendor import requests
app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)


@app.route('/', method=['GET'])
def __init__(self):
    self.ticket = []


@app.route('/insere')
def entrar_na_fila(self, elemento):
    self.ticket.append(elemento)


def chamar_proximo(self):
    return self.ticket.pop(0)
