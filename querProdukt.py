import os
import random

os.system('clear')
def zifferCounter(zahl):
	result = []
	for i in range(10):
		result.append([0])
	for ziffer in str(zahl):
		result[int(ziffer)] += ziffer
	for i in range(10):
		result[i] = len(result[i])-1
	return result

def querSumme(zahl):
	zahl = str(zahl)
	result = 0
	for ziffer in zahl:
		result = result + int(ziffer)
	return result

def querProdukt(zahl):
	zahl = str(zahl)
	result = 1
	for ziffer in zahl:
		if ziffer != '0':
			result = result * int(ziffer)
		else:
			pass
	return result
'''
inp = int(raw_input(':'))
inp = xrange(inp)
x = ''
for i in inp:
	x = str(x) + str(i)
x = int(x)
'''
x = int(raw_input(':'))
y = querProdukt(x)
z = querSumme(x)
'''
print 'X: ' + str(x)
print ''
counter = 0
for element in zifferCounter(x):
	print str(counter) + ': ' + str(element)
	counter += 1
print ''
print '1. Abstraktionsebene: '
print 'Querprodukt: ' + str(y)
print 'Quersumme: ' + str(z)
print ''
print '2. Abstraktionsebene: '
print 'Quersumme(Querprodukt(x)): ' + str(querSumme(y))
print 'Querprodukt(Quersumme(x)): ' + str(querProdukt(z))
print 'Quersumme(Quersumme(x)): ' + str(querSumme(z))
print 'Querprodukt(Querprodukt(x)): ' + str(querProdukt(y))
print ''
'''
# querprodukt = lambda z: reduce(lamda x,y: int(x)*int(y), list(str(z)))

def querSummeRek(zahl):
	counter = 0
	zahl = str(zahl)
	result = 0
	for ziffer in zahl:
		result = result + int(ziffer)
	counter += 1
	if len(str(result)) != 1:
		return querSummeRek(result)
	return result
print querSummeRek(x)

def querProduktRek(zahl):
	zahl = str(zahl)
	result = 1
	for ziffer in zahl:
		if ziffer != '0':
			result = result * int(ziffer)
		else:
			pass
	if len(str(result)) != 1:
		return querProduktRek(result)
	return result
# print querProduktRek(x)