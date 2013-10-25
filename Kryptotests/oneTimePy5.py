#coding: utf-8
import os
import random
import getpass
import time

os.system('clear')
class oneTimePad(object):

	def keyGenerierung(self,laengeKlartext):
		keyArray = []
		key = ''
		keyLaenge = 0
		alphabet = self.ALPHABET()
		for i in range(laengeKlartext):
			tmp = random.choice(alphabet)
			keyArray.append(tmp)
			key += tmp
		keyLaenge = len(keyArray)
		result = [key,keyArray,keyLaenge]
		return result
	def sonderzeichen(self):
		sonderZ1 = range(32,65)
		sonderZ2 = range(91,97)
		sonderZ3 = range(123,126)
		sonderZ = [sonderZ1,sonderZ2,sonderZ3]
		sonderZeichenListe = []
		for element in sonderZ:
			for sonderZeichen in element:
				sonderZeichenListe.append(str(chr(sonderZeichen)))
		return sonderZeichenListe
	def ALPHABET(self):
		Alphabet = []
		for i in range(26):
			Alphabet.append(chr(i+65))
		for i in range(26):
			Alphabet.append(chr(i+97))
		sonderZeichen = self.sonderzeichen()
		for SZeichen in sonderZeichen:
			Alphabet.append(SZeichen)
		return Alphabet
	def encode(self,klartext):
		'''
		Create a random One-Time-Pad and encode the input strings
		'''
		laengeKlartext = len(klartext)
		keyFoo = self.keyGenerierung(laengeKlartext)
		key = keyFoo[0]
		keyArray = keyFoo[1]
		klartextArray = list(klartext)
		geheimtextArray = []
		geheimtext = ''
		alphabet = self.ALPHABET()
		
		for i in range(laengeKlartext): # Diese for-Schleife kuemmert sich um die Codierung
			tmpKlartextIndex = alphabet.index(klartextArray[i])
			tmpKeyIndex = alphabet.index(keyArray[i])
			tmpG = alphabet[(tmpKlartextIndex + tmpKeyIndex) % len(alphabet)]
			geheimtextArray.append(tmpG)

		for element in geheimtextArray: # Diese for-Schleife wandelt den Array in einen String
			geheimtext += element

		return [geheimtext,key]
	def decode(self,geheimtext,key):
		laengeGeheimtext = len(geheimtext)
		keyArray = list(key)
		geheimArray = list(geheimtext)
		klartextArray = []
		klartext = ''
		alphabet = self.ALPHABET()
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
	def analyse(self,testString,rep):
		OTP = oneTimePad()
		trueCounter = 0
		falseCounter = 0
		for i in range(rep):
			tmpEncode = OTP.encode(testString)
			tmpGeheimtext = tmpEncode[0]
			tmpKey = tmpEncode[1]
			tmpDecode = OTP.decode(tmpGeheimtext,tmpKey)
			if tmpDecode == testString:
				trueCounter += 1
			else:
				falseCounter += 1
		result = [trueCounter,falseCounter]
		return result 

def keyGen():
	OTP = oneTimePad()
	keyLen = int(raw_input('Keylänge eingeben: \n'))
	result = OTP.keyGenerierung(keyLen)[0]
	print result

def analyse():
	OTP = oneTimePad()
	klartext = raw_input('Klartext eingeben: \n')
	rep = int(raw_input('Wiederholungszahl eingeben: \n'))
	Analyse = OTP.analyse(klartext,rep)
	print 'True:  ' + str(Analyse[0])
	print 'False: ' + str(Analyse[1])

def encoden():
	OTP = oneTimePad()
	klartext = raw_input('Klartext eingeben: \n')
	tmpResult = OTP.encode(klartext)
	print (12+len(tmpResult[0]))*'#'
	print 'Key:        ' + tmpResult[1]
	print (12+len(tmpResult[0]))*'#'
	print 'Geheimtext: ' + tmpResult[0]
	print (12+len(tmpResult[0]))*'#'

def decoden():
	OTP = oneTimePad()
	geheimtext = raw_input('Geheimtext eingeben: \n')
	key = raw_input('Key eingeben: \n')
	tmpResult = OTP.decode(geheimtext,key)
	print 'Klartext: '
	print tmpResult

# keyGen()
# encoden()
# decoden()
# analyse()