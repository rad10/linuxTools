#!/bin/bash
cd=false
co=false
ci=false
cl=false
cs=false
ip=0
while getopts "do:is:l" opt; do
	case $opt in
		d)		cd=true ;;	#show dead too
		o)		co=true; IFS=$'\n' read -rd '' -a ipList <<< "$OPTARG"	;;	#get iplist from file
		i)		ci=true ;;	#return with ip only
		s)		cs=true; ip=$OPTARG ;; #certain ip. can be range with *
		l)		cl=true	#scan local network
				localip=`ip addr | grep "inet " | grep "brd" | cut -d"/" -f1 | cut -d" " -f6`
				ip=`echo $localip | cut -d"." -f1,2,3`.*
				;;
	esac
done

#scan function


#main script
if $co; then
	for e  in ${#ipList[@]} ; do
		result=`ping -c 1 -W 2147 $e | grep -c "1 received"`
		if [ "$result" == "1" ]; then
			if $ci; then echo $e
			else
				echo "isAlive: true"
				echo "	$e"
			fi
		elif $cd; then
			echo "isAlive:false"
			echo "	$e"
		fi
	done
fi
if $cs; then
	result=`ping -c 1 -W 2147 $ip | grep -c "1 received"`
	if [ "$result" == "1" ]; then
		if $ci; then echo $ip
		else
			echo "isAlive: true"
			echo "	$ip"
		fi
	elif $cd; then
		echo "isAlive:false"
		echo "	$ip"
	fi
fi
if $cl; then
	for x in `seq 1 255`; do
		clipIp=`echo $ip | cut -d"." -f1,2,3`.$x
		result=`ping -c 1 -W 20 $clipIp | grep -c "1 received"`
		if [ "$result" == "1" ]; then
			if $ci; then echo $clipIp
			else
				echo "isAlive: true"
				echo "	$clipIp"
			fi
		elif $cd; then
			echo "isAlive:false"
			echo "	$clipIp"
		fi
	done
fi
