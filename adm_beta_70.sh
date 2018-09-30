#!/bin/bash

# Andrew Payne, linux(*t)komputermatrix(d*t)com

# Software current version
soft_name="ADM"
soft_vers="Beta 0.7"

wm="0"

while [ "$wm" -lt 1 ] || [ "$wm" -gt 2 ] ;
do
	printf "\033c" #clear the screen
        printf "\nWelcome to" "$soft_name" "version %s" "$soft_vers, a simple desktop manager script."
	printf "\nPlease pick a window manager or (q) to quit:\n
	(1) xfce4\n
	(2) ratpoison\n"
	read wm
		if [[ $wm = "" ]]; then
			wm="0"
			continue
		elif [[ $wm = "q" ]]; then
	   		exit
		elif (( ("$wm") == "1" )); then
 	   		echo `startx ~/.xinitrc xfce4`
		elif (( ("$wm") == "2" )); then
 	   		echo `startx ~/.xinitrc ratpoison`
		else
			continue
		fi
done
exit
