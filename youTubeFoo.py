import random
import os

curDir = os.getcwd()
if 'youtubeFoo.html' in os.listdir(curDir):
	os.system('rm youtubeFoo.html') 
	os.system('touch youtubeFoo.html')
else:
	os.system('touch youtubeFoo.html')

# Random Youtube video!

alphabet = []
for i in range(65,91):
	alphabet.append(chr(i))
for i in range(97,123):
	alphabet.append(chr(i))

rep = 10
linkVorlage = 'http://www.youtube.com/watch?v='
videoEndungLaenge = 11
HTMLanfang = '<a href="'
HTMLmitte = '">'
HTMLende = '</a><br>'

def linkGeneration():
	videoEndung = ''
	for i in range(videoEndungLaenge):
		videoEndung += random.choice(alphabet)
	link = linkVorlage + videoEndung
	HTMLink = HTMLanfang + link + HTMLmitte + 'Video ' + str(i) + ' ' + HTMLende
	return [link,HTMLink]

dateiInhalt = '<html> \n <body>'
hyperlinks = []
for i in  range(rep):
	hyperlinks.append(str('\n  ' + linkGeneration()[1]))
for link in hyperlinks:
	dateiInhalt += link
dateiInhalt += '\n </body> \n</html>'

print dateiInhalt

f1 = open('youtubeFoo.html','w')
file1 = f1.write(dateiInhalt)
f1.close()
os.system('chromium-browser youtubeFoo.html')



