#Author: Joshua Brent Collins 9/24/2011
#version: 1.1
#Description: Unix based tty communication program 




import os
import io
import termios
import sys

try:
#list devices
	print 'Serial Interface List:\r\n'
	os.system('dmesg | grep tty')
	print 'Enter COM port to connect to. \r\n'
	com = sys.stdin.readline()
#open port for reading and writng retun descriptor
	port = os.open( '/dev/ttyUSB'+com, os.O_RDWR | os.O_NONBLOCK)
        

#get termios settings
	sbaud=termios.tcgetattr(port)
#set new baud rate now
	sbaud[4]=termios.B9600
	sbaud[5]=termios.B9600
	termios.tcsetattr(port,termios.TCSAFLUSH,sbaud)
#print new settings
	print termios.tcgetattr(port)

#input loop
	while (1==1):	
	

		
		print 'Please enter command(exit to break):\r\n'
		command=sys.stdin.readline()
		if command=='exit':
			break
		else:
			os.write(port,command)
	
			print command


except:
	print 'Error occured unable to continue exiting.'	



