from sys import argv, exit
html = str(argv[1]) # this holds all of the html sourcing
try:
	html=html.split('<table border="1">')[1]
except:
	if "-web" in argv:
		exit()
	print("There are 0 domains attached to this ip")
	exit()
html=html.replace("</tr><tr>","|")
html=html.replace('</td><td align="center">',"\\")
html=html.replace("</td>| <td>","|")
html=html.replace("</td><td>","\\")
html=html.replace("</td></tr></table><br></td>|</tr>","")
html=html.replace("<tr><td>","")
rows=html.split("|")
for i in range(len(rows)):
	rows[i]=rows[i].split("\\")

#Grabbing Samplesize if there
e = 1
while argv[e][:2] != "-s": e+=1
sampleSize=int(argv[e][2:])

### print results
size = sampleSize+2 if (sampleSize > 0) else len(rows)
if "-web" in argv[2:]:
	for i in range(1,size-1):
		print(str(rows[i][0]))
else:
	print(str(rows[0][0])+" | "+str(rows[0][1]))
	print "----------------------"
	for i in range(1,size-1):
		print(str(rows[i][0])+" | "+str(rows[i][1]))
