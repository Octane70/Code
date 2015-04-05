import sys
import RPi.GPIO as gpio
import time
import tty
import termios

# Initiate gpio's for relay
gpio.setmode(gpio.BCM)
gpio.setup(12, gpio.OUT) # relay 1
gpio.setup(16, gpio.OUT) # relay 2
gpio.setwarnings(False)

#set all Motors to False
gpio.output(12, False)
gpio.output(16, False)

def getch():
	fd = sys.stdin.fileno()
	old_settings = termios.tcgetattr(fd)
	try:
		tty.setraw(sys.stdin.fileno())
		ch = sys.stdin.read(1)
	finally:
		termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
	return ch


# Relay 1
def relay_1():
    gpio.output(12, True) #Set relay 1 to true
    
# Define Right Motor Forward
def relay_2():
    gpio.output(16, True) #Set relay 2 to true 
    

while True:
	char = getch()
		
	if(char == "1"):
	    relay_1()
	    print ("Relay 1 on")
	
	elif(char == "2"):
	    relay_2()
	    print ("Relay 2 on")

	elif(char == "x"):
	    print("PROGRAM ENDED")
            gpio.output(12, False) #Set relay 1 to false
            gpio.output(16, False) #Set relay 2 to false
	    break

	char = ""
	    
gpio.cleanup()
	    
