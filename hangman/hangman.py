# coding: utf-8
import random
import os
# ToDo:
# * Fehlerzähler (Hangman) [check]
# * [Ausgeschlossene Buchstaben]
# ** ausgeschlossen, weil falsch
# ** ausgeschlossen, weil richtig
# * Ratebuchstaben
# ** erratene Buchstaben
# ** noch nicht erratene Buchstaben
# * Internes Alphabet
# * Wortliste?
# * Bewertungsalgorithmus für Wörter
# ** Länge des Wortes
# ** Häufigkeit der Buchstaben
# ** Seltenheit der Buchstaben
# * Interne Häufigkeitstabelle
# * 

haeufigkeitsTabellenDateiName = "haeufigkeitstabelleGER.csv"
HTDN = haeufigkeitsTabellenDateiName

def wortEingabeManuell():
	result = raw_input("Bitte geben sie das zu ratende Wort ein: ")	
	result = result.upper()
	os.system("clear")	
	return result

def wortEingabeAuto(filename):
	f1 = open(filename,'r')
	content = f1.read()
	f1.close()
	content.split(';')
	wort = random.choice(wort)
	return wort

def ratenManuell():
	char = raw_input("Raten sie einen Buchstaben: ")
	if len(char) != 1:
		return char[0]
	else:
		return char.upper()

def ratenZufallM():
	alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	result = random.choice(alphabet)
	x = raw_input(":")
	return result

def ratenRelativ():
	f1 = open(HTDN,"r")
	content = f1.read()
	f1.close()

	lines = content.split("\n")
	for i in range(len(lines)):
		lines[i] = lines[i].split(";")

	alphabet = []
	haeufigkeit = []
	indexList = []
	lines.pop()
	for element in lines:
		alphabet.append(element[0])
		haeufigkeit.append(int(element[1]))

	for i in range(len(haeufigkeit)):
		tmp = 0
		for i2 in range(0,i):
			tmp += haeufigkeit[i2]
		indexList.append(tmp)
	
	r = random.randint(0,sum(haeufigkeit))
	
	print r

	for element in indexList:		
		if element > r:
			result = alphabet[indexList.index(element)].upper()
	
	print result
	x = raw_input(":")	
	return result

eingabe = wortEingabeManuell
raten = ratenRelativ

def fehlerStatus(maximum,current):
	if current != maximum:	
				result = "[" + current*"*" + (maximum-current)*" " + "] " + str(current)	
	else:
		result = "You lose"

	print result

def main(wort,maximum = 10):
	wort = wort.upper()	
	wortA = list(wort)
	rate = []
	benutzteBuchstaben = []
	richtigeBuchstaben = []	
	
	for i in range(len(wortA)):
		rate.append("-")

	fehlerCounter = 0
	gewonnen = False

	while fehlerCounter != maximum:
		tmpCounter = 0

		for element in wortA:
			if element in richtigeBuchstaben:
				tmpCounter += 1

		if tmpCounter == len(wortA):
			gewonnen = True
			break

		for element in rate:
			print element ,
		print ''
		print "Benutzte Buchstaben: "

		for element in benutzteBuchstaben:
			print element ,
		print ''
		print "Fehlerzähler: "
		fehlerStatus(maximum,fehlerCounter)

		tmp = raten()
		if tmp not in benutzteBuchstaben:

			if tmp in wortA:

				for i in range(len(wort)):

					if wortA[i] == tmp:
						rate[i] = tmp
				benutzteBuchstaben.append(tmp)
				richtigeBuchstaben.append(tmp)

			else:
				fehlerCounter += 1
				benutzteBuchstaben.append(tmp)
		else:
			fehlerCounter += 1
		os.system("clear")

	if gewonnen:		
		f1 = open("gewonnen.txt","r")
		content = f1.read()
		f1.close()
		print content	

wort = eingabe()
main(wort)

