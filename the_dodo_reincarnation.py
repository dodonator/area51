#coding: utf-8
import turtle
import math

class dodo(turtle.Turtle):
	
	def __init__(self):
		self.figure = turtle.Turtle()
		self.speed = 5
		self.figure.speed(self.speed)
		turtle.colormode(255)
		self.army = {}
		self.army['default'] = self.figure

# Funktionen die Bewegen!
# Movefunctions

	def fd(self,length,name='default'):
		'''
		Move - Forward
		length : distance to walk
		name : figure to move (default = 'default')
		'''
		self.army[name].fd(length)

	def lt(self,gradient,name='default'):
		self.army[name].lt(gradient)

	def rt(self,gradient,name='default'):
		self.army[name].rt(gradient)

	def FL(self,length,gradient,name='default'):
		self.lt(gradient,name)
		self.fd(length,name)

	def FR(self,length,gradient,name='default'):
		self.rt(gradient,name)
		self.fd(length,name)

# Vorgefertigte Formen!
# Default shapes

	def draw_spirale_L(self,anfang,steigung,winkel,rep,name='default'):
		for x in xrange(rep):
			self.fd(anfang,name)
			self.lt(winkel,name)
			anfang += steigung

	def draw_spirale_R(self,anfang,steigung,winkel,rep,name='default'):
		for x in xrange(rep):
			self.fd(anfang,name)
			self.rt(winkel,name)
			anfang += steigung

	def draw_nikolaus(self,laenge,rep,name='default'):
		self.hide(name)
		self.army[name].penup()
		self.lt(180)
		self.fd(int(rep*laenge/2))
		self.lt(180)
		self.show(name)
		self.army[name].pendown()
		dachLaenge = int(math.sqrt((laenge*laenge)/2))
		for x in xrange(rep):
			self.fd(laenge,name)
			self.lt(135,name)
			self.fd(int(math.sqrt(2*laenge*laenge)),name)
			self.rt(135,name)
			self.fd(laenge,name)
			self.rt(135,name)
			self.fd(int(math.sqrt(2*laenge*laenge)),name)
			self.rt(135,name)
			self.fd(laenge,name)
			self.rt(45,name)
			self.fd(dachLaenge,name)
			self.rt(90,name)
			self.fd(dachLaenge,name)
			self.rt(45,name)
			self.fd(laenge,name)
			self.lt(90,name)

	def draw_oktogon_L(self,laenge,name='default'):
		for i in xrange(8):
			self.lt(45,name)
			self.fd(laenge,name)

	def draw_oktogon_R(self,laenge,name='default'):
		for i in xrange(8):
			self.rt(45,name)
			self.fd(laenge,name)

	def draw_square_L(self,hoehe,breite,name='default'):
		halfBreite = int(breite/2)
		self.hide(name)
		self.figure.penup()
		self.lt(180,name)
		self.fd(halfBreite,name)
		self.lt(180,name)
		self.figure.pendown()
		self.show(name)
		self.fd(halfBreite,name)
		self.lt(90,name)
		self.fd(hoehe,name)
		self.lt(90,name)
		self.fd(breite,name)
		self.lt(90,name)
		self.fd(hoehe,name)
		self.lt(90,name)
		self.fd(breite,name)

	def draw_square_R(self,hoehe,breite,name='default'):
		halfBreite = int(breite/2)
		self.hide(name)
		self.figure.penup()
		self.rt(180,name)
		self.fd(halfBreite,name)
		self.figure.pendown()
		self.show(name)
		self.fd(halfBreite,name)
		self.rt(90,name)
		self.fd(hoehe,name)
		self.rt(90,name)
		self.fd(breite,name)
		self.rt(90,name)
		self.fd(hoehe,name)
		self.rt(90,name)
		self.fd(breite,name)

	def draw_circle_D(self,length,precision,fillB=False,color=(0,0,0),name='default'):
		if fillB:
			self.army[name].fillcolor(color)
			self.army[name].fill(fillB)
		rep = 360/precision
		for i in xrange(rep):
			self.fd(length,name)
			self.lt(precision,name)
		if fillB:
			self.army[name].fill(False)

	def draw_circle_Def(self,radius,extent=None,steps=None,name='default'):
		self.army[name].circle(radius, extent, steps)

	def draw_circle_figure(self,number,radians,name='default'):
		for i in xrange(number):
			self.draw_circle_Def(radians,None,None,name)
			self.lt(int(360/number),name)

# Statusabfragen und Statusdefinitionen
# Tell to the turtle

	def hide(self,name='default'):
		self.army[name].ht()

	def show(self,name='default'):
		self.army[name].st()

	def set_Speed(self,value,name='default'):
		self.speed = value
		self.army[name].speed(self.speed)

	def get_Position(self,name='default'):
		return self.army[name].position()

	def setPosition(self,x,y,name='default'):
		self.army[name].goto(x,y)

	def get_Speed(self,name='default'):
		return self.army[name].speed()

	def get_xPos(self,name='default'):
		return self.army[name].xcor()

	def set_xPos(self,position,name='default'):
		self.army[name].setx(position)

	def get_yPos(self,name='default'):
		return self.army[name].ycor()	
	
	def set_yPos(self,position,name='default'):
		self.army[name].sety(position)

	def goHomeDodoYouAreDrunk(self,name='default'):
		self.army[name].home()

	def wait(self):
		x = raw_input('')

	def reset(self,name='default'):
		self.army[name].reset()

# Die Reinkarnation der Dodos hat begonnen! Fürchtet die Macht der Urzeitlaufvögel!
# The reincarnation of the dodo has begun! Fear the power of the primitive ratites!

	def reincarnationOfTheDodos(self,name):
		self.army[name] = self.figure.clone()
		return self.get_length_of_Army()

	def get_army(self):
		return self.army

	def get_dodo(self,name):
		return self.army[name]

	def get_length_of_Army(self):
		return len(self.army)

turtle = dodo()
# Action!
turtle.wait()