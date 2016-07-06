# !/usr/bin/env python
# -*- coding: utf-8 -*-




from urllib2 import URLError
from urllib2 import HTTPError
from StringIO import StringIO
import time
import os.path
import urllib2
import gzip


#--------------------Bloco de Variaveis ------------------# 
ArquivoURL = "/Users/nicholas/Desktop/Monitoramento/URL-CPmidias.txt"
ArquivoTargets = "/Users/nicholas/Desktop/Monitoramento/arquivoTargetsCPmidias.txt"
listadeURL = ""
listadeTargets = " "
ID =  " "
nomeApelido =  " "
ListadePalavrasdeBusca =  " "
contadordeURL = 0
cadaPalavra = 0
# ArquivodeERROR  = Arquivo Logs  
arquivo = "ArquivoTemporario.txt"



def pegarTudo():
	with open (arquivo) as variaveldoArquivo:
		return variaveldoArquivo.readlines()


def separarTargensdeTudo(umalinha):

	separadoumaLinha = umalinha.split(";")
	tpID = separadoumaLinha[0]
	tpURL = separadoumaLinha[1]
	tppalavrasChaves = separadoumaLinha[2].split(",")


	return tpID, tpURL, tppalavrasChaves

def conexaoInternet(URL):
	try: 
		request = urllib2.Request(URL)
		response = urllib2.urlopen(request)
		dados = response.read()
		# print dados
	except Exception as e:
	# Precisamos gravar na base os erros, relacionado a Internet 	
		print e 

	return dados 

def procuraPalavraChaves(tpDados,palavrasChave):

	for umaPalavraChave in palavrasChave:
		if tpDados.find(umaPalavraChave) == -1:
			print "Nao encontrado"
		else :
			print "Encontrado"




resultadodePegarTudo = pegarTudo()

for cadaLinha in resultadodePegarTudo:
	
	ident , url, palavrasChave = separarTargensdeTudo(cadaLinha)

	tpDados = conexaoInternet(url)
	print "-------------------------------------------- \n"
	procuraPalavraChaves(tpDados,palavrasChave)



# ------------------- Abrir arquivo de URL --------------------# 
def AbrirURL():
	global listadeURL

	with open(ArquivoURL) as URL:
		listadeURL = URL.readlines()

	return listadeURL

# ------------------- Abrir arquivo de Targets  --------------------# 
def pegarTargets():
	global listadeTargets

	with open(ArquivoTargets)  as Targets:
		listadeTargets = Targets.readlines()

	return listadeTargets

# ------------------- Separar as listas de palavras chaves --------------------# 

def separarTargets(umaLinha):
	global ID,nomeApelido,ListadePalavrasdeBusca

	nomePraDar = umaLinha.split(";")

	ID = nomePraDar[0] # ID de cada Target 
	nomeApelido = nomePraDar[1] # nome ou apelido de cada target 
	ListadePalavrasdeBusca = nomePraDar[2].split(",") # lista de palavra chaves 


# -------------------------- Chama  as funções -------------------------------- #
AbrirURL()
pegarTargets()
separarTargets(listadeTargets[0])

# ------------------------ Comando do bot ------------------------------------# 
while True:
	print listadeTargets[contadordeURL]
	cadaURL = listadeURL[contadordeURL]

	try: 
		request = urllib2.Request(cadaURL)
		response = urllib2.urlopen(request)
		dados = response.read()
		# print dados
	except Exception as e:
	# Precisamos gravar na base os erros, relacionado a Internet 	
		print e 
		continue 


	print cadaURL
	while True:

		busca = dados.find(ListadePalavrasdeBusca[cadaPalavra])

		if busca == -1:
			print 'Não encontrado'
			# dentro deste bloco devemos tomar uma ação monitoramento/ corretiva. 


		print ListadePalavrasdeBusca[cadaPalavra]
		print busca

		
		if cadaPalavra == len(ListadePalavrasdeBusca) -1:
			cadaPalavra = 0 
			print "Fim de Palavras"
			break
			

		cadaPalavra += 1



	contadordeURL += 1

	if contadordeURL != 5:
		separarTargets(listadeTargets[contadordeURL])
	else :
		print "aguardando"
		break
		# time.sleep(5)
		# contadordeURL = 0 
		# continue


