# RasPiSmartMirrorOS (Python 3)
_SmartMirror OS for RaspberryPi_
## About
The SmartMirrorGUI uses python 3 (Im using 3.5.3) in combination with tkinter to display a black fullscreen with (not :P) useful things on it like the weather, the time and a random cartoon from Ruthe.de (or other if you configure it).

In future I want to display the outside/ inside temperature and the CPU temperature (in °C).
## Installation
### Download setup.sh
There are 3 ways to get the setup:
- Download the latest setup [here](installer/setup_latest.sh).
- You can also just copy the text and paste it in any **\*.sh** file.
- The third option is using **wget** (`wget https://github.com/Schn33W0lf/RasPiSmartMirrorOS/blob/master/installer/setup_latest.sh --output-document=/home/$USER/Downloads/SmartMirrorOS_installer.sh`)
### Required setup
#### Software
1. Download an operating System. I have tested it with Noobs and Raspbian stretch.
2. Make sure that your system boots automaticly in Desktop (and logging in) (`sudo raspi-config`, 3 Boot options, B4 Desktop Autologin)
3. Download the installer
4. run it as root (`sudo bash /path/to/SmartMirrorOS.sh`). **Important** is, that you use **sudo** and **bash**, not sh.
#### Hardware
Basicly, you need the RaspberryPi 3 with a µSD-card and a power supply (I suggest to use the official one (5V_, 2.5A) because because of the voltage drop inside the Pi. More in the RPi Forum and [here](https://www.raspberrypi.org/documentation/hardware/raspberrypi/power/README.md)). Im using the RPi 3 B Rev 1.2

Additionally you can solder a perfboard or just connect the status LED and switches with jumper wires. You can find circuit diagrams, plans and other infos [here](hardware)
## Future plans:
- [ ] I want to add 2 temperature sensors (inside temp. and outside temp.)
- [ ] I want to display the CPU temperature
- [ ] I want to remote-control the py (eg for an audioplayer, ...)
- [ ] I want to use a kind of sites in my py script (like [pagepiling](https://alvarotrigo.com/pagePiling/) [\[GitHub\]](https://github.com/alvarotrigo/pagePiling.js)).

# HTML version of the SmartMirrorOS
The scripts arent very nice but here the schematic how it works
```
GPIO in   GPIO out   remote contriol
    |         ^            |
    V         |            V
        PYTHON SCRIPT
              |
              V
      HTML (& JS & CSS)
```
You can find the files [here](html)
- Download the pagepiling folder including the python 3 file _or_
- Just download the html & python file and download the pagepiling files [here](https://github.com/alvarotrigo/pagePiling.js) and put the html/ py file in the folder
- Also create a sh file with:
```
#open the html file in chromium & execute the python file.
$(chromium-browser "file:///path/to/file.html";python3 /path/to/file.py)
#if the python file is stopped, execute the next command.
shutdown 0
```
