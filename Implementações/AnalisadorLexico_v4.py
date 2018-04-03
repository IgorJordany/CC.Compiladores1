#-*- coding: utf-8 -*-
#201411310006 - Igor Jordany Richtic Silva

def pReservada (token): # testa se token é palavra reservada
	reservadas = ['var', 'integer', 'real', 'if', 'then']
	if token in reservadas:
		return True
	return False

def operador (token): # testa se token é operador
	operadores = [':=','+']
	if token in operadores:
		return True
	return False

def delimitador (token): # testa se token é delimitador
	delimitadores = [':',',',';']
	if token in delimitadores:
		return True
	return False

def verificabuf(buf): # verifica se buffer contem caracter
	if buf!="":
		return True
	return False

def proxcaracter(texto,indice): # pega caracter da entrada de acordo com indice
	if indice < len(texto):
		return texto[indice]
	elif indice == len(texto):
		return "\n"
	else:
		return False

def pesquisabuf(buf): # testa se buffer contem simbolo não aceitavel para identificador
	simbolo = '''!#$%&'()*+-./0123456789:;<>?[\]^`{|}~@'''
	for car in buf:
		if car in simbolo:
			return True
	return False
			
def identcaracter(buf,tokens): # testa se token é palavra reservada/operador/identificador
	if pReservada(buf):
		tokens.append("preservada "+buf+"\n")
		print(buf, " ---- palavra reservada")
	elif operador(buf):
		tokens.append("operador "+buf+"\n")
		print(buf," ---- operador ")
	elif pesquisabuf(buf):
		print(buf," ---- erro lexico")
		return "erro lexico"
	else:
		tokens.append("identificador "+buf+"\n")
		print(buf, " ---- identificador")

def analisadorlexico(texto):
	buf = ""
	tokens=[]
	indice = 0
	while proxcaracter(texto,indice) != False:
		caracter = proxcaracter(texto,indice)
		if caracter == "\n": # ao encontrar \n e tiver algo no buffer = identificar token no buffer
			if verificabuf(buf):
				if identcaracter(buf,tokens) == "erro lexico":
					return "erro lexico"
				buf=""
				indice = indice + 1
			else:
				indice = indice + 1
		elif caracter == " ": # ao encontrar espaço e tiver algo no buffer = identificar token no buffer
			if verificabuf(buf):
				if identcaracter(buf,tokens) == "erro lexico":
					return "erro lexico"
				buf=""
				indice = indice + 1
			else:
				indice = indice + 1
		elif delimitador(caracter): # ao encontrar delimitar e tiver algo no buffer = identificar token no buffer e token atual
			if verificabuf(buf):
				if identcaracter(buf,tokens) == "erro lexico":
					return "erro lexico"
				buf=""
				if proxcaracter(texto,indice+1) == '=':
					buf = buf + caracter
					buf = buf + proxcaracter(texto,indice+1)
					if identcaracter(buf,tokens) == "erro lexico":
						return "erro lexico"
					buf=""
					indice = indice + 2
			elif proxcaracter(texto,indice+1) == '=':
				buf = buf + caracter
				buf = buf + proxcaracter(texto,indice+1)
				if identcaracter(buf,tokens) == "erro lexico":
					return "erro lexico"
				buf=""
				indice = indice + 2
			else:
				tokens.append("delimitador "+caracter+"\n")
				print(caracter, " ---- delimitador")
				indice = indice + 1
		elif operador(caracter):
			if verificabuf(buf):
				if identcaracter(buf,tokens) == "erro lexico":
					return "erro lexico"
				print(caracter," ---- operador")
				buf=""
				indice = indice + 1
			else:
				tokens.append("operador "+caracter+"\n")
				print(caracter," ---- operador")
				indice = indice + 1
		else:
			buf=buf+caracter
			indice = indice + 1
	arqt.writelines(tokens)
arqc = open('codigo.txt','r')	# Abre o arquivo
arqt = open('tokens.txt','w')
texto = arqc.read()	# Leitura do arquivo
analisadorlexico(texto)
arqc.close()	# Fecha o arquivo codigo.txts
arqt.close()