import os
os.system('clear')
class krypto(object):
	def __init__(self, klartext,key):
		if len(key) < len(klartext):
			key += key
			if len(key) > len(klartext):
				while len(key) > len(klartext):
					klartext += 'X'
			if len(key) < len(klartext):
				while len(key) < len(klartext):
					key += 'Y'
		if len(klartext) % 2 != 0:
			klartext += 'X'
			self.Ungerade = True
		else:
			self.Ungerade = False
		if len(key) % 2 != 0:
			key += 'Y'

		self.key = key.upper()
		self.klartext = klartext.upper()
		self.laenge = len(self.klartext)

	
	def TrenneKlartext(self):
		self.result1 = []
		tmpKlartext = list(self.klartext)
		i = 0
		while i != (self.laenge):
			self.result1.append(str(tmpKlartext[i] + tmpKlartext[i+1]))
			i = i + 2
		return self.result1

	def DefinitionsBereich(self):
		self.definitionB = []
		ziffern = range(10)
		alphabet = []
		for i in range(65,91):
			alphabet.append(chr(i))
		alphabet2 = alphabet
		for element in alphabet:
			for element2 in alphabet2:
				self.definitionB.append(str(element + element2))
		for ziffer in ziffern:
			self.definitionB.append(ziffer)
		return self.definitionB

	def KlartextKompression(self):
		result2 = []
		tmpTestString = ''
		for element2 in self.definitionB:
			tmpTestString += str(element2)
		for element in self.result1:
			result2.append(tmpTestString.find(element))
		self.result2 = result2
		return self.result2

	def TrenneKey(self):
		self.result3 = []
		tmpKey = list(self.key)
		i = 0
		while i < len(tmpKey)-1:
			self.result3.append(str(tmpKey[i] + tmpKey[i+1]))
			i = i + 2
		return self.result3

	def KeyKompression(self):
		result4 = []
		tmpTestString = ''
		for element2 in self.definitionB:
			tmpTestString += str(element2)
		for element in self.result3:
			result4.append(tmpTestString.find(element))
		self.result4 = result4
		return self.result4	

	def CodierenStep1(self):
		result5 = []	
		for i in range(len(self.result2)):
			result5.append(int(self.result2[i] + self.result4[i]))
		self.result5 = result5
		return self.result5
	def Hexadezimalumrechner(self,zahl):
		result = []
		r1 = zahl % 256
		result.append(str((zahl-r1)/256))
		if r1 == 1:
			result.append(str(1))
			return result
		elif r1 == 0:
			return result
		else:
			r2 = r1 % 16
			result.append(str((r1-r2)/16))
			if r2 == 1:
				result.append(str(1))
				return result
			elif r2 == 0:
				return result
			else:
				r3 = r2 % 1
				result.append(str((r2-r3)/1))
				return result
	def Converter(self,zahl):
		result = self.Hexadezimalumrechner(zahl)
		for i in range(len(result)):
			if result[i] == '10':
				result[i] = 'A'
			elif result[i] == '11':
				result[i] = 'B'
			elif result[i] == '12':
				result[i] = 'C'
			elif result[i] == '13':
				result[i] = 'D'
			elif result[i] == '14':
				result[i] = 'E'
			elif result[i] == '15':
				result[i] = 'F'
		Result = ''
		for element in result:
			Result += str(element)
		return Result

	def CodierenStep2(self):
		result = ''
		result6 = []
		for element in self.result5:
			result6.append(self.Converter(element))
		for element in result6:
			result += element + ' '
		self.result6 = result
		return  result

	def main(self):
		k.TrenneKlartext()
		k.DefinitionsBereich()
		k.KlartextKompression()
		k.TrenneKey()
		k.KeyKompression()
		k.CodierenStep1()
		k.CodierenStep2()
		return self.result6

klartext = raw_input('Klartext: \n')
key = raw_input('Key: \n')
k = krypto(klartext,key)
print k.main()

