import math
import os

systemClear = "cls"

def qs(x):
	if x == 0:
		return 0
	else:
		return int(x % 10 + qs(math.floor(x/10)))

def cut(x):
	products = []
	for i in range(0,int(math.ceil(1000.0/3.0))):
		products.append(i*3)
	xs = str(x)
	lastLen = len(xs)
	while len(xs) >= 3:	
		for element in products:
			if str(element) in xs:
				xs = xs.replace(str(element),"")
				currentLen = len(xs)
				compression = str(lastLen - currentLen)
				com = (len(str(x))+1 - currentLen)*" " + compression + " Ziffern fallen weg."
				print str(element) + (4-len(str(element)))*" " + xs + com
				lastElement = element
				lastLen = currentLen
	print ""
	print "#" * (len(str(x))+26)
	if len(xs) == 0:
		print  str(lastElement) + " % 3 = 0"
		print str(x) + " % 3 = 0"
		print "#" * (len(str(x))+26)
		return 0
	else:
		print xs , "% 3 =" , str(int(xs)%3)
		print str(x) + " % 3 = " + str(int(xs)%3)
		print "#" * (len(str(x))+26)	
		return int(xs) % 3


inp = ""
while inp != "q":
	os.system(systemClear)
	if inp == "q":
		print "Good Bye!"
		break
	inp = raw_input("Bitte Zahl eingeben: \n\n    ")
	cut(int(inp))
	raw_input()
