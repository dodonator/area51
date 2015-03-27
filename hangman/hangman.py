# coding: utf-8
import random
import os
# ToDo:
# * Fehlerzähler (Hangman)
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
wortListenDateiName = "wortliste.txt"
WLDN = wortListenDateiName

# Eingabefunktionen:

def wortEingabeManuell():
	result = raw_input("Bitte geben sie das zu ratende Wort ein: ")	
	result = result.upper()
	os.system("clear")	
	return result

def wortEingabeAuto():
	filename = WLDN
	f1 = open(filename,'r')
	content = f1.read().upper()
	f1.close()
	content = content.split('\n')
	content.pop()
	wort = random.choice(content)
	return wort

# Ratefunktionen:
	
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

	for (index, element) in enumerate(indexList):		
		if element > r:
			result = alphabet[index].upper()			
			break
	
	x = raw_input(":")
	
	return result

# Hier können die Funktionen eingegeben werden, die
# benutzt werden sollen:
eingabe = wortEingabeAuto
raten = ratenManuell

def woerterHinzufuegen(wort,av = False):
	filename = WLDN
	f1 = open(filename,"r")
	content = f1.read().upper()
	f1.close()
	content = content.split("\n")
	
	if av:
		scores = {}
		for element in content:
			scores[element] = bewertung(element,True)
		
		b = bewertung(wort,True)
		
		durchschnitt = 0
		summe = 0
		counter = 0
		for element in scores:
			summe += scores[element]
			counter += 1
		durchschnitt = float(summe)/float(counter)
		
		if b <= durchschnitt:
			result = "\n" + wort
		else:
			result = ''
	else:
		result = "\n" + wort
	
	f1 = open(filename,"a")
	f1.write(result)
	f1.close()

def bewertung(wort,relScore=False):
	
	wort = wort.upper()
	
	f1 = open(HTDN,"r")
	ht = f1.read().upper()
	f1.close()
	
	lines = ht.split("\n")
	lines.pop()
	
	ht = {}
	for i in range(len(lines)):
		tmp = lines[i].split(";")
		ht[tmp[0]] = int(tmp[1])
	
	# ht ist nun eine Häufigkeitstabelle
	
	# Wiederholungen von Buchstaben:
	w = 1
	chars = []
	for tmp in wort:
		if tmp in chars:
			w += 1
		else:
			chars.append(tmp)
	# Länge eines Wortes:
	l = len(wort)
	
	# Seltenheit der Buchstaben:
	s = 0
	for char in wort:
		s += ht[char]
	
	print "w: " + str(w)
	print "s: " + str(s)
	print "l: " + str(l)
	
	# Scoring:
	if relScore:
		result = float(s+w)/float(l)
	else:
		result = 2000 - (s + w + l)
	
	print "r: " + str(result)
	
	return result
	
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
	
	woerterHinzufuegen(wort.upper(),True)

# wort = eingabe()
# print wort
# main(wort)
# bewertung(raw_input(":"),True)
x = raw_input("")
