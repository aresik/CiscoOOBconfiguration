# Cisco Out of Band (or Out of Box) configuration


-------
show-serial-number.py
-------
Point the script to an IP address of a terminal server connected to a Cisco Router with no config.
The script will read the Serial Number of the device.
Tested on Cisco 800 routers.

-------
configure-OOB-Router.py
-------
In addition the the show-serial-number.py script, this script will look for a text file named after the Serial Number of the device (e.g. ABCDE12345) and will push the commands from the file to the Router.
See example file ABCDE12345.

