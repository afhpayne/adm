#!/bin/sh

# xinitrc script adapted from the Arch Wiki
# https://wiki.archlinux.org/index.php/Xinit#xinitrc

userresources=$HOME/.Xresources
usermodmap=$HOME/.Xmodmap
sysresources=/etc/X11/xinit/.Xresources
sysmodmap=/etc/X11/xinit/.Xmodmap

# merge in defaults and keymaps

if [ -f $sysresources ]; then
    xrdb -merge $sysresources

fi

if [ -f $sysmodmap ]; then
    xmodmap $sysmodmap
fi

if [ -f "$userresources" ]; then
    xrdb -merge "$userresources"
fi

if [ -f "$usermodmap" ]; then
    xmodmap "$usermodmap"
fi

# start some nice programs

if [ -d /etc/X11/xinit/xinitrc.d ] ; then
 for f in /etc/X11/xinit/xinitrc.d/?*.sh ; do
  [ -x "$f" ] && . "$f"
 done
 unset f
fi

# Xmonad is the default, additional examples below
# It is also possible to trigger a executable startup file containing
# apps to be launched when starting a WM

session=${1:-xmonad}

case $session in
    xmonad            ) xterm & xterm & xterm & dropbox & exec xmonad;;
    openbox           ) dropbox & exec openbox-session;;
    i3                ) dropbox & exec i3;;
    spectrwm          ) exec /home/user/folder/start_file
    # No known session, try to run it as command
    *                 ) exec $1;;
esac
