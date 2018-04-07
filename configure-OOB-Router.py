import getpass
import sys
import telnetlib
import pexpect
import time
import re
import os

HOST = raw_input("Enter RPi internal IP Address ")
PORT = raw_input("Enter the telnet port number you are using: ")
#user = raw_input("Enter your telnet username: ")
#password = getpass.getpass()
tn = telnetlib.Telnet(HOST, PORT, timeout = 1)
#tn.set_debuglevel(8)
print "Connecting to" + HOST + "on port " + PORT
tn.write("\r\n")


time.sleep(2)
PRIV = tn.read_eager()
if "#" in PRIV:
	print "Someone Forgot to Logout, Again!"
	tn.write("exit\n")
tn.write("\r\n")
tn.write("\r\n")
hostname = tn.read_until(">", timeout=1).split()[-1][:-1]

def ShowVer():
	time.sleep(1)
	print "The Hostname of device is: " + hostname
	tn.write("en\r\n")
	time.sleep(3)
	tn.read_until("#")
	print "Console Access gained"
	time.sleep(4)
	tn.write("terminal leng 0\n")
	print "Terminal Lenght 0"
	tn.read_until(hostname + "#")
	time.sleep(1)
	tn.write("show version\n")
	time.sleep(5)
	print "Show Version"
	#print tn.read_eager()
	tn.read_until(hostname + "#")
	time.sleep(1)
	global data
	data = tn.read_until(hostname + "#")
	print "Info collected"
	time.sleep(2)
	p = re.compile(data)
	time.sleep(1)
	for each_line in data.splitlines():
	   if "Processor" in each_line:
		  global sn
		  sn = each_line.split()[-1]
		  print "The serial number of this device is:" + sn
	datafile = sn
	time.sleep(2)
	try:
	   with open(datafile) as f:
	      print ("File found, executing commands...")
	      for each_line in f.read().splitlines():
	         command = str(each_line)
	         tn.write("config t\n")
	         tn.write(command + "\n")
	         print "Applying command:" + command
	         tn.read_eager()
	         tn.read_until("#")
	         time.sleep(1)
	         #output = tn.read_until("#")
	         #print output
	except IOError as e:
   	   print ("Error: %s not found." % datafile)
	tn.write("end\n")
	tn.write("exit\n")
	print "Exiting..."
	time.sleep(1)
	tn.write("\x1d")
	time.sleep(1)
	tn.write("quit\n")
	print "Quiting telnet>"
	time.sleep(1)
	#print data
	#tn.set_debuglevel(10)
	tn.close()

ShowVer()
