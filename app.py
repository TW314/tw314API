from flask import Flask
# from pip._vendor import requests
from random import *
import string

app = Flask(__name__)

if __name__ == '__main__':
	app.run(debug = True)

# r = requests.get('http://localhost:3000/consultaInformacoesUsuariosPorPerfil/2').json()
# ## GLOBAIS
normal = []
prioritaria = []
total = [0]
empty = []
c = 10


@app.route('/')
def __init__():
	return priority()


@app.route('/insere')
def entrar_na_fila():
	# simulando valores
	prioridade = randint(0, 1)
	elemento = randint(0, 999)
	eh_maior_que_c(prioridade, elemento)
	return "NORMAL: " + str(normal) + "<br>" + "PRIORITÁRIO: " + str(prioritaria)


def eh_maior_que_c(prioridade, elemento):
	if prioridade == 1:
		prioritaria.append(elemento)
	elif prioridade == 0:
		normal.append(elemento)

# todo: Pensar em lógica melhor pra quando a fila ainda for pequena
"""
def nao_eh_maior_que_c(prioridade, elemento, i):
	i += 1
	if prioridade == 1:
		total.insert(i, elemento)
	elif prioridade == 0:
		total.append(elemento)
	return str(total)
"""


@app.route('/proximo')
def chamar_proximo():
	return str(total.pop(0))


def priority(n = total.index(total[-1]), k = 0):
	if total != empty:
		if normal or prioritaria != empty:
			total.extend(normal.copy())
			for i in range(len(normal + prioritaria)):
				total.insert(n, 0)
				n += 3
			for j in range(len(total)):
				if k < len(prioritaria):
					total.insert(total.index(0), prioritaria[k])
					k += 1
				if 0 in total:
					total.remove(0)
		# normal[:] = empty[:]
		# prioritaria[:] = empty[:]
	return str(total)
