import RPi.GPIO as gpio
import time
import sys
import tty
import Tkinter as tk
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
rh.start(0) #start right motor at 50% duty cycle
rh.ChangeDutyCycle(0)


lh = gpio.PWM(32,120) #blue // 2pwm
lh.start(0) #start left motor at 50% duty cycle
lh.ChangeDutyCycle(0)

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
    gpio.output(16, False)   
    gpio.output(18, True)
    gpio.output(11, True)    
    gpio.output(15, False)
    
def backwards():
    gpio.output(16, True)    
    gpio.output(18, False)   
    gpio.output(11, False)    
    gpio.output(15, True)

def turn_left():
    gpio.output(16, False)	 
    gpio.output(18, True)    
    gpio.output(11, False)  
    gpio.output(15, True)       

def turn_right():
    gpio.output(16, True)	 
    gpio.output(18, False)   
    gpio.output(11, True)  
    gpio.output(15, False)   

def pivot_left():
    gpio.output(16, False)	 
    gpio.output(18, True) 
    gpio.output(11, False)  
    gpio.output(15, True)  

def pivot_right():
    gpio.output(16, True)	 
    gpio.output(18, False)   
    gpio.output(11, True)  
    gpio.output(15, False)
    
print ("w: for forward")
print ("s: for backwards") 
print ("d: for right")
print ("a: for left")
print ("r: pivot right") 
print ("w: pivot left")
print ("x: for exit") 

def key_input(event):
	init()
	print 'Key:', event.char
	key_press = event.char         
	
	if key_press.lower() == 'w':
	    forward()
	    lh.ChangeDutyCycle(75)
	    rh.ChangeDutyCycle(75)

	elif key_press.lower() == 's':
	    backwards()
	    lh.ChangeDutyCycle(75)
	    rh.ChangeDutyCycle(75)
	
	elif key_press.lower() == 'a':
	    turn_left()
	    lh.ChangeDutyCycle(75)
	    rh.ChangeDutyCycle(75)
	
	elif key_press.lower() == 'd':
	    turn_right()
	    lh.ChangeDutyCycle(75)
	    rh.ChangeDutyCycle(75)
	
	elif key_press.lower() == 'q':
	    pivot_left()
	    rh.ChangeDutyCycle(75)
	
	elif key_press.lower() == 'e':
	    pivot_right()
	    lh.ChangeDutyCycle(75)
	    
while True:
	char = getch()
	
	if (char == "x"):
	    print("PROGRAM ENDED")
	    break
	    lh.ChangeDutyCycle(0)
	    rh.ChanegDutyCycle(0)
	    
	char = ""    
	        	 
command = tk.Tk()
command.bind('<KeyPress>', key_input)
command.mainloop()
gpio.cleanup()
