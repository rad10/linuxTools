html=open("ripHtml","r").read()
#html="<table><tr><td>Hello</td><td>World1</td></tr><tr><td>Hello</td><td>World2</td></tr><tr><td>Hello</td><td>World3</td></tr><tr><td>Hello</td><td>World4</td></tr><tr><td>Hello</td><td>World5</td></tr><tr><td>Hello</td><td>World6</td></tr></table>"
html=html.split('<table border="1">')[1]
html=html.replace("</tr><tr>","|")
html=html.replace('</td><td align="center">',"\\")
html=html.replace("</td>| <td>","|")
html=html.replace("</td><td>","\\")
html=html.replace("</td></tr></table><br></td>|</tr>","")
html=html.replace("<tr><td>","")
rows=html.split("|")
for i in range(0,len(rows)):
	rows[i]=rows[i].split("\\")

### print results
print(str(rows[0][0])+" | "+str(rows[0][1]))
print "----------------------"
for i in range(1,len(rows)-1):
	print(str(rows[i][0])+" | "+str(rows[i][1]))

