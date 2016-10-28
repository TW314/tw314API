from flask import Flask
# from pip._vendor import requests
from random import *
import string

app = Flask(__name__)

if __name__ == '__main__':
	app.run(debug = True)

# r = requests.get('http://localhost:3000/consultaInformacoesUsuariosPorPerfil/2').json()
normal = []
prioritaria = []
c = 10


@app.route('/')
def __init__():
	return str(total)


@app.route('/insere')
def entrar_na_fila():
	# simulando valores
	prioridade = randint(0, 1)
	elemento = randint(0, 999)
	if len(total) > c:
		return eh_maior_que_c(prioridade, elemento)
	else:
		return nao_eh_maior_que_c(prioridade, elemento, 1)


# todo: bug aqui
def eh_maior_que_c(prioridade, elemento):
	for i in range(c):
		if prioridade == 1:
			prioritaria.append(elemento)
		elif prioridade == 0:
			normal.append(elemento)
		return priority()


def nao_eh_maior_que_c(prioridade, elemento, i):
	i += 1
	if prioridade == 1:
		total.insert(i, elemento)
	elif prioridade == 0:
		total.append(elemento)
	return str(total)


@app.route('/proximo')
def chamar_proximo():
	return str(total.pop(0))


total = normal.copy()


def priority(n = 0, k = 0):
	for i in range(len(normal + prioritaria)):
		total.insert(n, 0)
		n += 3
	for j in range(len(total)):
		if k < len(prioritaria):
			total.insert(total.index(0), prioritaria[k])
			k += 1
		if 0 in total:
			total.remove(0)
	return str(total)


print(''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits)))
