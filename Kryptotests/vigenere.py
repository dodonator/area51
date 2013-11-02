
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

def alphabetGenerierung():
		
		alphabet = []
		
		for i in range(26):
			alphabet.append(chr(i+65))
		
		for i in range(26):
			alphabet.append(chr(i+97))
		
		sonderZeichen = sonderzeichen()
		
		for SZeichen in sonderZeichen:
			alphabet.append(SZeichen)
		
		return alphabet

def vigenere(klartext,key):
	alphabet = alphabetGenerierung()
	laengeKlartext = len(klartext)
	laengeKey = len(key)		
	keyArray = list(key)
	keyArray2 = keyArray
	klartextArray = list(klartext)
	geheimtext = ''
	
	if laengeKlartext != laengeKey:
		counter = 0
		while laengeKlartext != laengeKey:
			counter = (counter %  len(keyArray))
			keyArray2.append(keyArray[counter])
			laengeKey = len(keyArray2)
	
	for i in range(laengeKlartext): # Diese for-Schleife kuemmert sich um die Codierung
		tmpKlartextIndex = alphabet.index(klartextArray[i])
		tmpKeyIndex = alphabet.index(keyArray2[i])
		tmpG = alphabet[(tmpKlartextIndex + tmpKeyIndex) % len(alphabet)]
		geheimtext += tmpG

	return geheimtext
klartext = raw_input('Klartext: \n')
key = raw_input('Key: \n')
print vigenere(klartext,key)