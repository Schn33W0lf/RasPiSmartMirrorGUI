# RasPiSmartMirrorOS
_SmartMirror OS for RaspberryPi_
## About
The SmartMirrorGUI uses python 3 (Im using 3.5.3) in combination with tkinter to display a black fullscreen with (not :P) useful things on it like the weather, the time and a random cartoon from Ruthe.de (or other if you configure it).

In future I want to display the outside/ inside temperature and the CPU temperature (in °C).
## Installation
### Download setup.sh
Download the latest setup [here](installer/latest.sh).

You can also just copy the text and paste it in any **\*.sh** file.

The third option is using **wget** (`wget <URL> --output-document=/home/$USER/Downloads/SmartMirrorOS_installer.sh`)

### Required setup
#### Software
1. Download an operating System. I have tested it with Noobs and Raspbian stretch.
2. Make sure that your system boots automaticly in Desktop (and logging in) (`sudo raspi-config`, 3 Boot options, B4 Desktop Autologin)
3. Download the installer
4. run it with sudo (`sudo bash /path/to/SmartMirrorOS.sh`). **Important** is, that you use **sudo** and **bash**, not sh.
#### Hardware
Basicly, you need the RaspberryPi 3 with µSD-card and a power supply (I suggest to use the official one because because of the voltage drop in the Pi. More in the RPi Forum and [here](https://www.raspberrypi.org/documentation/hardware/raspberrypi/power/README.md)). Im using the RPi 3 B Rev 1.2

Additionally you can solder a perfboard or just connect the status LED and switches with jumper wires. You can find circuit diagrams, plans and other infos [here](hardware)
