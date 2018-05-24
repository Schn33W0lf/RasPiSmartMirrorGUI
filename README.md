# RasPiSmartMirrorGUI (Python 3)
_SmartMirror for RaspberryPi_<br>
[_**\[Bottom\]**_](#bottom)<br>
**Important:** Actually crontab does'nt do what I want... Run python3 /opt/SM_GUI_py3.5-tk/SM_GUI_v0.4.1.minimal.py manually <br>
Either, I have problems with the timeout of the dispay. Maybe its a problem of my display, maybe I looked for the wrong configs on the Pi.
## Content
**_\[ [&uarr;](#top)_ / _[&darr;](#bottom) \]_**
### Project
**_\[ [&uarr;](#top)_ / _[&darr;](#bottom) \]_**

| No. | Title | Status | Comment / Description |
| :--- | :--- | :---: | :---: |
| 1. | [python3 installer](python3/setup_v3.5.sh) | finished | v3.5 (for alpha/beta: 0.3.1 - 0.3.5, not recommended) |
| 2. | [python3 installer](python3/setup_latest.sh) | finished | v3.6 (for beta2: > 0.4.0, recommended) |
| 3. | [python3 installer](python3/setup_v4.0fbv.sh) | work in progress | v4.0fbv.sh (for all full/ basic versions, >1.0.0) |
| 4. | [python3 GUI (0.3.1)](python3/SM_GUI_v0.3.1.minimal.py) | finished | alpha |
| 5. | [python3 GUI (0.3.2)](python3/SM_GUI_v0.3.2.minimal.py) | finished | alpha |
| 6. | [python3 GUI (0.3.3)](python3/SM_GUI_v0.3.3.minimal.py) | finished | alpha |
| 7. | [python3 GUI (0.3.4)](python3/SM_GUI_v0.3.4.minimal.py) | finished | beta |
| 8. | [python3 GUI (0.3.5)](python3/SM_GUI_v0.3.5.minimal.py) | finished | beta |
| 9. | [python3 GUI (0.4.0)](python3/SM_GUI_v0.4.0.py) | finished | beta 2 |
| 10. | [python3 GUI (0.4.1)](python3/SM_GUI_v0.4.1.py) | finished | beta 2 |
| 11. | [python3 GUI (0.5.0)](python3/SM_GUI_v0.5.0.py) | finished | beta 2 |
| 12. | [python3 GUI (1.0.0b)](python3/SM_GUI_v1.0.0-basic.py) | finished | basic |
| 13. | [python3 GUI (1.0.0f)](python3/SM_GUI_v1.0.0-full.py) | work in progress | fulll |
### Documentation
**_\[ [&uarr;](#top)_ / _[&darr;](#bottom) \]_**

| No. | Title |
| :--- | :--- |
| 1. | [Content](#content) |
| 1.1 | [Project](#project) |
| 1.2 | [Documentation](#documentation) |
| 2. | [About](#about) |
| 3. | [Installation](#installation) |
| 4.1. | [Download setup.sh](#download-setupsh) |
| 4.2. | [Required setup](#required-setup) |
| 4.2.1. | [Software](#software) |
| 4.2.1. | [Configuration (Python)](#configuration-python) |
| 4.2.1.1. | [Weather Widget](#weather-widget) |
| 4.2.1.2. | [Settings](#settings) |
| 4.2.2. | [Hardware](#hardware) |
| 5. | [Future plans](#future-plans) |
| 6. | [Troubleshooting](#troubleshooting) |
| 6.1. | [Troubles with PIL](#troubles-with-pil) |
## About
**_\[ [&uarr;](#top)_ / _[&darr;](#bottom) \]_**<br>
The SmartMirrorGUI uses python 3 (Im using 3.5.3) in combination with tkinter to display a black fullscreen with (not :P) useful things on it like the weather, the date and time and a random cartoon from Ruthe.de (or other if you configure it). Further, the CPU-, Inside- and Outside Temperature is displayed (in °C). Below, a text, loaded from the internet is displayed it can be a random joke, an info that you've got messages, some news and other crazy stuff. Actually its loaded from a text file. More details below.
## Installation
**_\[ [&uarr;](#top)_ / _[&darr;](#bottom) \]_**<br>
### Download setup.sh
**_\[ [&uarr;](#top)_ / _[&darr;](#bottom) \]_**<br>
There are 3 ways to get the setup:
- Download any setup [here](python3) (Recommended is the [latest](python3/setup_latest.sh) or the [full](python3/setup_v4.0fbv.sh) setup).
- You can also just copy the text and paste it in any **\*.sh** file.
- The third option is using **wget** (`wget https://raw.githubusercontent.com/Schn33W0lf/RasPiSmartMirrorOS/master/python3/setup_latest.sh --output-document=/home/$USER/Downloads/SmartMirrorOS_installer.sh` **or** `wget https://raw.githubusercontent.com/Schn33W0lf/RasPiSmartMirrorOS/master/python3/setup_v4.0fbv.sh --output-document=/home/$USER/Downloads/SmartMirrorOS_installer.sh`).
### Required setup
**_\[ [&uarr;](#top)_ / _[&darr;](#bottom) \]_**<br>
#### Software
**_\[ [&uarr;](#top)_ / _[&darr;](#bottom) \]_**<br>
1. Download an operating System. I have tested it with Noobs » Raspbian [[More Infos]](#footnote-1).
2. Make sure that your system boots automaticly in Desktop (and logging in) (`sudo raspi-config`, 3 Boot options, B4 Desktop Autologin)
3. Download the installer
4. run it as root (`sudo bash /path/to/SmartMirrorGUI.sh`). **Important** is, that you use **sudo** and **bash**, not sh.
##### Configuration (python)
**_\[ [&uarr;](#top)_ / _[&darr;](#bottom) \]_**<br>
###### Weather widget
**_\[ [&uarr;](#top)_ / _[&darr;](#bottom) \]_**<br>
1. Create a weather widget on https://www.theweather.com/widget/.
2. Configure the widget like this:
[![demo](python3/examples/SmartMirror_weather_example.png)](python3/examples/SmartMirror_weather_example.png)<br>
It should look like this:
[![demo](python3/examples/SmartMirror_weather_example_config.png)](python3/examples/SmartMirror_weather_example_config.png)
3. Enter your email, chose An image below and copy the link to the generated image.
4. Paste it in the python script. under Ids\[1\] (Line 32, Column 45)
**Note:** If you want to show the snow line in meters (and not feet), just do the same configuration but in the end in the python script replace `https://theweather.com/...` with `https://daswetter.com/...` (its the german weather.com site).
##### Settings
**_\[ [&uarr;](#top)_ / _[&darr;](#bottom) \]_**<br>
In the python script line 23-38 are some settings;
```python
#SETTINGS#####################
##            [mode('BCM'/'BOARD'), B1, B2, B3, RED,    GRN,    w1-bus-pin (22),    jumper direction(GND:IO.FALLING/VCC:IO.RISING)]
gpio        = ['BCM',               2,  3,  4,  17,     27,     False,              IO.RISING]
##            [zoomed,  fullscreen, windowX,    windowY]
windowSizes = [False,   True,       0.75,       0.75]
##            [cartoonX,    cartoonY]
itemSizes   = [425*0.9,     596*0.9]
##            [version, weatherId,                                                                      tempSensorCpu,                              tempSensorIn,                       tempSensorOut,                      infoId]
Ids         = [1.0     'http://www.daswetter.com/wimages/foto99e83cda40fd2d3cd0a4d11485dffca2.png',    '/sys/class/thermal/thermal_zone0/temp',    '/opt/SM_GUI_py3.5-tk/testtemp1',   '/opt/SM_GUI_py3.5-tk/testtemp2',   'https://raw.githubusercontent.com/Schn33W0lf/RasPiSmartMirrorOS/master/res/test/headlines.txt']
##            [errors,  warnings,   infos,  debugInfos, logFeedback]
feedback    = [True,    True,       True,   False,      True]
##          = [time_placeholder,    info_placeholder]
texts       = ['Loading . . .',     'Here could be your advertisement! :P']
##            [allowshutdown]
fixes       = [True]
```
I don't recommend to change anything if you don't know what you're doing.
- gpio (don't change anything except w1 bus...: If you have connected 2 temperature sensors, write `True` if not `False`)
- windowSizes
  - zoomed: True: Ignoring the window size and use full size instead if it isn't in fullscreen.
  - fullscreen True: Starts in fullscreen.
  - windowX, Y: the sizes (0.75 = 75%) of the window if it isn't in fullscreen.
- itemSizes (dont change 425 and 596, these are the default values of the picture: 0.9 are the zoom (0.9 = 90%).)
- Ids
  - version Nr: Only change the nr (type = **float**!) if you have changed something and want to share.
  - weatherId: the image URL of the weather plugin generated by weather.com
  - tempSensorCpu: the 
  - tempSensorIn: the Id and output file (folder name (/sys/bus/w1/devices/XX-XXXXXXXXXXXX/) of the temperature sensor in the inside)
  - tempSensorOut: the Id and output file (folder name (/sys/bus/w1/devices/XX-XXXXXXXXXXXX/) of the temperature sensor in the outside)[They look equal, which one is the right?](#footnote-2)
  - infoId: the URL to the info sheet. You can seperate infos with a semicolon; and a line break. Semicolons, \n's, ... will be ignored.
- feedback: Do you want to see errors, warnings, infos, debug Infos in your console? Do you want to log the console? (Bool) If you're loggin everything it will be saved in /opt/SmartMirrorGUI(...)/logs/date-time-when-the-gui-was-started.log
- texts:
  - time_...: Placeholder instead of the time until they load.
  - info_...: Placeholder instead of the infos until they load.
- fixes: This option is to fix some known bugs. [Look here for details](#troubleshooting)
#### Hardware
**_\[ [&uarr;](#top)_ / _[&darr;](#bottom) \]_**<br>
Basicly, you need the RaspberryPi 3 with a µSD-card and a power supply (I suggest to use the official one (5V_, 2.5A) because of the voltage drop inside the Pi. More in the RPi Forum and [here](https://www.raspberrypi.org/documentation/hardware/raspberrypi/power/README.md)). Im using the RPi 3 B Rev 1.2<br>
Additionally you can solder a perfboard or just connect the status LED and switches with jumper wires. You can find circuit diagrams, plans and other infos [here](hardware)
## Future plans
**_\[ [&uarr;](#top)_ / _[&darr;](#bottom) \]_**
- [ ] I want to remote-control the py (eg for an audioplayer, ...)
- [ ] I want to use a kind of sites in my py script (like [pagepiling](https://alvarotrigo.com/pagePiling/) [\[GitHub\]](https://github.com/alvarotrigo/pagePiling.js)).
## Troubleshooting
**_\[ [&uarr;](#top)_ / _[&darr;](#bottom) \]_**
### Troubles with PIL:
If you get this Error Message if you run the script:
```python3
Traceback (most recent call last):
  File "/opt/SM_GUI_py3.5-tk/SM_GUI_v0.4.1.py", line 22, in <module>
    from PIL import ImageTk, Image
ImportError: cannot import name 'ImageTk'
```
Then, PIL isnt installed correctly. `sudo apt-get install python3-pil python3-pil.imagetk` fixed the problem for me ([source](https://stackoverflow.com/a/48170806)).
### Known GUI Bugs
1. In the past the PI shut down if you run the script by an .desktop file.<br>solution: run it by console
2. Maybe the PI still shut down.<br>solution: open the python script and comment 
# Footnotes
###### Footnote-1
```bash
uname -a:
Linux raspberrypi 4.14.30-v7+ #1102 SMP Mon Mar 26 16:45:49 BST 2018 armv7l GNU/Linux
```
###### Footnote-2
If you open `/sys/bus/w1/devices/XX-XXXXXXXXXXXX/w1-slave` you see (garbage and) the temperature in milli degrees.<br>
To view the temperature of a sensor, type `cat /sys/bus/w1/devices/XX-XXXXXXXXXXXX/w1-slave`.<br>
Change the temperature of one of the sensors. E.g. put it next to a light bulb **(Watch out and take care in the MAXIMUM HEAT RESISTANCE OF THE SENSOR!)**<br>
Then 'zap' with cat through all sensors and if one is warmer then the rest you have your first.<br>
Pro tip: Use paper or tape to mark the sensor ;P
# BOTTOM
_Just ignore that, i didnt found a better way to scroll to the end of the site..._<br>
[_**\[Top\]**_](#top)
