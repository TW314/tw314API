from flask import Flask
# from pip._vendor import requests
from random import *

app = Flask(__name__)

# r = requests.get('http://localhost:3000/consultaInformacoesUsuariosPorPerfil/2').json()
# ## GLOBAIS ##
normal = []  # eh zerada apos inserir em total
prioritaria = []  # zerada apos inserir em total
total = []
ins = 0
c = 5
se_inseriu = False # flag para controle se está inserindo ou não


# mostra lista contendo a fila já organizada
@app.route('/mostrar_fila')
def fila():
	return str(total)


# insere elemento vindo do banco na fila - todo: definir for por tamanha do request
@app.route('/inserir_na_fila')
def entrar_na_fila():
	# simulando valores
	global se_inseriu
	global ins
	ins += 1
	# valores para teste - todo : puxar valores reais
	prioridade = randint(0, 1)
	elemento = randint(0, 999)
	
	inserir_nos_auxiliares(prioridade, elemento)
	# se_inseriu = True
	priority()
	return "NORMAL: " + str(normal) + "<br>" + "PRIORITÁRIO: " + str(prioritaria)


# insere elementos nas filas auxiliares prioritaria e normal, de acordo com a prioridade
def inserir_nos_auxiliares(prioridade, elemento):
	if prioridade == 1:
		prioritaria.append(elemento)
	elif prioridade == 0:
		normal.append(elemento)


# pop na lista total do ultimo elemento se total nao for vazio
@app.route('/chamar_proximo')
def pop_total():
	return str(total.pop(0) if total else None)


# insere elementos dos auxiliares na lista total de acordo com a regra de negocio
def monta_total(n, k):
	global normal, prioritaria, total # chamando listas globais dentro do metodo
	if normal or prioritaria:   # verifica se ha valor nas listas auxiliares
		if ins > c:      # se quantidade de insercoes for maior que parametrizacao pelo usuario
			total = normal.copy()
			for i in range(len(normal + prioritaria)):
				total.insert(n, 0) # insere 0 na posicao n de total
				n += 3
			for j in range(len(total)):
				if k < len(prioritaria):
					total.insert(total.index(0), prioritaria[k]) # insere elementos prioritarios nas posicoes onde ha 0
					k += 1
				if 0 in total: # remove elementos de valor 0 da lista total
					total.remove(0)
		elif ins <= c:     # se quantidade de insercoes for menor que parametrizacao pelo usuario
			total = prioritaria.copy() + normal.copy() # total recebe soma entre prioritaria e norma (nessa ordem)


def priority(k = 0):
	global se_inseriu
	# if se_inseriu: # se flag de
	n = 0
	monta_total(n, k)
	#se_inseriu = False
	return str(total)


if __name__ == '__main__':
	app.run(debug = True)
