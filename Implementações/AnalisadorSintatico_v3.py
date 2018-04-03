#-*- coding: utf-8 -*-
#201411310006 - Igor Jordany Richtic Silva

def Z():
	global retorno
	retorno = I()
	if(retorno==False):
		return False
	retorno=S()
	if(retorno==False):
		return False
	else:
		print("Codigo valido")

def I():
	token = proxtoken()
	global indice
	global retorno
	print("token")
	if(token[1] == "var\n"):
		print("ok var")
		indice=indice+1
		token=proxtoken()
		retorno=D()
		if(indice==False):
			return False
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
	token=proxtoken()
	if(token==False):
		print("erro, esperado identificador")
		return False
	elif(token[0] == "identificador"):
		print("ok identificador")
		indice=indice+1
		token=proxtoken()
		retorno = X()
		if(indice==False):
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
	token=proxtoken()
	if(token==False):
		print("erro, esperado integer ou real")
		return False
	elif(token[1] == "integer\n"):
		print("ok integer")
		indice=indice+1
		token=proxtoken()
	elif(token[1] == "real\n"):
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
		print("dibas se o for vazio")

def S():
	global indice
	global retorno
	token=proxtoken()
	if(token==False):
			print("erro, esperado identificador")
			return False
	if(token[0] == "identificador"):
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
		print("ok identificador")
		indice=indice+1
	else:
		print("erro, esperado identificador")
		return False
	return True

def proxtoken():
	if indice < len(texto):
		return texto[indice].split(' ')
	else:
		return False

arq = open('tokens.txt','r')
texto = arq.readlines()
indice = 0
retorno= False
Z()
arq.close()