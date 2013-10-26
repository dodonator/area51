#coding: utf-8
import os
import random
import getpass
import time

os.system('clear')
class oneTimePad(object):

	def keyGenerierung(self,laengeKlartext):
		NCF = noCryptoFunctions()
		keyArray = []
		key = ''
		keyLaenge = 0
		alphabet = NCF.ALPHABET()
		for i in range(laengeKlartext):
			tmp = random.choice(alphabet)
			keyArray.append(tmp)
			key += tmp
		keyLaenge = len(keyArray)
		result = [key,keyArray,keyLaenge]
		return result

	

	def encode(self,klartext):
		'''
		Create a random One-Time-Pad and encode the input strings
		'''
		NCF = noCryptoFunctions()
		laengeKlartext = len(klartext)
		keyFoo = self.keyGenerierung(laengeKlartext)
		key = keyFoo[0]
		keyArray = keyFoo[1]
		klartextArray = list(klartext)
		geheimtextArray = []
		geheimtext = ''
		alphabet = NCF.ALPHABET()
		
		for i in range(laengeKlartext): # Diese for-Schleife kuemmert sich um die Codierung
			tmpKlartextIndex = alphabet.index(klartextArray[i])
			tmpKeyIndex = alphabet.index(keyArray[i])
			tmpG = alphabet[(tmpKlartextIndex + tmpKeyIndex) % len(alphabet)]
			geheimtextArray.append(tmpG)

		for element in geheimtextArray: # Diese for-Schleife wandelt den Array in einen String
			geheimtext += element

		return [geheimtext,key]

	def decode(self,geheimtext,key):
		NCF = noCryptoFunctions()
		laengeGeheimtext = len(geheimtext)
		keyArray = list(key)
		geheimArray = list(geheimtext)
		klartextArray = []
		klartext = ''
		alphabet = NCF.ALPHABET()
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

class noCryptoFunctions(object):

	def datumsStempel(self):
		t = time.localtime()
		year = t[0]
		month = t[1]
		day = t[2]
		hour = t[3]
		minute = t[4]
		second = t[5]
		counter = second + (minute*60) + (hour*3600)
		stempel = str(year) + '-' + str(month) + '-' + str(day)
		return [stempel,counter]

	def dateiZugriffSpeichern(self,filename,foldername,inhalt,typ):
		'''
		filename: 'filename'
		inhalt: sagdajs
		typ: 'g' für Geheimtext, 'k' für klartext oder 's' für Schlüssel
		'''
		currentDirectory = os.getcwd()
		filename = currentDirectory + '/' + foldername + '/' + typ.upper() + '--' + filename + '.' + typ
		command = 'sudo touch ' + filename
		os.system(command)
		f1 = open(filename,'w')
		file1 = f1.write(inhalt)
		f1.close()
		return filename

	def speicherRoutine(self,inhalt,typ):
		currentDirectory = os.getcwd()
		datumsStempel1 = self.datumsStempel()
		foldername = str(datumsStempel1[0])
		ID = datumsStempel1[1]
		if foldername not in os.listdir(os.getcwd()):
			os.system('mkdir ' + foldername)
		else:
			pass
		IDfolder = 'mkdir ' + currentDirectory + '/' + str(foldername)  + '/' + str(ID)
		if IDfolder not in os.listdir(os.getcwd() + '/' + str(foldername)):
			os.system(IDfolder)
		else:
			pass
		foldername = str(foldername) + '/' + str(ID)
		stempel = str(datumsStempel1[1])
		filename = self.dateiZugriffSpeichern(stempel,foldername,inhalt,typ)
		return filename

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

NCF = noCryptoFunctions()
OTP = oneTimePad()
chiffre = OTP.encode('Hunde')
geheimtext = chiffre[0]
key = chiffre[1]
NCF.speicherRoutine(geheimtext,'g')
NCF.speicherRoutine(key,'s')