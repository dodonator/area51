# coding=utf-8
import time
import os
import random

def printA(a):
	for inhalt in a:
		print inhalt

os.system('clear')
f2 = open('cleverbotLog.txt','r')
file2 = f2.read()
f2.close()
saetze = file2.split('\n')
woerter = ['Ja','Nein','Vielleicht','Blau','Weiß','Rot','Gelb','Grün','Schwarz']
specialWords = ['Ja','Nein','Vielleicht','Blau','Weiß','Rot','Gelb','Grün','Schwarz','Positiv','Negativ','Ich denke schon','Sehr gut','Das ist schlecht']
for i in range(len(saetze)):
	tmpSatz = saetze[i]
	tmpSatz = tmpSatz.split(' ')
	for tmpWort in tmpSatz:
		woerter.append(tmpWort)

# Eingabe

eingabe = ''
while eingabe != '#q':
	#os.system('clear')
	eingabe = raw_input('User:      | ')
	if eingabe == '#q':
		break
	elif eingabe == '#c':
		os.system('clear')
		continue
	saetze.append(eingabe)
	tmpWoerter = eingabe.split(' ')
	for i in range(len(tmpWoerter)):
		woerter.append(tmpWoerter[i])
	r = random.randint(1,100)
	if r <= 60:
		r1 = random.choice(saetze)
		# saetze.append(r1)
		print 'Cleverbot: | ' + r1
	elif r <= 80 and r > 60:
		res = ''
		for i in range(random.randint(5,15)):
			res += random.choice(woerter) + ' '		
		# saetze.append(res)
		print 'Cleverbot: | ' + res
	elif r > 80 and r <= 90:
		r2 = random.choice(woerter)
		print 'Cleverbot: | ' + r2
	elif r <= 93 and r > 90:
		print 'Cleverbot: | Ich beende hiermit diese Konversation!'
		break
	elif r > 93:
		print 'Cleverbot: | ' + random.choice(specialWords)
	tmpWoerter = []
	#time.sleep(3)

os.system('clear')

f1 = open('cleverbotLog.txt','w')
for i in saetze:
	inhalt = f1.write(i + '\n')
f1.close()
print 'Statistik:'
print 20*'#'
print 'Anzahl Saetze:  ' + str(len(saetze))
print 'Anzahl Woerter: ' + str(len(woerter))
print 'Durchschnittliche Anzahl an Wörtern pro Satz: ' + str(len(woerter)/len(saetze))
# Sätze können im cleverbotLog eingetragen werden.
