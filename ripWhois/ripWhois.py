from sys import argv, exit
html = str(argv[1]) # this holds all of the html sourcing
try:
	html=html.split('<table border="1">')[1]
except:
	if "-web" in argv:
		exit()
	print("This Admin doesn't own a site")
	exit()
html=html.replace("</td></tr><tr><td>","|")
html=html.replace('</td><td>',":")
html=html.replace("</td></tr></table><br></td></tr><tr></tr>","")
html=html.replace("<tr><td>","")
html=html.replace('</td><td width="130">',":")
#print html
rows=html.split("|")
#print rows
for i in range(len(rows)):
	rows[i]=rows[i].split(":")
#print rows

e = 1
while argv[e][:2] != "-s": e+=1
sampleSize=int(argv[e][2:])

size = sampleSize+2 if (sampleSize > 0) else len(rows)
### print results
if "-web" in argv[2:]:
	if size > 2:
		for i in range(1,size-1):
			print(str(rows[i][0]))
	else: print(str(rows[1][0]))
else:
	print(str(rows[0][0]))
	print "----------------------"
	if size > 2:
		for i in range(1,size-1):
			print(str(rows[i][0])+" | "+str(rows[i][1])+" | "+str(rows[i][2]))
	else: print(str(rows[1][0])+" | "+str(rows[1][1])+" | "+str(rows[1][2]))
	print("Admin holds "+str(len(rows)-1)+" domains")
