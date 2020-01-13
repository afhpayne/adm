#! /usr/bin/env python3

# Andrew Payne, info(*t)duckbrainsoftware(d*t)com
# MIT License
# Copyright (c) 2018-2020 Andrew Payne
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# Software Data:
soft_name = "ADM"
soft_tag  = "a simple display manager"

# Version
soft_vers = "1.1.2"

import datetime
import getpass
import os
import platform
import readline
import shutil
import socket
import subprocess

# Colors
W = '\033[0m'  # white
O = '\033[33m' # orange

# Lists  
wm_sort   = []
wm_print  = []
wm_choose = []

# Locations
user_home   = os.environ['HOME']
xinitrc_dir = os.path.join('/etc/X11/xinit')

# Variables
key = 1
user_num = ''

for wm in os.listdir(os.path.join("/etc/X11/xinit/")):
    if os.path.isfile(os.path.join("/etc/X11/xinit/", wm)):
        if wm.startswith('xinitrc') and len(wm) > 8:
            wm_sort.append(wm)
            wm_sort.sort()

for wm in wm_sort:
    wm_print.append("\t\t\t")
    wm_print.append("[")
    wm_print.append(key)
    wm_print.append("]")
    wm_print.append(" ")
    wm_print.append(wm.split('.')[1])
    wm_print.append("\n")
    key += 1
    wm_choose.append(wm)

os.system('clear')
getsize = shutil.get_terminal_size()
col,line = getsize
for i in range(int(round(line/8))):
    print(" ".center(col))
print("\t\t\t------------------------------------------------------------------")
welstr = ("Welcome to " + O+ soft_name +W + " version " + soft_vers + ", " + soft_tag + ".")
print("\t\t\t" + welstr)
print("\n")
date = datetime.datetime.now().strftime("%_I:%M %p on %A, %b %e %Y.")
datestr = ("It is " + date)
print("\t\t\t" + datestr)
youstr = ("You are logged in as " + getpass.getuser() + " on " + socket.gethostname() + ".")
print("\n")
print("\t\t\t" + youstr)
sysstr = ("Running " + platform.system() + " " + platform.release() + ", " + platform.processor())
print("\n")
print("\t\t\t" + sysstr)
print("\t\t\t------------------------------------------------------------------")
herestr = ("Here are the window managers found on your system...")
print("\n")
print("\t\t\t" + herestr)
print("\n")
print(''.join(map(str, wm_print)))
while user_num != 0 :
    user_num = input("\t\t\t(Q) to quit, or enter a number: ")
    if user_num == 'Q' or user_num == 'q':
        os.system('clear')
        break
    else:
        try:
            x = int(user_num) - 1
            winman = (wm_choose[x])
            user_uid  = os.getuid()
            group_gid = os.getgid()
## COMMENT OUT LINES 108, 109 and 110 TO DISABLE SAFETY BACKUP OF CURRENT XINITRC
            if os.path.isfile(os.path.join(user_home, '.xinitrc')):
                shutil.move(os.path.join(user_home, '.xinitrc'), os.path.join(user_home, '.xinitrc_LAST'))
                os.chmod(os.path.join(user_home, '.xinitrc_LAST'), 0o666)
            shutil.copy2(os.path.join(xinitrc_dir, winman), os.path.join(user_home, '.xinitrc'))
            os.chown(os.path.join(user_home, '.xinitrc'), user_uid, group_gid)
            user_num = 0
            subprocess.run('startx')
            exit(0)

        except ValueError:
            print("\t\t\t\t\t\t\t" + user_num + " is not an option")
            user_num=1
        except IndexError:
            print("\t\t\t\t\t\t\t" + user_num + " is not an option")
            user_num=1
exit(0)