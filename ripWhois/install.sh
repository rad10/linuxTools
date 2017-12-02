#!/bin/bash
if [ "$(id -u)" != "0" ]; then
	echo "Sorry, you must be in sudo to run this."
	exit 1
fi
mkdir ~/bin
cp rwhoisname ~/bin/
mkdir ~/.rip/
cp ripWhois.py ~/.rip/
