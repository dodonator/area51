#coding: utf-8

import math
def primRechner1(endwert):
	startwert = 5

	primzahlen = [2,3]
	prim = False

	for zahl in xrange(startwert,endwert,2):
		for primzahl in primzahlen:
			if zahl % primzahl == 0:
				prim = False
				break
			else:
				prim = True
		if prim:
			primzahlen.append(zahl)

	return primzahlen

def primPruefer1(testPrim):
	wurzel = math.sqrt(testPrim)
	if wurzel == int(wurzel):
		return False
	for i in xrange(2,int(wurzel)):
		if testPrim % i == 0:
			return False
	return True

def primZaehler(generator,menge):
	result = len(generator(menge))
	return result
	
def listenPruefer(pruefer,generator,menge):
	testListe = generator(menge)
	ergebnisListe = []
	ergebnis = True
	for element in testListe:
		tmp = pruefer(element)
		if tmp == False:
			ergebnis = False
		ergebnisListe.append(tmp)
	return [ergebnis,ergebnisListe]

def ausgabe(liste):
	pass
	
print primZaehler(primRechner1,1000)	

# print listenPruefer(primPruefer1,primRechner1,10000)[0]

