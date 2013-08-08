#coding: utf-8
import os
import time
import datetime
import getpass
import random
os.system('clear')
class ZeAPaVer(object):
	def LogDateiAuslesen(self):
		p = open('passwordLog.txt','r')
		self.passwords = p.read()
		p.close()
		
		res = ''
		res += self.passwords[1:]
		self.passwords = res

		self.passwords = self.passwords.split('#')
		tmpPasswords = self.passwords
		self.passwords = {}
		for element in tmpPasswords:
			element = element.split(';')
			# print element
			self.passwords[element[0]] = element[1]
	def formatTimeStamp(self):
		'''
		Formatiert den Time Stamp in einen schönen Stunden , Minuten Array
		Beispielsrückgabe: [23,42]
		'''
		zeit = time.localtime()
		return [zeit[3],zeit[4]]

	def passwordpruefung(self,timestamp,password):
		'''
		Gibt True zurück, wenn das Password hinzugefügt wurde,
		oder es mit dem bereits eingestellten Password übereinstimmt.
		'''
		timestamp = str(timestamp[0]) + ':' + str(timestamp[1])
		if timestamp not in self.passwords:
			self.passwords[timestamp] = password
			return True
		else:
			if self.passwords[timestamp] == password:
				return True
			else:
				return False 
	def standardPassworte(self):
		result = []
		if self.passwordpruefung([0,0],'Midnight'):
			result.append(True)
		else:
			result.append(False)

		if self.passwordpruefung([23,42],'Numerologika'):
			result.append(True)
		else:
			result.append(False)

		if self.passwordpruefung([8,15],'Schulbeginn'):
			result.append(True)
		else:
			result.append(False)

		if self.passwordpruefung([6,18],'Evan'):
			result.append(True)
		else:
			result.append(False)

		if self.passwordpruefung([17,00],'Feierabend'):
			result.append(True)
		else:
			result.append(False)

		if self.passwordpruefung([20,15],'Prime Time'):
			result.append(True)
		else:
			result.append(False)

		'''
		for ergebnis in result:
			print ergebnis
		'''

	def LogUpdate(self):
		passwordListe = ''
		for element in self.passwords:
			passwordListe += '#' + element + ';' + self.passwords[element]
		l = open('passwordLog.txt','w')
		p = l.write(passwordListe)
		l.close()
	def Interaktion(self):
		self.LogDateiAuslesen()
		# self.passwords = {}
		self.standardPassworte()
		#print self.passwords
		zeit = self.formatTimeStamp()
		tmpPassword = getpass.getpass('Bitte geben sie das Passwort ein: ')
		tmpResult = self.passwordpruefung(zeit,tmpPassword)
		self.LogUpdate()
		if tmpResult:
			return True
		else:
			return False
		
Z = ZeAPaVer()
Z.Interaktion()