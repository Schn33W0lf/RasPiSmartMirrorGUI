#!/bin/bash
function pythonLoadModules {
	python3 -c "import $1"
	if [ $? == 0 ]; then
		echo "          Installed:     $1"
	elif [ $? == 1 ]; then
		echo "          Not Installed: $1"
		pip3 install $1
	else
		echo "          Error:         $1"
	fi
}
versionSelected=1
arrowOpt1L="==>"
arrowOpt1R="<=="
arrowOpt2L="   "
arrowOpt2R="   "
arrowOpt3L="   "
arrowOpt3R="   "
while true; do
versionOpt1="
    ##############################
    #                            #
$arrowOpt1L #      SM Version 0.1.3      # $arrowOpt1R
    #                            #
    ##############################"
versionOpt2="
    ##############################
    #                            #
$arrowOpt2L #            About           # $arrowOpt2R
    #                            #
    ##############################"
versionOpt3="
    ##############################
    #                            #
$arrowOpt3L #            Exit            # $arrowOpt3R
    #                            #
    ##############################"
	echo -e "\0033\0143#SETUP#SM#CHOOSE#VERSION########################################################
     ##### ##### ##### #   # ####    ##### #   #
    #     #       #   #   # #   #   #     ## ##
   ##### #####   #   #   # ####    ##### # # #
      # #       #   #   # #           # #   #
 ##### #####   #   ##### #       ##### #   #
##################################################################by#Schn33W0lf#
              $versionOpt1$versionOpt2$versionOpt3$versionOpt4"
	read -s -n 1 -p "Navigate with the Numpad (8 up, 2 down, 5 select)" versionSelect
	if [ $versionSelect -eq 8 ]; then
		if [ $versionSelected -eq 2 ]; then
			versionSelected=1
			arrowOpt1L="==>"
			arrowOpt1R="<=="
			arrowOpt2L="   "
			arrowOpt2R="   "
			arrowOpt3L="   "
			arrowOpt3R="   "
		elif [ $versionSelected -eq 3 ]; then
			versionSelected=2
			arrowOpt1L="   "
			arrowOpt1R="   "
			arrowOpt2L="==>"
			arrowOpt2R="<=="
			arrowOpt3L="   "
			arrowOpt3R="   "
		fi
	elif [ $versionSelect -eq 2 ]; then
		if [ $versionSelected -eq 2 ]; then
			versionSelected=3
			arrowOpt1L="   "
			arrowOpt1R="   "
			arrowOpt2L="   "
			arrowOpt2R="   "
			arrowOpt3L="==>"
			arrowOpt3R="<=="
		elif [ $versionSelected -eq 1 ]; then
			versionSelected=2
			arrowOpt1L="   "
			arrowOpt1R="   "
			arrowOpt2L="==>"
			arrowOpt2R="<=="
			arrowOpt3L="   "
			arrowOpt3R="   "
		fi
	elif [ $versionSelect -eq 5 ]; then
		if [ $versionSelected -eq 1 ]; then
			pythonSource="https://gist.githubusercontent.com/Schn33W0lf/3953d3574ea75bb820fd020c888a8732/raw/9337a326b564677bc6ddd2d8223176362267c8bf/SM_GUI_v0.3.1.minimal.py"
		elif [ $versionSelected -eq 2 ]; then
			echo -e "\0033\0143#SETUP#SM#ABOUT#################################################################
     ##### ##### ##### #   # ####    ##### #   #   ##### ####  ##### #   # #####
    #     #       #   #   # #   #   #     ## ##   #   # #   # #   # #   #   #
   ##### #####   #   #   # ####    ##### # # #   ##### ####  #   # #   #   #
      # #       #   #   # #           # #   #   #   # #   # #   # #   #   #
 ##### #####   #   ##### #       ##### #   #   #   # ####  ##### #####   #
##################################################################by#Schn33W0lf#

[INFO] Required Bash tools:
       read
       wget
       mkdir
       crontab
       sed
[INFO] Destination folder:
       '/opt/SM_GUI_v0.3.1-py3.5-tk'
[INFO] File sources:
###### Python 3
'https://gist.githubusercontent.com/Schn33W0lf/3953d3574ea75bb820fd020c888a8732/raw/9337a326b564677bc6ddd2d8223176362267c8bf/SM_GUI_v0.3.1.minimal.py'
###### Folder (GitHub)

		fi
		break
	fi
done
if [ $versionSelected -eq 1 ]; then
	echo -e "\0033\0143#SETUP#SM#v#0.1.3###############################################################
     ##### ##### ##### #   # ####    ##### #   #         #####    #   #####
    #     #       #   #   # #   #   #     ## ##         #   #   ##       #
   ##### #####   #   #   # ####    ##### # # #   #   # # # #    #   #####
      # #       #   #   # #           # #   #    # #  #   #    #       #
 ##### #####   #   ##### #       ##### #   #     #   ##### #  # # #####
##################################################################by#Schn33W0lf#
[CREATE] '/opt/SM_GUI_v0.3.1-py3.5-tk'
         SmartMirror directory"
	mkdir /opt/SM_GUI_v0.3.1-py3.5-tk
	echo "
[LOAD]   '$pythonSource'
[CREATE] 'python3 /opt/SM_GUI_v0.3.1-py3.5-tk/SM_GUI_v0.3.1.minimal.py'
         '$pythonSource'
	 Python script"
	wget https://gist.githubusercontent.com/Schn33W0lf/3953d3574ea75bb820fd020c888a8732/raw/9337a326b564677bc6ddd2d8223176362267c8bf/SM_GUI_v0.3.1.minimal.py --output-document=/opt/SM_GUI_v0.3.1-py3.5-tk/SM_GUI_v0.3.1.minimal.py
	echo "
[CREATE] '/opt/SM_GUI_v0.3.1-py3.5-tk/SMstart.sh'
         'python3 /opt/SM_GUI_v0.3.1-py3.5-tk/SM_GUI_v0.3.1.py
	  sudo shutdown 0'
	  start shell script"
	echo -e "python3 /opt/SM_GUI_v0.3.1-py3.5-tk/SM_GUI_v0.3.1.py\nsudo shutdown 0\n" >> /opt/SM_GUI_v0.3.1-py3.5-tk/SMstart.sh
	echo "
[CREATE] /opt/SM_GUI_v0.3.1-py3.5-tk/SM_v0.3.1.crontab"
	echo "@reboot 'sh /opt/SM_GUI_v0.3.1-py3.5-tk/SMstart.sh" >> /opt/SM_GUI_v0.3.1-py3.5-tk/SM_v0.3.1.crontab
	echo "
[USE]    crontab -u $USER /opt/SM_GUI_v0.3.1-py3.5-tk/SM_v0.3.1.crontab
         '@reboot 'sh /opt/SM_GUI_v0.3.1-py3.5-tk/SMstart.sh'
         Load SMstart.sh after boot"
	crontab -u $USER /opt/SM_GUI_v0.3.1-py3.5-tk/SM_v0.3.1.crontab
	echo "
[EDIT]   /etc/lightdm/lightdm.conf
         Line 91
         'xserver-command=X'
         '#SM_0.1.3# xserver-command=X
          xserver-command=X -s 0 dpms'
         Prevent display timeout"
	sed -i 's/xserver-command=X/xserver-command=X -s 0 dpms/g' /etc/lightdm/lightdm.conf
	echo "
[EDIT]   /boot/config.txt
         'display_rotate=3
          # default     =0'
         Rotate the display by 270°"
	configOutput=$(cat /boot/config.txt)
	configAdd='\n# EDIT for SmartMirrorGUI\ndisplay_rotate=3\ndefault      =0\n'
	configInput=$configOutput$configAdd
	sed -i 's/$configOutput/$configInput/g' /boot/config.txt
	echo "
[LOAD]   Python 3"
	if [ $(python3 -c "import sys;print(sys.version.split()[0])") != "bash: python3: command not found" ]; then
		echo "         Installed."
	else
		echo "         Not installed."
		apt-get install python3
	fi
	echo " 
[LOAD]   python modules:"
	pyMod="Error"
	pythonLoadModules sys
	pythonLoadModules time
	pythonLoadModules base64
	pythonLoadModules io
	pythonLoadModules random
	pythonLoadModules requests
	pythonLoadModules PIL
	pythonLoadModules PIL.Image
	pythonLoadModules pyspectator.processor
	pythonLoadModules RPi.GPIO
	pythonLoadModules urllib.request
	pythonLoadModules tkinter
	echo "
[INFO]   Finished. Reboot to start the SM_GUI"
elif [ $versionSelected -eq 3 ]; then
	echo -e "\0033\0143exiting . . ."
	sleep 1
	echo -e "\0033\0143"

fi