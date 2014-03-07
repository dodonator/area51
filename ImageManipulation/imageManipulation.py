from scipy import ndimage
from scipy import misc
import matplotlib.pyplot as plt
import numpy as np

l = misc.lena()

misc.imsave('lena.png', l) # uses the Image module (PIL)

lines = []
lineInput = raw_input("Zahl zwischen 1 sund 512: \n")
print 'Farbe des Graphen: RED'
print ''
lineInput2 = raw_input("Zahl zwischen 1 und 512: \n")
print 'Farbe des Graphen: BLUE'

for xCor in xrange(1,513):
	lines.append(l[xCor-1:xCor, 0:512])
	# misc.imsave('y' + str(xCor-1) + '.png', lines[xCor-1]) # Speicherfunktion

tmpLine  = lines[int(lineInput)]
tmpLine2 = lines[int(lineInput2)]

plt.plot(tmpLine[0],'r') # Plotters
plt.plot(tmpLine2[0],'b')
plt.show()

new_tmpLine = []
new_tmpLine2 = []
for i in xrange(len(tmpLine[0])):
	new_tmpLine.append(255)
	new_tmpLine2.append(0)
l[int(lineInput)] = new_tmpLine
l[int(lineInput2)] = new_tmpLine2
plt.imshow(l)
plt.show()

