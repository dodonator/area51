#coding: utf-8
# Momentan in der Entwicklung befindliche Version!
import os
import random
import getpass
import time
import datetime
import sys
import uuid


os.system('clear')
class oneTimePad(object):
	def __init__(self):
		NCF = noCryptoFunctions()
		self.alphabet = NCF.alphabetGenerierung()

	def steganoKrypto(self,klartext,geheimtext):
		'''
		Parameter:
		klartext   (String) -- Der Text, der mit dem Schlüssel verschlüsselt werden soll.
		geheimtext (String) -- Der Text, der als Geheimtext erscheinen soll, und die Existenz
		              einer verschlüsselten Nachricht verschleiern soll.
		
		Rückgabewert:
		key (String) -- Liefert den Key zurück durch den man aus dem eingegebenen Klartext
		                den eingegebenen Geheimtext erstellen kann.

		Diese Funktion hilft zu verschleiern, dass es einen verschlüsselten Text gibt. Allerdings
		schränkt sie die Anzahl der rationalen Schlüssel ein und stellt daher ein potenzielles
		Sicherheitsrisiko dar.
		'''
		klartextArray = list(klartext)
		geheimtextArray = list(geheimtext)
		numKlartextArray = []
		numGeheimtextArray = []
		key = ''
		keyArray = []
		numKeyArray = []

		if len(klartext) != len(geheimtext):
			raise Exception('The code and the plain text must have the same length.')

		for i in range(len(klartext)):
			numKlartextArray.append(self.alphabet.index(klartextArray[i]))
			numGeheimtextArray.append(self.alphabet.index(geheimtextArray[i]))

		for i in range(len(klartext)):
			tmpGStelle = numGeheimtextArray[i]
			tmpKStelle = numKlartextArray[i]
			if tmpGStelle < tmpKStelle:
				tmpGStelle += len(self.alphabet)
			numKeyArray.append(int((tmpGStelle-tmpKStelle)%len(self.alphabet)))

		for i in range(len(klartext)):
			keyArray.append(self.alphabet[numKeyArray[i]])
			key += str(self.alphabet[numKeyArray[i]])
		
		return key

	def keyGenerierung(self,laengeKlartext):
		'''
		Parameter:
		laengeKlartext (Integer) -- Gibt die Länge des zu erstellenden Schlüssels an.

		Rückgabewert:
		result (Array) = [key (String),keyArray (Array), keyLaenge (Integer)]
		key       -- Beinhaltet den erzeugten Schlüssel als String.
		keyArray  -- Beinhaltet den erzeugten Schlüssel als Liste.
		keyLaenge -- Beinhaltet die Länge des erzeugten Schlüssels als Integer.

		'''
		keyArray = []
		key = ''

		for i in range(laengeKlartext):
			tmp = random.choice(self.alphabet)
			keyArray.append(tmp)
			key += tmp

		keyLaenge = len(keyArray)
		result = [key,keyArray,keyLaenge]

		return result

	
	def CodiererMitManuellerKeyEingabe(self,klartext,key):
		'''
		Parameter:
		klartext   (String) -- Text zum codieren
		key        (String) -- Schlüssel, der zum Codieren benötigt wird.

		Rückgabewert:
		geheimtext (String) -- Geheimtext der aus der Codierung ensteht
		'''

		laengeKlartext = len(klartext)
		laengeKey = len(key)		
		keyArray = list(key)
		klartextArray = list(klartext)
		geheimtextArray = []
		geheimtext = ''
		
		if laengeKlartext != laengeKey:
			raise Exception("Error! It's very important that the input and the key have the same length.")
		
		for i in range(laengeKlartext): # Diese for-Schleife kuemmert sich um die Codierung
			tmpKlartextIndex = self.alphabet.index(klartextArray[i])
			tmpKeyIndex = self.alphabet.index(keyArray[i])
			tmpG = self.alphabet[(tmpKlartextIndex + tmpKeyIndex) % len(self.alphabet)]
			geheimtextArray.append(tmpG)
			geheimtext += tmpG

		return geheimtext

	def encode(self,klartext): # Codiert den eingegebenen String
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
		
		for i in range(laengeKlartext): # Diese for-Schleife kuemmert sich um die Codierung
			tmpKlartextIndex = self.alphabet.index(klartextArray[i])
			tmpKeyIndex = self.alphabet.index(keyArray[i])
			tmpG = self.alphabet[(tmpKlartextIndex + tmpKeyIndex) % len(self.alphabet)]
			geheimtextArray.append(tmpG)
			geheimtext += str(tmpG)

		return [geheimtext,key]

	def decode(self,geheimtext,key):
		laengeGeheimtext = len(geheimtext)
		keyArray = list(key)
		geheimArray = list(geheimtext)
		klartextArray = []
		klartext = ''

		for i in range(laengeGeheimtext):
			tmpGeheimtextIndex = self.alphabet.index(geheimArray[i])
			tmpKeyIndex = self.alphabet.index(keyArray[i])
			tmpDifferenz = tmpGeheimtextIndex - tmpKeyIndex
			
			if tmpDifferenz >= 0:
				klartextArray.append(self.alphabet[tmpDifferenz])
				klartext += self.alphabet[tmpDifferenz]
			else:
				tmpDifferenz = tmpGeheimtextIndex + len(self.alphabet) - tmpKeyIndex
				klartextArray.append(self.alphabet[tmpDifferenz])
				klartext += self.alphabet[tmpDifferenz]

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
		
		return [trueCounter,falseCounter]

class noCryptoFunctions(object):
	def __init__(self):
		self.prozessID = uuid.uuid4()

	def kompression(self,Liste):
		resultListe = []
		last = Liste[0]
		
		for i in range(1,len(Liste)):
			resultListe.append(Liste[i]-last)
			last = Liste[i]
		
		return [resultListe,Liste[0]]

	def deKompression(self,compListe):
		start = compListe[1]
		resultListe = [start]
		last = compListe[0][0] + start
		resultListe.append(last)
		Liste = compListe[0]
		
		for i in range(1,len(Liste)):
			resultListe.append(int(last + Liste[i]))
			last = last + Liste[i]
		
		return resultListe

	def datumsStempel(self):
		'''
		Parameter:
		--- Keine ---
		
		Rückgabewert:
		result (Array) = [stempel,counter]
		stempel (String)  -- Ein Datumsstempel mit '-' als Trennzeichen
		counter (Integer) -- Ein Counter für die Minuten, der als ID fungiert.
		'''
		t = time.localtime()
		year = t[0]
		month = t[1]
		day = t[2]
		hour = t[3]
		minute = t[4]
		second = t[5]
		counter = minute + hour*60
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

	def speicherRoutine(self,inhalt,typ,ID):
		currentDirectory = os.getcwd()
		datumsStempel1 = self.datumsStempel()
		foldername = datumsStempel1[0]
		
		if not os.path.exists(os.getcwd()+'/'+foldername):
			os.makedirs(os.getcwd()+'/'+foldername)
		else:
			pass
		
		IDfolder = currentDirectory + '/' + str(foldername)  + '/' + str(ID)
		
		if not os.path.exists(IDfolder):
			os.makedirs(IDfolder)
		else:
			pass
		
		foldername = str(foldername) + '/' + str(ID)
		stempel = str(datumsStempel1[1])
		filename = self.dateiZugriffSpeichern(str(ID),foldername,inhalt,typ)
		
		return ID

	def dateiZugriffLaden(self,filename):
		
		f1 = open(filename,'r')
		result = f1.read()
		f1.close()
		
		return result

	def LadeRoutine(self,ID,typ,year,month,day):
		
		foldername = str(year) + '-' + str(month) + '-' + str(day) + '/' + str(ID)
		currentDirectory = os.getcwd()
		filename = currentDirectory + '/' + foldername + '/' + typ.upper() + '--' + ID + '.' + typ
		result = self.dateiZugriffLaden(filename)
		
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

	def alphabetGenerierung(self):
		
		alphabet = []
		
		for i in range(26):
			alphabet.append(chr(i+65))
		
		for i in range(26):
			alphabet.append(chr(i+97))
		
		sonderZeichen = self.sonderzeichen()
		
		for SZeichen in sonderZeichen:
			alphabet.append(SZeichen)
		
		return alphabet

def RandomDecodierer(): #Random Decode Auswertung
	
	OTP = oneTimePad()
	NCF = noCryptoFunctions()
	alphabet = NCF.alphabetGenerierung()
	rep = int(raw_input('Wiederholungszahl eingeben: \n'))
	klartextLaenge = int(raw_input('Bitte die Länge des Teststrings eingeben: \n'))
	trueCounter = 0
	falseCounter = 0
	
	for i in range(rep):
		key = ''
		geheimtext = ''
	
		for i in range(klartextLaenge):
			key += random.choice(alphabet)
	
		for i in range(klartextLaenge):
			geheimtext += random.choice(alphabet)
	
		klartext = OTP.decode(geheimtext,key)
		print geheimtext
		YN = raw_input('Ergibt der zufällig erzeugte Klartext Sinn (Y/N): \n')
	
		if YN == 'Y' or YN == 'y':
			trueCounter += 1
		elif YN == 'N' or YN == 'n' or YN == '':
			falseCounter += 1
	
		os.system('clear')
	
	print 'Sinn:   ' + str(trueCounter)
	print 'Unsinn: ' + str(falseCounter)

def USE_keyGen(): # Generiert einen Schlüssel
	
	OTP = oneTimePad()
	keyLen = int(raw_input('Keylänge eingeben: \n'))
	result = OTP.keyGenerierung(keyLen)[0]
	print result

def USE_analyse(): # Analysiert die Richtigkeit und verlustfreie Codierung und Decodierung
	
	OTP = oneTimePad()
	klartext = raw_input('Klartext eingeben: \n')
	rep = int(raw_input('Wiederholungszahl eingeben: \n'))
	Analyse = OTP.analyse(klartext,rep)
	print 'True:  ' + str(Analyse[0])
	print 'False: ' + str(Analyse[1])

def CodiererMitSpeicherFunktion(): #Encoding Save Results in Files
	
	OTP = oneTimePad()
	NCF = noCryptoFunctions()
	ID = NCF.prozessID
	klartext = raw_input('Klartext eingeben: \n')
	tmpResult = OTP.encode(klartext)
	geheimtext = tmpResult[0]
	key = tmpResult[1]
	IDg = NCF.speicherRoutine(geheimtext,'g',ID)
	IDk = NCF.speicherRoutine(key,'s',ID)
  	os.system('clear')
	
	if IDg == IDk:
		print'True! ' + str(IDg)
	else:
		print 'False! ' + str(IDg) + ' != ' + str(IDk)

def DecodiererMitLadeFunktion(): # Decoding Parameter will be loaded
	
	OTP = oneTimePad()
	NCF = noCryptoFunctions()
	ID = raw_input('ID: ')
	year = raw_input('Jahr: ')
	month = raw_input('Monat: ')
	day = raw_input('Tag: ')
	geheimtext = NCF.LadeRoutine(ID,'g',year,month,day)
	key = NCF.LadeRoutine(ID,'s',year,month,day)
	result = OTP.decode(geheimtext,key)
	print result

def USE_decode():
	
	OTP = oneTimePad()
	geheimtext = raw_input('Geheimtext eingeben: \n')
	key = raw_input('Key eingeben: \n')
	tmpResult = OTP.decode(geheimtext,key)
	print 'Klartext: '
	print tmpResult

def USE_encode():
	
	OTP = oneTimePad()
	klartext = raw_input('Klartext eingeben: \n')
	tmpResult = OTP.encode(klartext)
	print (12+len(tmpResult[0]))*'#'
	print 'Key:        ' + tmpResult[1]
	print (12+len(tmpResult[0]))*'#'
	print 'Geheimtext: ' + tmpResult[0]
	print (12+len(tmpResult[0]))*'#'

def USE_CodierungMitManuellerKeyEingabe():
	
	OTP = oneTimePad()
	klartext = raw_input('Klartext eingeben: \n')
	key = raw_input('Schlüssel der Länge ' + str(len(klartext)) + ' eingeben: \n')
	os.system('clear')
	print (12 + len(klartext)) * '#'
	print 'Klartext:   ' + klartext
	print 'Schlüssel:  ' + key
	print 'Geheimtext: ' + OTP.CodiererMitManuellerKeyEingabe(klartext,key)
	print (12 + len(klartext)) * '#'

def USE_steganoKrypto():
	
	OTP = oneTimePad()
	klartext = raw_input('Klartext eingeben: ')
	klartextLaenge = len(klartext)
	text = 'Geheimtext der Länge ' + str(klartextLaenge) + ' eingeben: '
	geheimtext = raw_input(text)
	key = OTP.steganoKrypto(klartext,geheimtext)
	print 'Schlüsselwort: ' + key
	print 'Entschlüsselt: ' + OTP.decode(geheimtext,key)


def main():
	
	modus = ''
	
	while modus != 'q':
		os.system('clear')
		print 'Keygenerierung [0]'
		print 'Codieren (Ergebenis wird abgespeichert) [1]'
		print 'Decodieren (Parameter werden ausgelesen) [2]'
		print 'Analyse der Funktionalität [3]'
		print 'Decodierung mit zufälligen Parametern [4]'
		print 'Codierung ohne Key Generierung [5]'
		print 'Steganokryptographie [6]'
		modus = raw_input(': ')
		os.system('clear')
		
		if modus == 'q':
			nachricht = 'Auf Wiedersehen!'
			abstand = int((columns - len(nachricht))/2)*' '
			print 3*'\n'
			print abstand + nachricht + abstand
			print 3*'\n'
			sys.exit()
		
		if modus == '0':
			USE_keyGen()
		elif modus == '1':
			CodiererMitSpeicherFunktion()
		elif modus == '2':
			DecodiererMitLadeFunktion()
		elif modus == '3':
			USE_analyse()
		elif modus == '4':
			RandomDecodierer()
		elif modus == '5':
			USE_CodierungMitManuellerKeyEingabe()
		elif modus == '6':
			USE_steganoKrypto()
		
		warteAufEingabe = raw_input('Bitte zum Fortfahren "Enter" drücken')

columns = 112 # Die Anzahl Zeichen, die auf dem Terminal in eine Zeile passen.

main()