#-*- coding: utf-8 -*-
#201411310006 - Igor Jordany Richtic Silva
from AnalisadorLexico_v4 import *

def Z():
	global retorno
	global tabelaDeSimbolo
	retorno = I()
	if(retorno==False):
		return False
	retorno=S()
	if(retorno==False):
		return False
	else:
		print("Codigo valido")
		print(tabelaDeSimbolo)

def I():
	token = proxtoken()
	global indice
	global retorno
	if(token[1] == "var\n"):
		print("ok var")
		indice=indice+1
		token=proxtoken()
		D()
	else:
		print("erro, esperado var")
		return False
	return True

def D():
	global indice
	global retorno
	retorno=L()
	if(retorno==False):
		return False
	token=proxtoken()
	if(token[1] == ":\n"):
		print("ok :")
		indice=indice+1
		token=proxtoken()
		retorno=K()
		if(retorno==False):
			return False
		token=proxtoken()
		if(token==False):
			return False
		retorno=O()
		if(retorno==False):
			return False
	else:
		print("erro, esperado delimitador")
		return False
	return False

def L():
	global indice
	global retorno
	global listaux
	token=proxtoken()
	if(token==False):
		print("erro, esperado identificador")
		return False
	elif(token[0] == "identificador"):
		listaux.append(token[1])
		print(listaux)
		print("ok identificador")
		indice=indice+1
		token=proxtoken()
		retorno = X()
		if(retorno==False):
			return False
	else:
		print("erro, esperado identificador")
		return False

def X():
	global indice
	global retorno
	token=proxtoken()
	if(token==False):
		print("erro, esperado , ou :")
		return False
	elif(token[1] == ",\n"):
		print("ok ,")
		indice=indice+1
		token=proxtoken()
		retorno=L()
		if(retorno==False):
			return False
	else:
		print("dibas se x for vazio")

def K():
	global indice
	global retorno
	global listaux
	token=proxtoken()
	if(token==False):
		print("erro, esperado integer ou real")
		return False
	elif(token[1] == "integer\n"):
		retorno = insereTabelaDeSimbolo(listaux,token[1])
		listaux=[]
		if retorno==False:
			return False
		print("ok integer")
		indice=indice+1
		token=proxtoken()
	elif(token[1] == "real\n"):
		retorno = insereTabelaDeSimbolo(listaux,token[1])
		listaux=[]
		if retorno==False:
			return False
		print("ok real")
		indice=indice+1
		token=(proxtoken())
	else:
		print("erro, esperado integer ou real")
		return False

def O():
	global indice
	global retorno
	token=proxtoken()
	if(token==False):
			return False
	if(token[1] == ";\n"):
		print("ok ;")
		indice=indice+1
		token=proxtoken()
		retorno=D()
		if(retorno==False):
			return False
	else:
		print("dibas se O for vazio")

def S():
	global indice
	global retorno
	global tiposaux
	token=proxtoken()
	if(token==False):
			print("erro, esperado identificador")
			return False
	if(token[0] == "identificador"):
		if buscaTipo(token[1]):
			tiposaux = buscaTipo(token[1])
		else:
			print("erro semântico, variavel não declarada")
			return False
		print("ok identificador")
		indice=indice+1
		token=proxtoken()
		if(token==False):
			print("erro, esperado :=")
			return False
		if(token[1] == ":=\n"):
			print("ok :=")
			indice=indice+1
			token=proxtoken()
			retorno=E()
			if(retorno==False):
				return False
		else:
			print("erro, esperado operador :=")
			return False
	elif(token[1] == "if\n"):
		print("ok if")
		indice=indice+1
		token=proxtoken()
		if buscaTipo(token[1]):
			tiposaux = buscaTipo(token[1])
		else:
			print("erro semântico, variavel não declarada")
			return False
		retorno=E()
		if(retorno==False):
			return False
		token=proxtoken()
		if(token[1] == "then\n"):
			print("ok then")
			indice=indice+1
			token=proxtoken()
			retorno=S()
			if(retorno==False):
				return False
		else:
			print("erro, esperado palavra reservada then")
			return False
	else:
		print("erro, esperado atribuição ou condicional")
		return False
	return True

def E():
	global indice
	global retorno
	retorno=T()
	if(proxtoken()==False):
		return True
	token=proxtoken()
	retorno=R()
	if(retorno==False):
		return False
	return True

def R():
	global indice
	global retorno
	token=proxtoken()
	if(retorno==False):
		return False
	elif(token[1] == "+\n"):
		print("ok +")
		indice=indice+1
		token=proxtoken()
		retorno=T()
		if(retorno==False):
			return False
		token=proxtoken()
		if(proxtoken()==False):
			return True
		retorno=R()
	elif(token[1]=="then\n"):
		return True
	else:
		print(token)
		print("erro, esperado operador +")
		return False
	return True

def T():
	global indice
	global retorno
	token=proxtoken()
	if(token==False):
		print("erro, esperado identificador")
		return False
	elif(token[0] == "identificador"):
		if busca(token[1]):
			if tiposaux and buscaTipo(token[1]):
				if buscaTipo(token[1])!=tiposaux:
					print("erro semântico, tipos diferentes")
					return False
			print("ok identificador")
			indice=indice+1
		else:
			print("erro semântico, variavel não declarada")
			return False
	else:
		print("erro, esperado identificador")
		return False
	return True

def proxtoken():
	if indice < len(texto):
		return texto[indice].split(' ')
	else:
		return False

def busca(lex):
	global tabelaDeSimbolo
	for lista in tabelaDeSimbolo:
		if lex in lista:
			return True

def buscaTipo(lex):
	global tabelaDeSimbolo
	for lista in tabelaDeSimbolo:
		if lex in lista:
			return lista[1]

def insereTabelaDeSimbolo(listaux,tipo):
	global tabelaDeSimbolo
	for lex in listaux:
		if not busca(lex):
			tabelaDeSimbolo.append([lex,tipo])
			print(tabelaDeSimbolo)
		else:
			print("Variavel já declarada")
			return False

arq = open('tokens.txt','r')
tabelaDeSimbolo = []
listaux = []
tiposaux = []
texto = arq.readlines()
indice = 0
retorno= False
Z()
arq.close()