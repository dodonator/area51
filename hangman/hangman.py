# coding: utf-8
import random
import os
# ToDO:
# ratenRelativ richtig machen
# configurationsdatei einbinden
# Dokumentation!
# Windowskompatibilität
# Wortlistensäuberung
# Warum funktioniert das Eingeben von WÖrtern nicht?
# Themenspezifische Wortlisten (pokemon, personen und ähnliches)
# und vieles mehr...

haeufigkeitsTabellenDateiName = "haeufigkeitstabelleGER.csv"
HTDN = haeufigkeitsTabellenDateiName
wortListenDateiName = "wortliste.txt"
WLDN = wortListenDateiName

# Eingabefunktionen:

def wortEingabeManuell():
	result = raw_input("Bitte geben sie das zu ratende Wort ein: ")	
	result = result.upper().strip()
	os.system("cls") # Windows
	# os.system("clear") # Unix
	return result
	
def wortEingabeAuto():
	filename = WLDN
	f1 = open(filename,'r')
	content = f1.read().upper()
	f1.close()
	content = content.split('\n').strip()
	content.pop()
	wort = random.choice(content)
	return wort

# Ratefunktionen:
	
def ratenManuell():
	wort = raw_input("Raten sie einen Buchstaben: ")
	return wort.upper()

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
eingabe = wortEingabeManuell
raten = ratenManuell

def woerterHinzufuegen(wort,av = False):
	result = av
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
		
		if b <= durchschnitt and wort not in content:
			con = "\n" + wort
			result = True
		else:
			con = ''
			result = False
	else:
		con = "\n" + wort
		result = False
	
	f1 = open(filename,"a")
	f1.write(con)
	f1.close()
	
	return result

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
	
	# print "w: " + str(w)
	# print "s: " + str(s)
	# print "l: " + str(l)
	
	# Scoring:
	if relScore:
		result = float(s+w)/float(l)
	else:
		result = 2000 - (s + w + l)
	
	# print "r: " + str(result)
	
	return result
	
def fehlerStatus(maximum,current):

	if current != maximum:	
				result = "[" + current*"*" + (maximum-current)*" " + "] " + str(current)	
	else:
		result = "You lose"

	print result
		
def main(wort,maximum = 10, av = False):
	wort = wort.upper()	
	wortA = list(wort)
	rate = []
	benutzteBuchstaben = []
	benutzteWorte = []
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
		print '\n'
		
		print "Benutzte Buchstaben: "
		for element in benutzteBuchstaben:
			print element ,
		print '\n'
		
		print "Benutzte Wörter: "
		for element in benutzteWorte:
			print element + ' ' ,
		print '\n'
		
		print "Fehlerzähler: "
		fehlerStatus(maximum,fehlerCounter)
		print '\n'

		tmp = raten()
		if len(tmp) == 1:		
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
		elif len(tmp) == len(wort):
			if tmp == wort:
				gewonnen = True
			else:
				benutzteWorte.append(tmp)
				break
		else:
			fehlerCounter += 1
			
		os.system("cls") # Windows
		# os.system("clear") # Unix
		
	if gewonnen:
		print "Das Wort war: " + wort
		f1 = open("gewonnen.txt","r")
		content = f1.read()
		f1.close()
		print content
	
	tmp = woerterHinzufuegen(wort.upper(),av)
	if eingabe == wortEingabeManuell and tmp:
		print "Das eingegebene Wort war so gut, "
		print "dass es in die Wortliste aufgenom-"
		print "men wurde."

x = ""
while x != "q":
	# os.system("clear") # Unix
	os.system("cls") # Windows
	if x != "q":
		wort = eingabe()
		main(wort,10,True)
		x = raw_input("Drücken sie 'q' zum verlassen: ")
		r = random.randint(0,10)
		if r < 6:
			eingabe = wortEingabeAuto
		else:
			eingabe = wortEingabeManuell
	else:
		break
	
	
	
