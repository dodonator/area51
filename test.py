def Hexadezimalumrechner(zahl):
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
def Converter(zahl):
	result = Hexadezimalumrechner(zahl)
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
print Converter(1001)


