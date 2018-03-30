# HTML version of the SmartMirrorGUI
## Required Python modules:
- uinput                #to emulate key presses, mouse clicks, ...
- RPi.GPIO              #gpio library
- time
- sys                   #to check python version
- pyspectator.processor #to read CPU temp
## Software (required files):
+ SmartMirror
|-> pagepiling-files
|-> jquery.min.js       #or use a jquery script from an URL (google, ...)
|-> gpioQuery.py
|-> SmartMirrorSetup.sh
## Software (boot options, ...):
1. `sudo nano /boot/config.txt`, `display-rotate=3` #for vertical screen (270°)
2. `sudo nano /etc/lightdm/lightdm.conf`, anywhere in \[Seat:\*\] is a line (91 for me) with `xserver-command=X`. change it to `xserver-command=X 0dpms`. The display wont go off after that. (Maybe you have to reboot)
3. `crontab -e` add this line: `@reboot bash /path/to/SmartMirrorSetup.sh` to run this file after boot.

Also, you have to edit the raspi-config so you boot in Desktop without a password request.
