#!/usr/bin/python
import urllib
from sys import argv, exit
#[InitConfig]
typed=carrier=tZone=locTime=location=loCalArea=areaCode=""
btyped=bcarrier=btZone=blocTime=blocation=bloCalArea=bareaCode=False
ball=True
phonenumber=0
#[/InitConfig]
#[Config]
for i in argv[1:]:
	if (i=="--all"): ball=True; btyped=bcarrier=btZone=blocTime=blocation=bloCalArea=bareaCode=False
	elif (i.lower()=="-type"): btyped=True
	elif (i.lower()=="-carrier"): bcarrier=True
	elif (i.lower()=="-timezone"): btZone=True
	elif (i.lower()=="-location"): blocation=True
	elif (i.lower()=="-localcallarea"): bloCalArea=True
	elif (i.lower()=="-areacode"): bareaCode=True
	elif (i[0]=="-"):
		print("Error: Command not found")
		exit()
	else:
		phonenumber=i
if (phonenumber==0):
	print("Error: Phonenumber not entered")
	exit()
#[/Config]
#[Site Grabber]
try:
	sock = urllib.urlopen("https://www.searchbug.com/tools/landline-or-cellphone.aspx?FULLPHONE="+str(phonenumber))
	phoneLookup=sock.read()
	sock.close()
except:
	print("Error: cannot connect to site")
	exit()
phoneLookup=phoneLookup.split("\n")
ftyped=filter(lambda x: 'Phone Type:' in x, phoneLookup)
fcarrier=filter(lambda x: 'Carrier:' in x, phoneLookup)
#ftZone=filter(lambda x: 'Phone T' in x, phoneLookup)
#fblocTime=filter(lambda x: 'Phone Type:' in x, phoneLookup)
flocation=filter(lambda x: 'Location:' in x, phoneLookup)
floCalArea=filter(lambda x: 'Local Calling Area:' in x, phoneLookup)
fareaCode=filter(lambda x: 'Area Code:' in x, phoneLookup)
for i in range (0,len(phoneLookup)):
	if (phoneLookup[i]==ftyped[0]):
		typed=phoneLookup[i+2]
		for e in range(0,len(typed)):
			if(typed[e]!=" " and typed[e]!="\t"):
				typed=typed[e:]
				break
	elif (phoneLookup[i]==fcarrier[0]):
		carrier=phoneLookup[i+2]
		for e in range(0,len(carrier)):
			if(carrier[e]!=" " and carrier[e]!="\t"):
				carrier=carrier[e:]
				break
	elif (phoneLookup[i]==flocation[0]):
		location=phoneLookup[i+1]
		for e in range(0,len(location)):
			if (location[e]==">"):
				location=location[e+1:len(location)-7]
				break
	elif (phoneLookup[i]==floCalArea[0]):
		loCalArea=phoneLookup[i+1]
		for e in range(0,len(loCalArea)):
			if (loCalArea[e]==">"):
				loCalArea=loCalArea[e+1:len(loCalArea)-7]
				break
	elif (phoneLookup[i]==fareaCode[0]):
		areaCode=phoneLookup[i+1]
		for e in range(0, len(areaCode)):
			if (areaCode[e]==">"):
				areaCode=areaCode[e+1:len(areaCode)-7]
				break
if ball:
	print("Type: "+str(typed))
	print("Carrier: "+str(carrier))
	print("location: "+str(location))
	print("Local Call Area: "+str(loCalArea))
	print("Areacode: "+str(areaCode))
	print("Done")
if btyped: print(typed)
if bcarrier: print(carrier)
if blocation: print(location)
if bloCalArea: print(loCalArea)
if bareaCode: print(areaCode)
#[/Site Grabber]