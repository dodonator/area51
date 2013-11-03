import itertools
def cartesian(stellen,array2):
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