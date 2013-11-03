import math
import itertools
import os
os.system('clear')

def QP(zahl):
	result = 1
	zahl = str(zahl)
	zahl = list(zahl)
	for ziffer in zahl:
		ziffer = int(ziffer)
		if ziffer != 0:
			result = result * ziffer
		else:
			continue
	return result

def QS(zahl):
	result = 0
	zahl = str(zahl)
	zahl = list(zahl)
	for ziffer in zahl:
		ziffer = int(ziffer)
		result += ziffer
	return result

def T(zahl):
	teiler = []
	wurzel = int(math.sqrt(zahl))
	for i in range(1,wurzel+1):
		if (zahl % i) == 0:
			if i != (zahl/i):
				teiler.append(i)
				teiler.append(zahl/i)
			else:
				teiler.append(i)
	teiler.sort()
	return teiler

def R(x,y,z):
	return range(x,y+1,z)

def SA(zahl):
	return len(str(zahl))

def C(stellen,array2):
	array1 = range(stellen)
	zahlen = []
	result = []
	for zahl in array1:
		zahlen.append(array2)

	for l in itertools.product(*zahlen):
	    tmpResult = ''.join(str(l))
	    tmpResult = tmpResult.replace('(','')
	    tmpResult = tmpResult.replace(')','')
	    tmpResult = tmpResult.replace(',','')
	    tmpResult = tmpResult.replace(' ','')
	    result.append(tmpResult)
	return result

def I(testElement,testArray):
	return testElement in testArray

def PA(array):
	for element in array:
		print element ,

def mainDodo(zahl):
	werte = {}
	werte['QS(x)'] = QS(zahl)
	werte['QP(x)'] = QP(zahl)
	werte['SA(x)'] = SA(zahl)
	werte['T(QP(x))'] = T(werte['QP(x)'])
	werte['SU(QS(x))'] = range(werte['QS(x)'])
	werte['s1'] = []
	for element in werte['SU(QS(x))']:
		if I(element,werte['T(QP(x))']):
			werte['s1'].append(element)
	werte['s2'] = C(werte['SA(x)'],werte['s1'])
	werte['s3QS'] = []
	werte['s3QP'] = []
	for element in werte['s2']:
		if QS(element) == werte['QS(x)'] and len(str(element)) == werte['SA(x)']:
			werte['s3QS'].append(element)
	for element in werte['s2']:
		if QP(element) == werte['QP(x)'] and len(str(element)) == werte['SA(x)']:
			werte['s3QP'].append(element)
	werte['s4'] = []
	for element in werte['s3QS']:
		if I(element,werte['s3QP']):
			werte['s4'].append(element)
	return werte['s4']

x = int(raw_input('Bitte Zahl eingeben: \n'))
r = mainDodo(x)
PA(r)
print '\n' + str(len(r))




