import random
import os
alphabet = []

zeichenOrd = range(65,91)
for i in zeichenOrd:
	alphabet.append(str(chr(i)))
rep = int(raw_input('Wiederholungen: \n'))
for n in range(rep):
	gesString =''
	for i in range(30):
		laenge = 40
		tmpString = ''
		for i in range(laenge):
			tmpString += random.choice(alphabet) + ' '
		print tmpString
		gesString += tmpString + '\n'
	curDir = os.getcwd()
	if 'buchstabenSalat.txt' not in os.listdir(curDir):
		os.system('touch buchstabenSalat' + str(n) + '.txt')
	f = open('buchstabenSalat' + str(n) + '.txt','w')
	file1 = f.write(gesString)
	f.close()


