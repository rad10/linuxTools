#!/bin/bash
#if [ "$(id -u)" != "0" ]; then
#	echo "Sorry, you must be in sudo to run this."
#	exit 1
#fi
sudo cp arpmap /usr/local/bin/
mkdir ~/.arpip/
cp arp.py ~/.arpip/
