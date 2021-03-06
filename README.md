adm is a simple cli-only display manager.

adm will:

* present a friendly command-line interface showing time and date, user and system
* automatically display installed window managers or desktop environments
* launch one with a single keyboard press

CONTENTS:

[Dependencies](#dependencies)

[Running adm](#running)

[Notes](#notes)

[Release Notes](#release-notes)

[Screenshot](#screenshot)

[Beginners Help](#beginners-help)


<br><br>
## Dependencies:

Python3


<br><br>
## Running:

1. Download adm.py, make it executable, and place it with user-executable files (e.g., /usr/local/bin/).  When you login on reboot, just type 'adm.py' in your terminal.

2. To have adm start automatically when a user logs in, simply append
    ```
    adm.py
    ```
    to your .bash_profile

<br><br>
## Notes:

adm uses startx and it looks for xinitrc files in /etc/X11/xinit/ in Linux or /usr/local/etc/X11/xinit in FreeBSD
* these files should be called xinitrc.name_of_wm
* there's a template in that folder to build from - most window managers startup by adding the final line:
    ```
    exec name_of_wm
    ```
* this method also means you can also have different startup configurations for different window managers
* adm will replace the .xinitrc file in your home directory!  To be safe, it will back up the one there as
    ```
    .xinitrc_LAST
    ```
  You can disable this behavior by commenting out lines in the code that have been marked.

* NixOS support means adm will search in a user location for xinitrc files. I keep mine in a git directory for example. This location is currently hard-coded.

<br><br>
## Release notes:
1.2.2 Bug fix, failed to parse list of Linux options <br>
1.2.1 Bug fix check os-release  <br>
1.2.0 Bug fix 'distro' deprecated, now adm reads os-release <br>
1.1.9 Add support for NixOS using startx <br>
1.1.8 Layout fix <br>
1.1.7 Major code overhaul; now responsive to any monitor resolution; more efficient identification of xinitrc files, stability improvements<br>
1.1.6 Added FreeBSD support, bug fixes

<br><br>
## Screenshot  
![screenshot](https://github.com/afhpayne/adm/blob/master/adm.png "adm screenshot")

<br><br>
## Beginners' Help  

If you're new to non-graphical Python programs, using them is still easy.

* You can always run one by navigating into its folder using your terminal and typing:
  ```
  python3 program_name
  ```
  I use python3 in the example to be certain, but a thoughtfully formatted program should be ok with just 'python' - sometimes a fatal syntax error is a clue your program is calling the wrong version of Python.

* You can make life easier by making the program executable:
  ```
  chmod +x program_name
  ```
  This means you can do away with 'python3' and just type:
  ```
  program_name
  ```
* You can now go step further and place your program in an executable directory, such as:
  ```
  mv program_name /usr/local/bin
  ```
  /usr/bin/local is one of several possible locations common in Linux.  Doing so means that simply opening a terminal and typing the program_name will run the program.  No need to go to the directory itself.

* Lastly, you can go a step further still and make your own executable directory, such as:
  ```
  mkdir -p /home/username/bin
  ```
  Then you would add this line to your .bash_profile:
  ```
  PATH=$PATH:/home/username/bin
  ```
  and
  ```
  reboot
  ```
  Replace _username_ with your own and you're off...
