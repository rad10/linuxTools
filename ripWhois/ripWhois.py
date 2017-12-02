html=open("ripHtml","r").read()
html=html.split('<table border="1">')[1]
html=html.replace("</td></tr><tr><td>","|")
html=html.replace('</td><td>',":")
html=html.replace("</td></tr></table><br></td></tr><tr></tr>","")
html=html.replace("<tr><td>","")
html=html.replace('</td><td width="130">',":")
#print html
rows=html.split("|")
#print rows
for i in range(0,len(rows)):
	rows[i]=rows[i].split(":")
#print rows
### print results
print(str(rows[0][0])+" | "+str(rows[0][1])+" | "+str(rows[0][2]))
print "----------------------"
if len(rows) > 2:
	for i in range(1,len(rows)-1):
		print(str(rows[i][0])+" | "+str(rows[i][1])+" | "+str(rows[i][2]))
else: print(str(rows[1][0])+" | "+str(rows[1][1])+" | "+str(rows[1][2]))
print("Admin holds "+str(len(rows)-1)+" domains")
