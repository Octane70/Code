import RPi.GPIO as gpio
import time
import sys
import tty
import termios


gpio.setmode(gpio.BOARD)
gpio.setup(16, gpio.OUT) #brown // 1ina
gpio.setup(18, gpio.OUT) #Yellow // 1inb
gpio.setup(32, gpio.OUT) #blue // 1pwm
gpio.setup(12, gpio.OUT) #purple // 2pwm
gpio.setup(15, gpio.OUT) #green // 2inb
gpio.setup(11, gpio.OUT) #orange // 2ina
gpio.setwarnings(False)
    
gpio.output(12, True) #purple // 1pwm
gpio.output(32, True) #blue // 2pwm
     
rh = gpio.PWM(12,120) #purple // 1pwm
rh.start(10) #start right motor at 50% duty cycle
#rh.ChangeDutyCycle(0)


lh = gpio.PWM(32,120) #blue // 2pwm
lh.start(10) #start left motor at 50% duty cycle
#lh.ChangeDutyCycle(0)

def reset_all(): #set all Motors to False
	gpio.output(16, False)
	gpio.output(18, False)
	gpio.output(15, False)
	gpio.output(11, False)
	   
def getch():
	fd = sys.stdin.fileno()
	old_settings = termios.tcgetattr(fd)
	try:
		tty.setraw(sys.stdin.fileno())
		ch = sys.stdin.read(1)
	finally:
		termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
	return ch	    
  
        
def forward():
    gpio.output(16, True) #Left Motor // 1ina 
    gpio.output(18, False)  #Left Motor // 1inb
    gpio.output(11, False)  #Right Motor // 2ina  
    gpio.output(15, True) #Right Motor // 2inb
    
def backward():
    gpio.output(16, False)  #Left Motor // 1ina  
    gpio.output(18, True) #Left Motor // 1inb 
    gpio.output(11, True) #Right Motor // 2ina   
    gpio.output(15, False)  #Right Motor // 2inb

def turn_left():
    gpio.output(16, False) #Left Motor // 1ina 
    gpio.output(18, True)  #Left Motor // 1inb 
    gpio.output(11, False) #Right Motor // 2ina 
    gpio.output(15, True)  #Right Motor // 2inb     

def turn_right():
    gpio.output(16, True)  #Left Motor // 1ina 
    gpio.output(18, False) #Left Motor // 1inb  
    gpio.output(11, True)  #Right Motor // 2ina
    gpio.output(15, False) #Right Motor //  2inb 

def pivot_left():
    gpio.output(16, False) #Left Motor // 1ina	 
    gpio.output(18, False) #Left Motor // 1inb
    gpio.output(11, False) #Right Motor // 2ina 
    gpio.output(15, True)  #Right Motor // 2inb

def pivot_right():
    gpio.output(16, True)  #Left Motor // 1ina 
    gpio.output(18, False) #Left Motor // 1inb  
    gpio.output(11, False) #Right Motor // 2ina
    gpio.output(15, False) #Right Motor // 2inb
    
def all_stop():
    gpio.output(16, False) #Left Motor // 1ina 
    gpio.output(18, False) #Left Motor // 1inb  
    gpio.output(11, False) #Right Motor // 2ina
    gpio.output(15, False) #Right Motor // 2inb    
    
print ("w: for forward")
print ("s: for backward") 
print ("d: for right")
print ("a: for left")
print ("e: pivot right") 
print ("q: pivot left")
print ("f: all stop")
print ("x: for exit")          

while True:
	char = getch()
	
	if(char == "w"):
	    forward()
	    lh.ChangeDutyCycle(25)
	    rh.ChangeDutyCycle(25)

	if(char == "s"):
	    backward()
	    lh.ChangeDutyCycle(25)
	    rh.ChangeDutyCycle(25)
	
	if(char == "a"):
	    turn_left()
	    lh.ChangeDutyCycle(20)
	    rh.ChangeDutyCycle(20)
	
	if(char == "d"):
	    turn_right()
	    lh.ChangeDutyCycle(20)
	    rh.ChangeDutyCycle(20)
	
	if(char == "q"):
	    pivot_left()
	    lh.ChangeDutyCycle(0)
	    rh.ChangeDutyCycle(15)
	
	if(char == "e"):
	    pivot_right()
	    lh.ChangeDutyCycle(15)
	    rh.ChangeDutyCycle(0)
	    
	if(char == "f"):
	    all_stop()
	    lh.stop
	    rh.stop
	
	if(char == "x"):
	    print("PROGRAM ENDED")
	    break
	    lh.ChangeDutyCycle(0)
	    rh.ChanegDutyCycle(0)
	    
	char = ""    	 


gpio.cleanup()
