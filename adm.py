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
soft_vers = "1.1.7"

import datetime
import getpass
import os
import pathlib
import platform
import readline
import shutil
import socket
import subprocess
import time

# Colors
W = '\033[0m'  # white
O = '\033[33m' # orange

# Lists
wm_sort = []
wm_print = []
wm_choose = []
xinitrc_dir = []

# Home location
user_home   = os.environ['HOME']

# xinitrc location
check_platform =  platform.system()
if "linux" in check_platform.lower():
    xinitrc_dir.append('/etc/X11/xinit')
elif "freebsd" in check_platform.lower():
    xinitrc_dir.append('/usr/local/etc/X11/xinit')
else:
    print(check_platform, "is not supported in this release.  Exiting.")
    exit(1)

for wm in os.listdir(os.path.join(xinitrc_dir[0])):
    if os.path.isdir(os.path.join(xinitrc_dir[0] + "/" + wm)) is False:
        if wm.startswith("xinitrc") and len(wm) > 8:
            wm = wm.replace("xinitrc.", "")
            wm_sort.append(wm)
            wm_sort.sort()
wm_print = {}
key = 1
for wm in wm_sort:
    wm_print.update({key:wm})
    key += 1

# get terminal window size to set layout
getsize = shutil.get_terminal_size()
column,line = getsize
head_factor = (round(line * .0625))
left_factor = (round(column * .0625))
header = ("\n" * head_factor)
margin = (" " * left_factor)
divider = ("-" * 66)

welstr  = ("Welcome to " + O+ soft_name +W + " version " + soft_vers + ", " + soft_tag + ".")

date    = datetime.datetime.now().strftime("%I:%M %p on %A, %b%e %Y.")
datestr = ("It is " + date)

username = getpass.getuser()
hostname = socket.gethostname()
youstr   = ("You are logged in as " + username + " on " + hostname + ".")

system  = platform.system()
release = platform.release()
cpu     = platform.processor()
sysstr  = ("Running " + system + " " + release + " " + cpu)

herestr = ("Here are the window managers found on your system...")

os.system('clear')

print(header)
print(margin + divider)
print(margin + welstr)
print("\n")
print(margin + datestr)
print("\n")
print(margin + youstr)
print("\n")
print(margin + sysstr)
print(margin + divider)
print("")
print(margin + herestr)
print("")
for key,value in wm_print.items():
    print(margin + " " * 4 + "[" + str(key) + "] " + str(value))
print("")

user_num = 0
while user_num == 0 :
    user_num = input(margin + " "*4 + "(Q) to quit, or enter a number: ")
    if user_num == 'Q' or user_num == 'q':
        user_num = 1
        os.system('clear')
        exit(0)
    else:
        try:
            x = int(user_num) - 1
            winman = (wm_sort[x])
            user_uid  = os.getuid()
            group_gid = os.getgid()
            ## COMMENT OUT LINES 133, 134 and 135 TO DISABLE SAFETY BACKUP OF CURRENT XINITRC
            if os.path.isfile(os.path.join(user_home, '.xinitrc')):
                shutil.move(os.path.join(user_home, '.xinitrc'), os.path.join(user_home, '.xinitrc_LAST'))
                os.chmod(os.path.join(user_home, '.xinitrc_LAST'), 0o666)
            shutil.copy2((os.path.join(xinitrc_dir[0] + "/" + "xinitrc." +winman)), os.path.join(user_home, '.xinitrc'))
            os.chown(os.path.join(user_home, '.xinitrc'), user_uid, group_gid)
            print("")
            print((margin + " "*4), end=" ")
            print("-->", end=" ")
            time.sleep(.1)
            print("Starting " + winman)
            time.sleep(.4)
            user_num = 1
            subprocess.run('startx')
            exit(0)
        except ValueError:
            print(margin + " " *4 + "\t" + user_num + " is not an option")
        except IndexError:
            print(margin + " " *4 + "\t" + user_num + " is not an option")
exit(0)
