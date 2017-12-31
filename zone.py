#!/usr/bin/python
import json
from sys import argv
import urllib
#[Intro Config Variables]#
errors=name=dns=help=check=soa=a=aaaa=detail=mx=cname=b=False
url="google.com"
#[/Intro Config Variables]#
for i in argv[1:]: #grabs all args - zone.py
	if (i=="--all"): errors=name=dns=help=check=soa=a=aaaa=detail=mx=cname=True
	elif (i=="-name"): name=True
	elif (i=="-dns"): dns=True
	elif (i=="-check"): check=True
	elif (i=="-soa"): soa=True
	elif (i=="-a"): a=True
	elif (i=="-aaaa"): aaaa=True
	elif (i=="--detail"): detail=True
	elif (i=="-mx"): mx=True
	elif (i=="-cname"): cname=True
	elif (i=="-b"): b=True
	elif (i[0]=="-"): print("Incorrect Command")
	else:
		if (i[0:7]=="http://"): url=i[7:]
		elif (i[0:8]=="https://"): url=(i[8:])
		else: url=i
		#print url
	#else: help=True


#[/Config]#
#[Import JSON info from site]#
try:
	sock = urllib.urlopen("http://api.zone.vision/"+url)
	jsonSite=sock.read()
	sock.close()
	#[/Import JSON from site]#
	jsonData = json.loads(jsonSite) #Turn JSON into usable data
	#[Config]#
except:
	print("Error: cannot connect to site")
	exit()
#[Generator]#

if errors: print("Errors: "+str(jsonData["errors"]))
if name: print("url: "+str(jsonData["name"]))
if dns:
	print("Naming Servers:")
	print("IPv4:")
	if(str(jsonData["parent"]["glue"]["v4"])=="None"): print("+None") #if theres no record, itll display it as no record
	else:
		for i in jsonData["parent"]["glue"]["v4"]: #lists every server that uses ipv6
			print("+Name: "+i["name"]) #lists the name
			print("+Address: "+i["address"]) #lists the address
	print("IPv6:")
	if (str(jsonData["parent"]["glue"]["v6"])=="None"):print("+None") #if theres no record, itll display it as no record
	else:
		for i in jsonData["parent"]["glue"]["v6"]: #lists every server that uses ipv6
			print("+name: "+i["name"]) #lists the name
			print("+Address: "+i["address"]) #lists the address
#[SOA]#
if soa:
	total=0 #holds tally for all servers that say true
	size=0 #tallys all servers, true or not
	for i in jsonData["diagnostics"]["results"][6]["sources"]:
		if jsonData["diagnostics"]["results"][6]["sources"][i]: total=total+1
		size=size+1
	if b: #Only enacts if the program requests a boolean with -b
		if detail: #This setting allows to get details on subject
			if (total==size): print("All SOA Records are present")
			else: print("Not all SOA Records are present")
			for i in jsonData["diagnostics"]["results"][6]["sources"]:
				print(i+": "+str(jsonData["diagnostics"]["results"][6]["sources"][i])) #goes through all servers and sends the name and the info bound to the server name
		else:
			if (total==size): print(True) #this side of script just gives true or false for automation
			else: print(False)
	else:
		if (total==size):
			print("All SOA Records are present")
			for i in range(0,len(jsonData["authoritative"]["soa"])): #used to select all sources possible
				print(jsonData["authoritative"]["soa"][i]["source"]) #Prints the server name
				print("+Name: "+str(jsonData["authoritative"]["soa"][i]["records"][0]["name"])) #Prints the websites name
				print("+Primary Server: "+str(jsonData["authoritative"]["soa"][i]["records"][0]["mname"])) 
				print("+Responsible Party: "+str(jsonData["authoritative"]["soa"][i]["records"][0]["rname"]))
				print("+Serial Number: "+str(jsonData["authoritative"]["soa"][i]["records"][0]["serial"]))
		else: print("There is no A Record info available") #Will only print this is there no record info to be found
#[/SOA]#
#[A]#
if a:
	total=0 #holds tally for all servers that say true
	size=0 #tallys all servers, true or not
	for i in jsonData["diagnostics"]["results"][7]["sources"]:
		if jsonData["diagnostics"]["results"][7]["sources"][i]: total=total+1
		size=size+1
	if b: #Only enacts if the program requests a boolean with -b
		if detail: #This setting allows to get details on subject
			if (total==size): print("All A Records are present")
			else: print("Not all A Records are present")
			for i in jsonData["diagnostics"]["results"][7]["sources"]:
				print(i+": "+str(jsonData["diagnostics"]["results"][7]["sources"][i])) #goes through all servers and sends the name and the info bound to the server name
		else:
			if (total==size): print(True) #this side of script just gives true or false for automation
			else: print(False)
	else:
		if (total==size):
			print("All A Records are present")
			for i in range(0,len(jsonData["authoritative"]["a"])): #used to select all sources possible
				print(jsonData["authoritative"]["a"][i]["source"]) #Prints the server name
				print("+Name: "+str(jsonData["authoritative"]["a"][i]["records"][0]["name"])) #Prints the websites name
				print("+Address: "+str(jsonData["authoritative"]["a"][i]["records"][0]["address"])) #Prints the info given
		else: print("There is no A Record info available") #Will only print this is there no record info to be found
#[/A]#
#[AAAA]#
if aaaa:
	total=0 #holds tally for all servers that say true
	size=0 #tallys all servers, true or not
	for i in jsonData["diagnostics"]["results"][8]["sources"]:
		if jsonData["diagnostics"]["results"][8]["sources"][i]: total=total+1
		size=size+1
	if b: #Only enacts if the program requests a boolean with -b
		if detail: #This setting allows to get details on subject
			if (total==size): print("All AAAA Records are present")
			else: print("Not all AAAA Records are present")
			for i in jsonData["diagnostics"]["results"][8]["sources"]:
				print(i+": "+str(jsonData["diagnostics"]["results"][8]["sources"][i])) #goes through all servers and sends the name and the info bound to the server name
		else:
			if (total==size): print(True) #this side of script just gives true or false for automation
			else: print(False)
	else:
		if (total==size):
			print("All AAAA Records are present")
			for i in range(0,len(jsonData["authoritative"]["aaaa"])): #used to select all sources possible
				print(jsonData["authoritative"]["aaaa"][i]["source"]) #Prints the server name
				print("+Name: "+str(jsonData["authoritative"]["aaaa"][i]["records"][0]["name"])) #Prints the websites name
				print("+Address: "+str(jsonData["authoritative"]["aaaa"][i]["records"][0]["address"])) #Prints the info given
		else: print("There is no A Record info available") #Will only print this is there no record info to be found
#[/AAAA]#
#[MX]#
if mx:
	total=0 #holds tally for all servers that say true
	size=0 #tallys all servers, true or not
	for i in jsonData["diagnostics"]["results"][9]["sources"]:
		if jsonData["diagnostics"]["results"][9]["sources"][i]: total=total+1
		size=size+1
	if b: #Only enacts if the program requests a boolean with -b
		if detail: #This setting allows to get details on subject
			if (total==size): print("All MX Records are present")
			else: print("Not all MX Records are present")
			for i in jsonData["diagnostics"]["results"][9]["sources"]:
				print(i+": "+str(jsonData["diagnostics"]["results"][9]["sources"][i])) #goes through all servers and sends the name and the info bound to the server name
		else:
			if (total==size): print(True) #this side of script just gives true or false for automation
			else: print(False)
	else:
		if (total==size):
			print("All MX Records are present")
			for i in range(0,len(jsonData["authoritative"]["mx"])): #used to select all sources possible
				print(jsonData["authoritative"]["mx"][i]["source"]) #Prints the server name
				print("+Name: "+str(jsonData["authoritative"]["mx"][i]["records"][0]["name"])) #Prints the websites name
				print("+Address: "+str(jsonData["authoritative"]["mx"][i]["records"][0]["exchange"])) #Prints the info given
		else: print("There is no MX Record info available") #Will only print this is there no record info to be found
#[/MX]#
#[CNAME]#
if cname:
	total=0 #holds tally for all servers that say true
	size=0 #tallys all servers, true or not
	for i in jsonData["diagnostics"]["results"][10]["sources"]:
		if jsonData["diagnostics"]["results"][10]["sources"][i]: total=total+1
		size=size+1
	if b: #Only enacts if the program requests a boolean with -b
		if detail: #This setting allows to get details on subject
			if (total==size): print("All CNAME Records are present")
			else: print("Not all CNAME Records are present")
			for i in jsonData["diagnostics"]["results"][10]["sources"]:
				print(i+": "+str(jsonData["diagnostics"]["results"][10]["sources"][i])) #goes through all servers and sends the name and the info bound to the server name
		else:
			if (total==size): print(True) #this side of script just gives true or false for automation
			else: print(False)
	else:
		if (total==size):
			print("All CNAME Records are present")
			for i in range(0,len(jsonData["authoritative"]["cname"])): #used to select all sources possible
				print(jsonData["authoritative"]["cname"][i]["source"]) #Prints the server name
				print("+Name: "+str(jsonData["authoritative"]["cname"][i]["records"][0]["name"])) #Prints the websites name
				#print("+Address: "+str(jsonData["authoritative"]["cname"][i]["records"][0]["address"])) #Prints the info given
		else: print("There is no CNAME Record info available") #Will only print this is there no record info to be found
#[/CNAME]#
#[/Generator]#