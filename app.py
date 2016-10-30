from flask import Flask
# from pip._vendor import requests
from random import *
import string

app = Flask(__name__)

# r = requests.get('http://localhost:3000/consultaInformacoesUsuariosPorPerfil/2').json()
# ## GLOBAIS ##
normal = []  # eh zerada apos inserir em total
prioritaria = []  # zerada apos inserir em total
total = []
ins = 0
c = 5
count_insere = False


@app.route('/')
def fila():
	return priority()


@app.route('/insere')
def entrar_na_fila():
	# simulando valores
	global count_insere
	global ins
	ins += 1
	prioridade = randint(0, 1)
	elemento = randint(0, 999)
	eh_maior_que_c(prioridade, elemento)
	count_insere = True
	return "NORMAL: " + str(normal) + "<br>" + "PRIORITÁRIO: " + str(prioritaria)


def eh_maior_que_c(prioridade, elemento):
	if prioridade == 1:
		prioritaria.append(elemento)
	elif prioridade == 0:
		normal.append(elemento)


def nao_eh_maior_que_c(prioridade, elemento):
	global total
	eh_maior_que_c(prioridade, elemento)
	total = prioritaria + normal


@app.route('/proximo')
def chamar_proximo():
	res = total.pop(0) if total else None
	return str(res)


def monta_total(n, k):
	t = []
	global normal, prioritaria, total
	if normal or prioritaria:
		if ins > c:
			t.extend(normal.copy())
			for i in range(len(normal + prioritaria)):
				t.insert(n, 0)
				n += 3
			for j in range(len(t)):
				if k < len(prioritaria):
					t.insert(t.index(0), prioritaria[k])
					k += 1
				if 0 in t:
					t.remove(0)
			total.extend(t)
		elif ins <= c:
			total.extend(prioritaria + normal)
		else:
			pass
		normal = []
		prioritaria = []


def priority(k = 0):
	global count_insere
	if count_insere:
		n = 0
		monta_total(n, k)
		count_insere = False
	return str(total)


if __name__ == '__main__':
	app.run(debug = True)
