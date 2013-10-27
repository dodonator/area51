import os
os.system('clear')
x = int(raw_input('x      : '))
s = int(raw_input('s      : '))
r = int(raw_input('r      : '))
b = int(raw_input('b (0/1): '))
zahlen1 = range(s,x+s,s)
zahlen2 = range(x,0,-s)
zahlen = [zahlen1,zahlen2]
zeichen = []
for element in zahlen:
	for i in element:
		zeichen.append(i)
#print zeichen
#'''
os.system('clear')
for e in range(r):
	for i in zeichen:
		if b == 0:
			abstand = int((112-i)/2)
		elif b == 1:
			abstand = int(i/2)
		elif b== 2:
			abstand = int(i*2)
		else:
			abstand = int(i*b)
		print abstand*' ' + i*'*' + abstand* ' '
#'''