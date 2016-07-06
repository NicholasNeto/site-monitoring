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
 
arquivo = "/Users/nicholas/Desktop/Monitoramento/ArquivoTemporario.txt"


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

def procuraPalavraChaves(ident,tpDados,palavrasChave):

	for umaPalavraChave in palavrasChave:
		if tpDados.find(umaPalavraChave) == -1:
			print "Nao encontrado - " + umaPalavraChave + " em " + ident
		else :
			print "Encontrado - " + umaPalavraChave + " em " + ident




resultadodePegarTudo = pegarTudo()

for cadaLinha in resultadodePegarTudo:
	
	ident , url, palavrasChave = separarTargensdeTudo(cadaLinha)

	tpDados = conexaoInternet(url)
	print "-------------------------------------------- \n"
	procuraPalavraChaves(ident,tpDados,palavrasChave)