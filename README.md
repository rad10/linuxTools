# linuxTools
These are the tools that I've made for my Linux System. some of the tools require other tools like nmap to function.

# Brightness
this is a program that is supposed to fix the frightness function on linux systems. It gives options:
-set		sets an exact number for brightness (best to stay between 0.0-1.0)
-inc		increases the brightness by a given amount
-dec		decreases the brightness by a given amount
-get		gets the current brightness on the monitor
-blank	blank is a switch between 0.0 and 1.0
-bump		It periodically bumps the brightness from 0.25, 0.5, 0.75 and 1 and increases with every press until its reset back to 0.25

# Staticip
Its one purpose is to go to get the network static ip address for the router.
it goes through http://ipecho.net/plain

# ipsearch
this is an old script that may or may not work. I havent had time to test and fix it, but it is up to you to play with it and see if you can fix it.

# localip
gets the local ip address on the current network using hostname

# nipscan
Nmap Ipscan is a program that takes a list of ip addresses or group of ip addresses and gives a list of alive hosts along with possible hostnames
!!Requires nmap to run
Here are the options:
-a | (-)-alive			Filters results to only currently active machines
-f | (-)-file			Input ip list from file
-tl | (-)-textlist [default]	Input ip's. it can be 1 or more, but to have you multiple it must be in quotes and there has to be a space in between each ip address. you can also scan multiple addresses with a - in between the numbers
-e 				Example: "123.456.789.101 987.654.321.012" "123.832.1.0-255 101.204.294.103"
-ln | (-)-local			Scans entire local network. no given ip address is required
-vi | (-)-visual [default]	Gives you a visual with alive machine ip's and names. it is on by default
-t				simple output. doesnt give names, but gives alive ips in list for to be used by other programs
-e | (-)-extra			Add extra Args for scan (Specifically nmap options)

# Phonelookup
This is a script with the purpose of collecting information on a phone.
it goes through an active web server page get its information: https://www.searchbug.com/tools/landline-or-cellphone.aspx
This has no working options, but basically, you run the script and give it a phone number to look up
