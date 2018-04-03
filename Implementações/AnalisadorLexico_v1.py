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

arq = open('codigo.txt','r')	# Abre o arquivo
texto = arq.read()	# Leitura do arquivo
buffer = ""
linhatok = 1
for caracter in texto:
	if caracter == "\n":
		linhatok=linhatok+1        
        if(buffer == ""):
            print("otario")
	elif delimitador(caracter):
		print("demilitador ",caracter," linha ", linhatok)
	elif operador(caracter):
		print("operador ",caracter," linha ", linhatok)
	elif operador(buffer):
		print("operador ",caracter," linha ", linhatok)
arq.close()	# Fecha o arquivo codigo.txts