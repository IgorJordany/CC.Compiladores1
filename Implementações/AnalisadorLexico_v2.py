def pReservada (token):
	reservadas = ['var', 'integer', 'real', 'if', 'then']
	if token in reservadas:
		return True
	return False

def operador (token):
	operadores = [':=','+']
	if token in operadores:
		return True
	return False

def delimitador (token):
	delimitadores = [':',',',';']
	if token in delimitadores:
		return True
	return False

def verificabuf(buf):
	if buf!="":
		return True
	return False
	
arq = open('codigo.txt','r')	# Abre o arquivo
texto = arq.read()	# Leitura do arquivo
buf = ""
linhatok = 1
for caracter in texto:
	if caracter == "\n":
		if verificabuf(buf):
			if pReservada(buf):
				print("palavra reservada ", buf, " linha ", linhatok)
				buf=""
			elif operador(buf):
				print("operador ",buf," linha ", linhatok)
				buf=""
			else:
				print("talvez ID")
				buf=""
		linhatok=linhatok+1
	elif caracter ==" ":
		if verificabuf(buf):
			if pReservada(buf):
				print("palavra reservada ", buf, " linha ", linhatok)
				buf=""
			elif operador(buf):
				print("operador ",buf," linha ", linhatok)
				buf=""
			else:
				print("talvez ID")
				buf=""
	elif delimitador(caracter):
		if verificabuf(buf):
			if pReservada(buf):
				print("palavra reservada ", buf, " linha ", linhatok)
				buf=""
			elif operador(buf):
				print("operador ",buf," linha ", linhatok)
				buf=""
			else:
				print("talvez ID")
				buf=""
		else:
			print("demilitador ",caracter," linha ", linhatok)
	elif operador(caracter):
		if verificabuf(buf):
			if pReservada(buf):
				print("palavra reservada ", buf, " linha ", linhatok)
				buf=""
			elif operador(buf):
				print("operador ",buf," linha ", linhatok)
				buf=""
			else:
				print("talvez ID")
				buf=""
		else:
			print("operador ",caracter," linha ", linhatok)
	else:
		buf=buf+caracter
arq.close()	# Fecha o arquivo codigo.txts