#!/usr/bin/python
from sys import argv, exit
import nmap

#[InitConfig]#
scanner = nmap.PortScanner()
d = False
ip = []
opts = ["-F"]
#[/InitConfig]#
#[Help]#


def help():
    print("isipalive.py [HOSTS]")
    print("isipalive.py is a function script. input an ip address and it will return 1 or 0 for true or false is the address is alive.")
    exit()


#[/Help]#
#[Config]#
for i in argv[1:]:
    if (i == "-d" or i == "-display" or i == "--display"):
        d = True
#[/Config]#
