# MyFirstProject


-------
show-serial-number.py
-------
Point the script to an IP address of a Raspberry PI running SER2NET on port 4001 which is connected to the console of a Cisco Router/Switch with no config.
The script will read the Serial Number of the device.

-------
ser2net_project.py
-------
In addition the the show-serial-number.py script, this script will look for a text file named after the Serial Number of the device (e.g. ABCDE12345) and will push the commands from the file to the Router/Switch.
See example file ABCDE12345
