import sys
#sys.path.append("/home/pi/code/Maestro/modules")
#import maestro
import RPi.GPIO as gpio
import time
import tty
import termios

#servo = maestro.Controller()

gpio.setmode(gpio.BCM)
gpio.setup(22, gpio.OUT) # button_a
gpio.setup(23, gpio.OUT) # button_b
gpio.setup(24, gpio.OUT) # button_c

def getch():
	fd = sys.stdin.fileno()
	old_settings = termios.tcgetattr(fd)
	try:
		tty.setraw(sys.stdin.fileno())
		ch = sys.stdin.read(1)
	finally:
		termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
	return ch

def button_a():
    gpio.output(22, True) #motor_a on
    print ("motor_a on")
    #else:
    #gpio.output(22, False) #motor_a off
    #print ("motor_3 off")
    
def button_b():
    gpio.output(23, True) #motor_b on
    print ("motor_4a on")
       # else:
         #gpio.output(23, False)  #motor_b off
         #print ("motor_4a off")

def button_c():
    gpio.output(24, True) #motor_c on
    print ("motor_4b on")
    #else:
    #gpio.output(24, False)  #motor_c off
    #print ("motor_4b off")
  
print ("a: for motor_3")
print ("b: for motor_4a")
print ("c: for motor_4b")        

while True:
	char = getch()
		
	if(char == "a"):
	    button_a()
	    print ("button_a")
	
	if(char == "b"):
	    button_b()
	    print ("button_b")
	    
	if(char == "c"):
	    button_c()
	    print ("button_c")	    
		
	if(char == "x"):
	    print("PROGRAM ENDED")
	    gpio.output(22, False) #button_a off
	    gpio.output(23, False) #button_4a off
	    gpio.output(24, False) #button_4b off
	    break
	    
	char = ""    	 


gpio.cleanup()

             
