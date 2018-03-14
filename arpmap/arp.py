#!/bin/python
from sys import argv, exit
iplist=str(argv[1])
#iplist=open("arplist.txt","r").read()
ip=iplist.split("\n")
for i in range(0,len(ip)):
	ip[i]=ip[i].split("\t")
for i in range(0,len(ip)):
	print ip[i][0]
