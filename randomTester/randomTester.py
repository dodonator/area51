import random
import math as crystalMath


func = random.randint

def med(array):
	l = len(array)
	i = l/2
	return array[i]


def avg(array):	
	s = 0
	l = len(array)
	for x in array:
		s += x
	return float(float(s)/float(l))


def delete(array,ind):
	result = []
	for i in range(len(array)):
		if i != ind:
			result.append(array[i])
		else:
			continue
	return result


def groups(array,l): # racism
	result = []
	for i in range(len(array)-l+1):
		tmp = []
		for i2 in range(l):
			tmp.append(array[i+i2])
		result.append(tmp)
	return result


def create(l, func):
	result = []
	array = range(l)
	for i in range(l):
		r = func(0,len(array) - 1)
		result.append(array[r])
		array = delete(array,r)
	return result


def flip(array):
	result = []
	size = len(array[0])
	for i in range(size):
		result.append([])
	for c in range(len(array[0])):
		for r in range(len(array)):
			result[c].append(array[r][c])
	return result


def listToString(array):
	result = ''
	for element in array:
		result += str(element)
		result += ','
	return result
		

x = 25
y = 5000
l = 5

Result = [] 
Groups = []
Number = []
tamponG = []

for i in range(y):
	Result.append(create(x,func))

for element in Result:
	tmp = groups(element,l)
	for el in tmp:
		tamponG.append(el)

for element in tamponG:
	name = listToString(element)
	if name not in Groups:
		Groups.append(name)
		Number.append(1)
	elif name in Groups:
		i = Groups.index(name)
		Number[i] += 1
	else:
		raise Exception('Unexpexted Error')

# for i in range(len(Groups)): print Groups[i],Number[i]

print len(tamponG)
print len(Groups)
print ''
print 'x: ' + str(x)
print 'y: ' + str(y)
print 'l: ' + str(l)
print ''
print 'Max: ' + str(max(Number))
print 'Average: ' + str(crystalMath.avg(Number))
print 'Median: ' + str(med(Number))
print 'Min: ' + str(min(Number))
