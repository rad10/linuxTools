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

# Reverse IP (rip)
Reverse IP is made to find all of the websites on a machine.
You input an IP address and it gives you up to 1000 web addresses on that server.
This application uses viewdns.info to get its information.

Options:

-gui	Uses w3m to view what is shown on the actual website.


# Reverse Whois
This application takes a persons name and returns all of the websites they own up to 1000 websites.
It requires two words to search, like in this example "rwhoisname John Doe" but it can include more names by adding a plus to the second name, like in example "rwhoisname James Robert+Fields"
This application uses viewdns.info to collect its information

Options:

-gui	Uses w3m to view what is shown on the actual website.


# Arpmap
!! requires arp-scan and nmap to run !!
Arpmap is an application that combines arp-scan and nmap to find all of the machines on a local network then find their display names
It can also be set to scan the ports on all local machines. Including an intensive scan.

Options:

-f | (-)-file			Input ip list from file

-tl | (-)-textlist [default]	Input ip's. it can be 1 or more, but to have you multiple it must be in quotes and there has to be a space in between each ip address. you can also scan multiple addresses with a - in between the numbers

				Example: "123.456.789.101 987.654.321.012" "123.832.1.0-255 101.204.294.103"

-ln | (-)-local			Scans entire local network. no given ip address is required

-vi | (-)-visual [default]	Gives you a visual with alive machine ip's and names. it is on by default

-t				simple output. doesnt give names, but gives alive ips in list for to be used by other program

-p				Scans ports on all machines

-P				Scans all ports intensively. similiar to  zenmaps intensive scan

-e				Scans ports along with services and OS

-r				Adds -Pn command to nmap script
