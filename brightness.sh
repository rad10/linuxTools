#!/bin/bash

curBrightness=`xrandr --verbose | grep "Brightness" | cut -d" " -f2`

case "$1" in
    "-set")	xrandr --output eDP-1 --brightness $2 ;;
    "-inc" | "-increase")	xrandr --output eDP-1 --brightness `python -c "print $curBrightness+$2"` ;;
    "-dec" | "-decrease")	xrandr --output eDP-1 --brightness `python -c "print $curBrightness-$2"` ;;
    "-get")	echo $curBrightness ;;
    "-blank")
        if [[ "$curBrightness" == "0.0" ]]; then
            xrandr --output eDP-1 --brightness 1.0
        else
            xrandr --output eDP-1 --brightness 0.0
    fi ;;
    "-bump")
        if [[ "$curBrightness" == "1.0" ]]; then
            xrandr --output eDP-1 --brightness 0.25
            elif [[ "$curBrightness" == "0.25" ]]; then
            xrandr --output eDP-1 --brightness 0.5
            elif [[ "$curBrightness" == "0.50" ]]; then
            xrandr --output eDP-1 --brightness 0.75
            elif [[ "$curBrightness" == "0.75" ]]; then
            xrandr --output eDP-1 --brightness 1.0
        else
            xrandr --output eDP-1 --brightness 1.0
    fi ;;
esac
