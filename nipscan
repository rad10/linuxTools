#!/bin/bash

#test to see if nmap is installed
command -v nmap >/dev/null 2>&1 || { echo >&2 "Error: Nmap isnt installed. Please install nmap to run this script. Exiting."; exit 1; }

#init variables
spot=("$1" "$2" "$3" "$4" "$5" "$6" "$7" "$8")
v=true; t=false
opt="-sL"

#options
for i in `seq 0 $((${#spot[@]}-1))`; do
	case "${spot[$i]}" in
		"-a" | "-alive" | "--alive")	opt="-F" ;;
		"-f" | "-file" | "--file")	ip=`cat ${spot[$(($i+1))]}` ;;
		"-tl" | "-textlist" | "--textlist")	ip=${spot[$(($i+1))]} ;;
		"-ln" | "-local" | "--local")	ip=`hostname -I | cut -d" " -f1 | cut -d"." -f1,2,3`.0-255 ;;
		"-vi" | "-visual" | "--visual")	v=true; t=false ;;
		"-t")	t=true; v=false ;;
		"-r")	opt="$opt -Pn" ;;
		"-ar" | "-ra")	opt="-F -Pn" ;;
		"-e" | "-extra" | "--extra")	opt="$opt ${spot[$(($i+1))]}" ;;
		"-h" | "-help" | "--help")
		echo -e "\n$0 [OPTION] [IPADDRESS]"
		echo "$0 is a program made to scan a list of ip's and return a list of alive hosts and their names. This program is dependant on nmap and its functions to properly work"
		echo -e "\nOptions:\n"
		echo "-a | (-)-alive			Filters results to only currently active machines"
		echo "-f | (-)-file			Input ip list from file"
		echo "-tl | (-)-textlist [default]	Input ip's. it can be 1 or more, but to have you multiple it must be in quotes and there has to be a space in between each ip address. you can also scan multiple addresses with a - in between the numbers"
		echo -e "				Example: \"123.456.789.101 987.654.321.012\" \"123.832.1.0-255 101.204.294.103\""
		echo "-ln | (-)-local			Scans entire local network. no given ip address is required"
		echo "-vi | (-)-visual [default]	Gives you a visual with alive machine ip's and names. it is on by default"
		echo "-t				simple output. doesnt give names, but gives alive ips in list for to be used by other programs"
		echo "-e | (-)-extra			Add extra Args for scan (Specifically nmap options)"
		exit 1;;
		"-"*)	echo "Error: incorrect command use. Command ${spot[$i]} doesnt exist. use $0 -h to find possible arguements"; exit 1 ;;
		*)	if [[ "${spot[$i]}" != "-"* ]] && [[(-n ${spot[$i]})]] && [[(-z ${spot[$(($i+1))]})]]; then
				ip=${spot[$i]}
			fi
			break ;;
	esac
done
if [[(-z $1)]]; then
	$0 -h
	exit 1
fi
if [[ "$1" != "-"* ]]; then
	v=true; ip=$1
fi
#gen options
if $v; then
	nmap $opt $ip | grep "scan report for" | grep --color=never "(*.*.*.*)"
fi
if $t; then
	nmap $opt $ip | grep "scan report for" | grep -o --color=never "(*.*.*.*)" | cut -d")" -f1 | cut -d"(" -f2
fi
