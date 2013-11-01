#coding: utf-8
import os
import random
import getpass
import time

os.system('clear')

def keyGenerierung(laengeKlartext):
	keyArray = []
	key = ''
	keyLaenge = 0
	alphabet = ALPHABET()
	for i in range(laengeKlartext):
		tmp = random.choice(alphabet)
		keyArray.append(tmp)
		key += tmp
	keyLaenge = len(keyArray)
	result = [key,keyArray,keyLaenge]
	return result
def sonderzeichen():
	sonderZ1 = range(32,65)
	sonderZ2 = range(91,97)
	sonderZ3 = range(123,126)
	sonderZ = [sonderZ1,sonderZ2,sonderZ3]
	sonderZeichenListe = []
	for element in sonderZ:
		for sonderZeichen in element:
			sonderZeichenListe.append(str(chr(sonderZeichen)))
	return sonderZeichenListe
def ALPHABET():
	Alphabet = []
	for i in range(26):
		Alphabet.append(chr(i+65))
	for i in range(26):
		Alphabet.append(chr(i+97))
	sonderZeichen = sonderzeichen()
	for SZeichen in sonderZeichen:
		Alphabet.append(SZeichen)
	return Alphabet
def encode(klartext):
	'''
	Create a random One-Time-Pad and encode the input strings
	'''
	laengeKlartext = len(klartext)
	keyFoo = keyGenerierung(laengeKlartext)
	key = keyFoo[0]
	keyArray = keyFoo[1]
	klartextArray = list(klartext)
	geheimtextArray = []
	geheimtext = ''
	alphabet = ALPHABET()
	
	for i in range(laengeKlartext): # Diese for-Schleife kuemmert sich um die Codierung
		tmpKlartextIndex = alphabet.index(klartextArray[i])
		tmpKeyIndex = alphabet.index(keyArray[i])
		tmpG = alphabet[(tmpKlartextIndex + tmpKeyIndex) % len(alphabet)]
		geheimtextArray.append(tmpG)

	for element in geheimtextArray: # Diese for-Schleife wandelt den Array in einen String
		geheimtext += element

	return [geheimtext,key]
def decode(geheimtext,key):
	laengeGeheimtext = len(geheimtext)
	keyArray = list(key)
	geheimArray = list(geheimtext)
	klartextArray = []
	klartext = ''
	alphabet = ALPHABET()
	for i in range(laengeGeheimtext):
		tmpGeheimtextIndex = alphabet.index(geheimArray[i])
		tmpKeyIndex = alphabet.index(keyArray[i])
		tmpDifferenz = tmpGeheimtextIndex - tmpKeyIndex
		if tmpDifferenz >= 0:
			klartextArray.append(alphabet[tmpDifferenz])
		else:
			tmpDifferenz = tmpGeheimtextIndex + len(alphabet) - tmpKeyIndex
			klartextArray.append(alphabet[tmpDifferenz])

	for element in klartextArray:
		klartext += element

	return klartext
def analyse(testString,rep):
	trueCounter = 0
	falseCounter = 0
	for i in range(rep):
		tmpEncode = encode(testString)
		tmpGeheimtext = tmpEncode[0]
		tmpKey = tmpEncode[1]
		tmpDecode = decode(tmpGeheimtext,tmpKey)
		if tmpDecode == testString:
			trueCounter += 1
		else:
			falseCounter += 1
	result = [trueCounter,falseCounter]
	return result 
'''
klartext = raw_input(': \n')
rep = int(raw_input(':: \n'))	
'''
'''
result = encode(klartext)
print 'Geheimtext:    ' + result[0]
print 'Key:           ' + result[1]
print 'Enschluesselt: ' + decode(result[0],result[1])
'''
'''
Analyse = analyse(klartext,rep)
print 'True:  ' + str(Analyse[0])
print 'False: ' + str(Analyse[1])
'''
keyL = int(raw_input(':'))
print keyGenerierung(keyL)[0]