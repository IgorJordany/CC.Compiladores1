#-*- coding: utf-8 -*-
#201411310006 - Igor Jordany Richtic Silva

def Z(token,indice):
	indice = I(token,indice)
	if(indice==False):
		return False
	token=proxtoken(indice)
	S(token,indice)

def I(token,indice):
	if(token[1] == "var\n"):
		print("ok var")
		indice=indice+1
		token=proxtoken(indice)
		indice=D(token,indice)
	return indice

def D(token,indice):
	indice=L(token,indice)
	token=proxtoken(indice)
	if(token[1] == ":\n"):
		print("ok :")
		indice=indice+1
		token=proxtoken(indice)
		indice=K(token,indice)
		token=proxtoken(indice)
		indice=O(token,indice)
		return indice
	return False

def L(token,indice):
	if(token[0] == "identificador"):
		print("ok identificador")
		indice=indice+1
		token=proxtoken(indice)
		indice = X(token,indice)
	else:
		print("erro, esperado identificador")
	return indice

def X(token,indice):
	if(token[1] == ",\n"):
		print("ok ,")
		indice=indice+1
		token=proxtoken(indice)
		indice=L(token,indice)
	else:
		print("dibas se x for vazio")
	return indice

def K(token,indice):
	if(token[1] == "integer\n"):
		print("ok integer")
		indice=indice+1
		token=proxtoken(indice)
	elif(token[1] == "real\n"):
		print("ok real")
		indice=indice+1
		token=(proxtoken(indice))
	else:
		print("erro, esperado integer ou real")
	return indice

def O(token,indice):
	if(token[1] == ";\n"):
		print("ok ;")
		indice=indice+1
		token=proxtoken(indice)
		indice=D(token,indice)
	else:
		print("dibas se o for vazio")
	return indice

def S(token,indice):
	if(token[0] == "identificador"):
		print("ok identificador")
		indice=indice+1
		token=proxtoken(indice)
		if(token[1] == ":=\n"):
			print("ok :=")
			indice=indice+1
			token=proxtoken(indice)
			indice=E(token,indice)
	elif(token[1] == "if\n"):
		print("ok if")
		indice=indice+1
		token=proxtoken(indice)
		indice=E(token,indice)
		token=proxtoken(indice)
		if(toke[1] == "then\n"):
			print("ok then")
			indice=indice+1
			token=proxtoken(indice)
			indice=S(token,indice)
	else:
		print("erro, esperado atribuição ou condicional")
	return indice

def E(token,indice):
	indice=T(token,indice)
	token=proxtoken(indice)
	if(proxtoken(indice)==False):
		return False
	indice=R(token,indice)
	return indice

def R(token,indice):
	if(token[1] == "+\n"):
		print("ok +")
		indice=indice+1
		token=proxtoken(indice)
		indice=T(token,indice)
		token=proxtoken(indice)
		if(proxtoken(indice)==False):
			return False
		indice=R(token,indice)
	else:
		print("dibas se R for vazio")
	return indice

def T(token,indice):
	if(token[0] == "identificador"):
		print("ok identificador")
		indice=indice+1
	else:
		print("erro, esperado identificador")
	return indice

def proxtoken(indice):
	if indice < len(texto):
		return texto[indice].split(' ')
	else:
		return False

arq = open('tokens.txt','r')
texto = arq.readlines()
indice=0
token=(proxtoken(indice))
Z(token,indice)
arq.close()