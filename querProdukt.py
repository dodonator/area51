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
		result = result * int(ziffer)
	return result

x = 564928
y = querProdukt(x)
z = querSumme(x)
print 'X: ' + str(x)
print ''
print '1. Abstraktionsebene: '
print 'Querprodukt: ' + str(y)
print 'Quersumme: ' + str(z)
print ''
print '2. Abstraktionsebene: '
print 'Quersumme(Querprodukt(x)): ' + str(querSumme(y))
print 'Querprodukt(Quersumme(x)): ' + str(querProdukt(z))
print 'Quersumme(Quersumme(x)): ' + str(querSumme(z))
print 'Querprodukt(Querprodukt(x)): ' + str(querProdukt(y)), y, repr(y)
print ''
