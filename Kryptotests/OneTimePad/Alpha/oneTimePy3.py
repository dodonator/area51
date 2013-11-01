#coding: utf-8
import os
import random
import getpass
import time

os.system('clear')


def sonderzeichen():
	sonderZ1 = range(32,65)
	sonderZ2 = range(91,97)
	sonderZ3 = range(123,126)
	sonderZ = [sonderZ1,sonderZ2,sonderZ3]
	sonderZeichenListe = []
	for element in sonderZ:
		for sonderZeichen in element:
			sonderZeichenListe.append(chr(sonderZeichen))
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
	key = ''
	keyArray = []
	klartextArray = list(klartext)
	geheimtextArray = []
	geheimtext = ''
	alphabet = ALPHABET()

	for i in range(laengeKlartext): # Diese for-Schleife generiert den Schluessel
		keyArray.append(random.choice(alphabet))
	
	for i in range(laengeKlartext): # Diese for-Schleife kuemmert sich um die Codierung
		tmpKlartextIndex = alphabet.index(klartextArray[i])
		tmpKeyIndex = alphabet.index(keyArray[i])
		tmpG = alphabet[(tmpKlartextIndex + tmpKeyIndex) % len(alphabet)]
		geheimtextArray.append(tmpG)

	for element in geheimtextArray: # Diese for-Schleife wandelt den Array in einen String
		geheimtext += element

	for element in keyArray:
		key += element

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



klartext = raw_input(': \n')	
result = encode(klartext)
print 'Geheimtext:    ' + result[0]
print 'Key:           ' + result[1]
print 'Enschluesselt: ' + decode(result[0],result[1])
