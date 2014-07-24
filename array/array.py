# 'append', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'

class vector(list):
	
	def __init__(self, *args):
		result = []
		for element in args:
			result.append(element)
		self.v = result


	def get(self):
		return self.v
	

	def add(self, v2):
		result = []
		for i in range(len(self.v)):
			result.append(self.v[i] + v2[i])
		return result


	def skalar(self, x):
		result = []		
		for element in self.v:
			result.append(element*x)
		return result


	def checksum(self):
		result = 0
		for element in self.v:
			result += element
		return result




