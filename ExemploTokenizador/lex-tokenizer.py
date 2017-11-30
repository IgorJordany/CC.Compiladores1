# -*- coding: utf-8 -*-    # permite colocar caracteres acentuados nestes programas/scripts
#!/usr/bin/python3      # indica ao script onde está o interpretador Python no ambiente Linux
#tokenizando um arquivo contendo o código fonte da linguagem a ser compilada

import nltk

fd = open('arqFonte','r')
stream = fd.read()

ident = '\w+'
pont = '\(|\)|\{|\;|\}'

reg = ident + '|' + pont

tokenizer = nltk.RegexpTokenizer(reg)
print(tokenizer)

termList = tokenizer.tokenize(stream)
print(termList)
print (" ============== \n Lista de Tokens com RegexpTokenizer \n =================")
for w in termList:
		print(w.lower())

fd.close