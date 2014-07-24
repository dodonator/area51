#coding: utf-8
import os

def listToStr(array):
	result = ''
	for element in array:
		result += element
	return result 

def getMaxOfDict(dictonary,n):
	tmp = 0	

	for element in dictonary:
		if dictonary[element] > tmp:
			tmp = dictonary[element]
	for element in dictonary:
		if dictonary[element] == tmp:
			result = [element,dictonary[element]]
			return result

filename = 'originalText.txt'
# filename = 'test.txt'
textfile = open(filename,'r')
content = textfile.read()
textfile.close()
filename = 'test.txt'

# content = content.replace('\n','')
content = content.replace('ä','ae')
content = content.replace('Ä','Ae')
content = content.replace('ö','oe')
content = content.replace('Ö','Oe')
content = content.replace('ü','ue')
content = content.replace('Ü','ue')
content = content.replace('ß','ss')

n = 5
number = 20
origLen = len(content)

for counter in range(number):
	N = []
	for i in range(len(content)-n):
		tmp = []	
		for i2 in range(n):	
			tmp.append(content[i+i2])	
		N.append(tmp)

	appearNumber = {}

	for element in N:
		if '#' not in element:
			name = listToStr(element)
			appearNumber[name] = N.count(element)

	# for element in appearNumber: print element, appearNumber[element]
	maxEntry = getMaxOfDict(appearNumber,n)
	print maxEntry

	content = content.replace(maxEntry[0],'#' + str(counter))

textfile = open(filename,'w')
textfile.write(content)
textfile.close()

print origLen
print len(content)
print str(number) + ' ' + str(100-float(float(len(content))/float(origLen)*100)) + '%'
