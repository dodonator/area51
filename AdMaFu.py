#coding: utf-8
import math
import random
import os
class polynome(object):
	
	def polynom_1(self,x,a,b):
		'''
		p(x) = a*x+b
		'''
		p = a*x+b
		term = 'p(x) = a*x+b'
		return p

	def polynom_2(self,a,b,c,x):
		'''
		p(x) = a * x^2 + b * x + c
		'''
		p = a * x^2 + b * x + c
		term = 'p(x) = a * x^2 + b * x + c'
		return p

	def polynom_3(self,a,b,c,d,x):
		'''
		p(x) = a * x^3 + b * x^2 + c * x + d
		'''
		term = 'p(x) = a * x^3 + b * x^2 + c * x + d'
		p = a * x^3 + b * x^2 + c * x + d
		return p

	def polynom_n(self,x,n,faktoren):
		'''
		p(x) = a * x^n + b*x^(n-1) + c*x^(n-2) ... z*x + A
		faktoren must be an array of integer with the length n
		'''
		p = 0
		exponenten = range(n,0,-1)
		for i in range(n):
			p += faktoren[i] * pow(x,exponenten[i])
		return p

	def create_Faktoren(self,n):
		faktoren = []
		for i in range(n):
			faktoren.append(int(raw_input('Faktor ' + str(i+1) + ': ')))
		return faktoren


class modulo(object):
	
	def modulo_10(self,x):
		return x%10

	def modulo_100(self,x):
		return x%100

	def modulo_1000(self,x):
		return x%1000

	def modulo_10_pot_n(self,x,n):
		return x%pow(10,n)

	def modulo_2(self,x):
		return x%2

	def modulo_8(self,x):
		return x%8

	def modulo_16(self,x):
		return x%16

	def modulo_2_pot_n(self,x,n):
		return x%pow(2,n)

	def modulo_26(self,x):
		return x%26

	def modulo_n(self,x,n):
		return x%n


class queroperatoren(object):

	def quersumme(self,x):
		summe = 0
		ziffernarray = list(str(x))
		for ziffer in ziffernarray:
			summe += int(ziffer)
		return summe

	def querprodukt_ignore_0(self,x):
		produkt = 1
		for ziffer in list(str(x)):
			if ziffer != 0:
				produkt *= int(ziffer)
		return produkt

	def querprodukt(self,x):
		produkt = 1
		for ziffer in list(str(x)):
			produkt *= int(ziffer)
		return produkt

	def lenght(self,x):
		return len(list(str(x)))


class basisoperatoren(object):

	def addieren(self,a,b):
		return a + b

	def subtrahieren(self,a,b):
		return a - b

	def multiplizieren(self,a,b):
		return a * b

	def dividieren(self,a,b):
		return a/b

	def quadrieren(self,a):
		return pow(a,2)

	def quadratwurzeln(self,a):
		return math.sqrt(a)

	def potenzieren(self,a,b):
		return pow(a,b)

	def negieren(self,a):
		return a*(-1)

	def betrag(self,a):
		return abs(a)

	def wertetabelle_2(self,start,ende,funktion,filename='log.csv'):
		os.system('touch log.csv')
		dateiInhalt = ''
		tabelle = [[],[]]
		tabelle[0] = xrange(start,ende+1)
		for i in range(len(tabelle[0])):
			tabelle[1].append(funktion(tabelle[0][i]))

		for i in range(len(tabelle[0])):
			dateiInhalt += str(tabelle[0][i]) + ';' + str(tabelle[1][i]) + '\n'
		file1 = open(filename,'w')
		F1 = file1.write(dateiInhalt)
		file1.close()
		return tabelle


class eigeneFunktionen(object):
	def __init__(self):
		self.B = basisoperatoren()
		self.M = modulo()
		self.P = polynome()
		self.Q = queroperatoren()

	def f1(self,x):
		a = self.B.negieren(x)
		b = self.Q.lenght(x)
		n = self.B.multiplizieren(a,b)
		y = []
		y.append(self.P.polynom_1(x,a,b))        # y[0]
		y.append(self.B.potenzieren(b,b))        # y[1]
		y.append(self.Q.quersumme(x))            # y[2]
		y.append(self.Q.querprodukt(x))          # y[3]
		y.append(y[1] + y[2] + y[3] + y[0])      # y[4]
		y.append(self.M.modulo_10_pot_n(y[4],4)) # y[5]
		return y[5]

	def f2(self,x):
		y = []
		qp = self.Q.querprodukt_ignore_0(x)
		qs = self.Q.quersumme(x)
		QPqs = self.Q.querprodukt_ignore_0(qs)
		QSqp = self.Q.quersumme(qp)
		y.append(self.B.addieren(QSqp,QPqs))
		y.append(self.B.multiplizieren(QSqp,QPqs))
		return y[0]

E = eigeneFunktionen()
B = basisoperatoren()
B.wertetabelle_2(0,1000,E.f1)