# coding: utf-8
import random
import os
eingaben = ['Willkommen in der Karibik Schatz','Ich halte das für eine ganz schlechte Idee','Ich habe da ein ganz mieses Gefühl','Ich bin Batman','Du wirst hart trainieren müssen']

chars = []
for i in range(65,91):
	chars.append(chr(i))


def charMixer(eingabe , length):
	tmpResult = []
	result = ''
	while len(tmpResult) <= length:
		word = random.choice(eingabe)
		tmpResult.append(word)
	for res in tmpResult:
		result += res
	return result

def wordMixer(eingabe):
	eingabe = eingabe.lower()
	words = eingabe.split(' ')
	usedWords = []
	result = ''
	while len(words) > len(usedWords):
		word = random.choice(words)
		if word not in usedWords:
			result += word + ' '
			usedWords.append(word)
	return result


os.system('clear')


for ein in eingaben:
	print wordMixer(ein)

'''
codes = []
for i in range(32):
	codes.append(charMixer(chars,25))
	print codes[i]
'''