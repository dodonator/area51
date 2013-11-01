import random
import os
import sys
amplitude = 5
while amplitude != 'q':
	os.system('clear')
	last = 55
	amplitude = raw_input('Amplitude:        ')
	if amplitude == 'q':
		sys.exit()
	minimum = int(raw_input('Minimum (min. 10):  '))
	maximum = int(raw_input('Maximum (max. 110): '))
	last = int(raw_input('Startwert:          '))
	while True:
		r1 = random.randint(last - int(amplitude),last + int(amplitude))
		abstandL = int((110 - r1)/2)
		abstandR = abstandL
		if r1 < maximum and r1 > minimum:
			print abstandL * ' ' + r1*'*' + (abstandR)*' '
			last = r1
		else:
			pass	 	