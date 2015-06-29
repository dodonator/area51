import math

class line(object):

	def __init__(self, tmpName):
		self.name = tmpName
		self.direction_vector = vector3("direction")
		self.stanchion_vector = vector3("stanchion")
		self.factor = 1

	def get_name(self):
		return self.name

	def get_directionVector(self):
		return self.direction_vector

	def set_directionVector(self, tmpVector):
		self.direction_vector = tmpVector

	def get_stanchionVector(self):
		return self.stanchion_vector
	
	def set_stanchionVector(self, tmpVector):
		self.stanchion_vector = tmpVector

	def get_factor(self):
		return self.factor

	def set_factor(self, tmpF):
		self.factor = tmpF

	def iter_factor(self):
		self.factor = self.factor + 1

	def swap_vectors(self):
		tmp = self.direction_vector
		self.direction_vector = self.stanchion_vector
		self.stanchion_vector = tmp

	def main(self, r = self.factor):

		rX = self.stanchion_vector.getXcor() + r * self.direction_vector.getXcor()
		rY = self.stanchion_vector.getYcor() + r * self.direction_vector.getYcor()
		rZ = self.stanchion_vector.getZcor() + r * self.direction_vector.getZcor()
		
		result = vector3("line", rX, rY, rZ)

		return result


class vectorOperations(object):
	def __init__(self, a=vector3("a",0,0,0), b=vector3("b",0,0,0)):
		self.vector_1 = a
		self.vector_2 = b

		self.x1 = self.vector_1.getXcor()
		self.x2 = self.vector_2.getXcor()

		self.y1 = self.vector_1.getYcor()
		self.y2 = self.vector_2.getYcor()
		
		self.z2 = self.vector_1.getZcor()
		self.z2 = self.vector_2.getZcor()


	def addition(self):
		aX = self.x1 + self.x2
		aY = self.y1 + self.y2
		aZ = self.z1 + self.z2

		return vector3("resultA", aX, aY, aZ)


	def multiply(self, r):

		mX1 = self.x1 * m
		mY1 = self.y1 * m
		mz1 = self.z1 * m

		mX2 = self.x2 * m
		mY2 = self.y2 * m
		mZ2 = self.z2 * m

		result_1 = vector3("result_M_1", mX1, mY1, mZ1)
		result_2 = vector3("result_M_2", mX2, mY2, mZ2)

		result = [result_1, result_2]

		return result


	def dot_product(self):
	
		dX = self.x1 * self.x2
		dY = self.y1 * self.y2
		dZ = self.z1 * self.z2

		result = dX + dY + dZ

		return result


	def cross_product(self):

		cX = self.y1 * self.z2 - self.z1 * self.y2
		cY = self.z1 * self.x2 - self.x1 * self.z2
		cZ = self.x1 * self.y2 - self.y1 * self.x2

		result = vector3("result_C", cX, cY, cZ)

		return result

	def rectangle(self):
		return self.cross_product().absolute()

	def triangle(self):
		return float(self.rectangle()) / float(2)


class vector3(object):

	def __init__(self, tmpName, tmpX = 0, tmpY = 0, tmpZ = 0):
		self.xCor = tmpX
		self.yCor = tmpY
		self.zCor = tmpZ

		self.name = tmpName

	############################################################
	
	def setName(self, tmpName):
		self.name = tmpName

	def getName(self):
		return self.name

	############################################################

	def setXcor(self, tmpX):
		self.xCor = tmpX

	def getXcor(self):
		return self.xCor

	############################################################

	def setYcor(self):
		self.yCor = tmpY

	def getYcor(self):
		return self.yCor

	############################################################

	def setZcor(self):
		self.zCor = tmpZ

	def getZcor(self):
		return self.zCor

	############################################################

	def skalar(self):
		sX = self.getXcor * self.getXcor
		sY = self.getYcor * self.getYcor
		sZ = self.getZcor * self.getZcor
		return sX + sY + sZ

	############################################################

	def absolute(self):
		return math.sqrt(self.skalar)

	############################################################

	def negation(self):
		return vector3("result", self.xCor * (-1), self.yCor * (-1), self.zCor * (-1))