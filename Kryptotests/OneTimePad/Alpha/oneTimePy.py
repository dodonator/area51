import os
import random
import getpass
import time

os.system('clear')

def encode(klartext):
	'''
	Create a random One-Time-Pad and encode the input strings
	'''
	klartext = klartext.upper()
	laengeKlartext = len(klartext)
	key = ''
	keyArray = []
	klartextArray = list(klartext)
	geheimtextArray = []
	geheimtext = ''
	GKArray = []

	for element in klartextArray:
		if ord(element) >= 65 and ord(element) <= 91:
			GKArray.append(True)
		elif ord(element) >= 97 and ord(element) <= 122:
			GKArray.append(False)

	for i in range(laengeKlartext): # Diese for-Schleife generiert den Schluessel
		keyArray.append(str(chr(random.randint(65,91))))
	
	for i in range(laengeKlartext): # Diese for-Schleife kuemmert sich um die Codierung
		tmpG = chr(((ord(klartextArray[i]) + ord(keyArray[i])) % 26) + 65)
		geheimtextArray.append(tmpG)

	for element in geheimtextArray: # Diese for-Schleife wandelt den Array in einen String
		geheimtext += element

	for element in keyArray:
		key += element
	return [geheimtext,key,GKArray]

def decode(geheimtext,key,GKArray):
	geheimtext = geheimtext.upper()
	key = key.upper()
	laengeGeheimtext = len(geheimtext)
	keyArray = list(key)
	geheimArray = list(geheimtext)
	klartextArray = []
	klartext = ''
	Alphabet = [[],[]]

	for i in range(26):
		Alphabet[0].append(chr(65+i))
		Alphabet[1].append(chr(97+i))

	for i in range(laengeGeheimtext):
		tmpDifferenz = ord(geheimArray[i]) - ord(keyArray[i])
		if tmpDifferenz >= 0:
			klartextArray.append(chr(65+tmpDifferenz))
		else:
			tmpDifferenz = ord(geheimArray[i])+26 - ord(keyArray[i])
			klartextArray.append(chr(65+tmpDifferenz))

	for i in range(laengeGeheimtext):
		if GKArray[i] == True:
			klartextArray[i] = Alphabet[0][ord(klartextArray[i])-65]
		elif GKArray[i] == False:
			klartextArray[i] = Alphabet[1][ord(klartextArray[i])-65]

	for element in klartextArray:
		klartext += element

	return klartext



klartext = raw_input(': ')	

result = encode(klartext)
geheimtext = result[0]
key = result[1]
GKArray = result[2]
print result[0]
print decode(result[0],result[1],result[2])
