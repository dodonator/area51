plaintext = raw_input('Geheimtext eingeben: \n')
shift = int(raw_input('Verschiebung eingeben: \n'))%26

def caesar(plaintext, shift):
	result = ''

	alphaUP = []
	alphaLOW = []
	for i in range(26):
		alphaUP.append(chr(i+65))
		alphaLOW.append(chr(i+97))

	for char in plaintext:
		if char.upper() == char:
			tmp = alphaUP.index(char)
			result += alphaUP[(tmp+shift)%26]

		elif char.lower() == char:
			tmp = alphaLOW.index(char)
			result += alphaLOW[(tmp+shift)%26]
	return result

def caesar2(plaintext, shift):
	printableChars = []
	result = ''
	for i in range(32,123):
		printableChars.append(chr(i))
	for char in plaintext:
		tmp = printableChars.index(char)
		result += printableChars[(tmp+shift) % len(printableChars)]
	return result

def analyse(secret):
	for i in range(26):
		print caesar(secret,i)

print caesar(plaintext,shift)


