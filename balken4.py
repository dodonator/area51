#coding: utf-8
import random
import os
import sys
import time
columns = 112
maxi = columns - 2
#############################################################################################
def graph(amplitude,minimum,maximum,maxiC):
	os.system('clear')
	startwert = int((minimum + maximum)/2)
	if minimum >= maximum:
		raise Exception('Der minimale Wert muss kleiner sein als der maximale Wert!')
	if startwert <= minimum or startwert >= maximum:
		raise Exception('Der Startwert muss zwischen dem Minimum und dem Maximum liegen!')
	if maximum > maxiC or minimum < 1:
		raise Exception('Das Maximum soll unter ' + str(maxiC+1) + '  liegen und das Minimum über 0!')
	last = startwert
	for i in range(50000):
		r1 = random.randint(last - int(amplitude),last + int(amplitude))
		abstandL = int((maxiC - r1)/2)
		abstandR = abstandL
		if r1 < maximum and r1 > minimum:
			print abstandL * ' ' + r1*'*' + (abstandR)*' '
			last = r1
		else:
			pass
Amplituden = [1,5,8,10,15]
Minima = [1,10,50,75]
Maxima = [90,100,110]
counter = 0
mode = raw_input('Modus (a,e): ')
if mode == 'a' or mode == 'A': 
	gesamtZahlDurchLaeufe = len(Amplituden) * len(Minima) * len(Maxima)
	for amplitude in Amplituden:
		for minimum in Minima:
			for maximum in Maxima:
				os.system('clear')
				message = 'Amplitude: ' + str(amplitude) + ' | Minimum: ' + str(minimum) + ' | Maximum: ' + str(maximum) + ' | Startwert: ' + str(int((minimum + maximum)/2))
				abstand = int((maxi-len(message))/2)*' '
				balken = '' 
				for i in range(20):
					os.system('clear')
					balken += '*'
					spaces = (20-len(balken))* ' '
					print '\n'*4
					print abstand + len(message)*'#' + abstand
					print abstand + message + abstand
					print abstand + len(message)*'#' + abstand
					print ( int((maxi-22)/2)-17)*' ' + 'Fortschritt:     [' + balken + spaces + ']' + int((110-22)/2)*' '
					counterFoo = str(counter) + ' von ' + str(gesamtZahlDurchLaeufe) + ' Durchläufen beendet.'
					abstandC = int((maxi-len(counterFoo))/2)*' '
					print abstand + len(message)*'#' + abstand
					print abstandC + counterFoo + abstandC
					print abstand + len(message)*'#' + abstand
					time.sleep(0.5)
				graph(amplitude,minimum,maximum,maxi)
				counter += 1
elif mode == 'e' or mode == 'E':
	runs = []
	for amplitude in Amplituden:
		for minimum in Minima:
			for maximum in Maxima:
			
				runs.append([amplitude,minimum,maximum])
	run = int(raw_input(''))
	run = run-1
	os.system('clear')
	message = 'Amplitude: ' + str(amplitude) + ' | Minimum: ' + str(minimum) + ' | Maximum: ' + str(maximum) + ' | Startwert: ' + str(int((minimum + maximum)/2))
	abstand = int((maxi-len(message))/2)*' '
	print abstand + len(message)*'#' + abstand
	print abstand + message + abstand
	print abstand + len(message)*'#' + abstand
	time.sleep(4)
	graph(runs[run][0],runs[run][1],runs[run][2],maxi)
	
