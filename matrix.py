import random
alphabet = []
zeichenOrd = range(65,91)
for i in zeichenOrd:
	alphabet.append(str(chr(i)))
'''
rep = int(raw_input('Wiederholungen: \n'))
for i in range(rep):
'''
while True:	
	laenge = 111
	tmpString = ''
	for i in range(laenge):
		tmpString += random.choice(alphabet)
	print tmpString
