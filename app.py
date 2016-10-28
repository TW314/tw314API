from flask import Flask
# from pip._vendor import requests
from random import *

app = Flask(__name__)


if __name__ == '__main__':
	app.run(debug = True)


# r = requests.get('http://localhost:3000/consultaInformacoesUsuariosPorPerfil/2').json()
normal = []
prioritaria = []
total = []


@app.route('/')
def __init__():
	for i in range(99):
		prioridade = randint(0, 1)
		elemento = randint(0, 999)
		entrar_na_fila(elemento, prioridade)
	return priority()


@app.route('/insere')
def entrar_na_fila(elemento, prioridade):
	if prioridade == 1:
		prioritaria.append(elemento)
	elif prioridade == 0:
		normal.append(elemento)


def priority(n = 0, k = 0):
	total = normal.copy()
	for i in range(len(normal+prioritaria)):
		total.insert(n, 0)
		n += 3
	for j in range(len(total)):
		if k < len(prioritaria):
			total.insert(total.index(0), prioritaria[k])
			k += 1
		if 0 in total:
			total.remove(0)
	return fila_json(total)


@app.route('/fila')
def fila_json(total):
	res = "TOTAL: " + str(total) + "<br>" + "PRIORITARIA: " + str(prioritaria) + "<br>" + "NORMAL: " + str(normal)
	return res


@app.route('/proximo')
def chamar_proximo():
	return total.pop(0)
