import RPi.GPIO as GPIO
import sys
import time
import subprocess

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(23, GPIO.OUT) # purple // 1in
GPIO.setup(24, GPIO.OUT) # blue // 2in
GPIO.setup(22, GPIO.OUT) # green // 3in
GPIO.setup(27, GPIO.OUT) # yellow // 4in

#set all Motors to False
GPIO.output(23, False)
GPIO.output(24, False)
GPIO.output(27, False)
GPIO.output(22, False)

print ("rouge2 motors")

#stop all motors
def Stop():
    GPIO.output(23, False)
    GPIO.output(24, False)
    GPIO.output(27, False)
    GPIO.output(22, False)
    print ("stop")
    
#dpad up commands
def Forward():
    GPIO.output(23, True) #Left Motor // 1ina 
    GPIO.output(24, False)  #Left Motor // 1inb
    GPIO.output(27, False)  #Right Motor // 2ina  
    GPIO.output(22, True) #Right Motor // 2inb
    print("forward")
        
#dpad down commands
def Reverse():
    GPIO.output(23, False)  #Left Motor // 1ina  
    GPIO.output(24, True) #Left Motor // 1inb
    GPIO.output(27, True) #Right Motor // 2ina   
    GPIO.output(22, False)  #Right Motor // 2inb
    print("reverse")
        
#dpad left commands
def Left():
    GPIO.output(23, False)  #Left Motor // 1ina  
    GPIO.output(24, True) #Left Motor // 1inb
    GPIO.output(27, False)  #Right Motor // 2ina  
    GPIO.output(22, True) #Right Motor // 2inb	
    print("left")
        
#dpad right commands
def Right():
    GPIO.output(23, True) #Left Motor // 1ina 
    GPIO.output(24, False)  #Left Motor // 1inb
    GPIO.output(27, True) #Right Motor // 2ina   
    GPIO.output(22, False)  #Right Motor // 2inb
    print("right")    


