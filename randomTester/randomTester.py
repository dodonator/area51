import random

def delete(array,ind):
	result = []
	for i in range(len(array)):
		if i != ind:
			result.append(array[i])
		else:
			continue
	return result


def groups(array,l):
	result = []
	for i in range(len(array)-l):
		tmp = []
		for i2 in range(l):
			tmp.append(array[i+i2])
		result.append(tmp)
	return result


def create(l):
	result = []
	array = range(l)
	for i in range(l):
		r = random.randint(0,len(array)-1)
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
		

x = 20
y = 20
l = 2

Result = [] 
Groups = []
Number = []
tmpG = []

for i in range(y):
	Result.append(create(x))

for element in Result:
	tmp = groups(element,l)
	for el in tmp:
		tmpG.append(el)

print tmpG


for element in tmpG:
	name = listToString(element)
	if name not in Groups:
		Groups.append(name)
		Number.append(1)
	elif name in Groups:
		i = Groups.index(name)
		Number[i] += 1
	else:
		raise Exception('Unexpexted Error')

for i in range(len(Groups)):
	print Groups[i],Number[i]
