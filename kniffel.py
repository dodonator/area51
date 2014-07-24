#coding: utf-8
import uuid
# kniffel


class feldOben(object):
	pass


class feldUnten(object):
	pass


class wurf(object):
	def __init__(self):
		self.würfelzahl = 5


class wuerfel(object):
	def __init__(self):
		self.gesamtWahrscheinlichkeit = 100
		self.ID = uuid.uuid4()
	
	def wahrscheinlichkeitsRechner(self):
		self.wahrscheinlichkeiten = []
		if self.gesamtWahrscheinlichkeit % self.augenzahl == 0:
			for i in range(self.augenzahl):
				self.wahrscheinlichkeiten.append(int(self.gesamtWahrscheinlichkeit/self.augenzahl))
		else:
			rest = self.gesamtWahrscheinlichkeit % self.augenzahl
			tmpWahr = (self.gesamtWahrscheinlichkeit + (self.augenzahl - rest)) / self.augenzahl
			for i in range(self.augenzahl):
				self.wahrscheinlichkeiten.append(int(tmpWahr))
	
	def get_ID(self):
		return self.ID

	def set_augenzahl(self,augenzahl):
		self.augenzahl = augenzahl

	def get_augenzahl(self):
		return self.augenzahl



class player(object):
	def __init__(self,kontostand):
		self.kontostand = kontostand
	
	def set_playername(playername):
		self.playername = playername
	
	def get_playername(self):
		return self.playername

	def get_kontostand(self):
		return self.kontostand
		
