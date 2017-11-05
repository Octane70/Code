import RPi.GPIO as GPIO
import sys
#sys.path.insert(0, "/home/pi/rouge/bluepad")
#from bluepad.btcomm import BluetoothServer
#from signal import pause
import time
import subprocess

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(23, GPIO.OUT) # purple // 1in
GPIO.setup(24, GPIO.OUT) # blue // 2in
#GPIO.setup(12, GPIO.OUT) # white // 1pwm
#GPIO.setup(18, GPIO.OUT) # grey // 2pwm
GPIO.setup(22, GPIO.OUT) # green // 3in
GPIO.setup(27, GPIO.OUT) # yellow // 4in

#rh = GPIO.PWM(18,120) #white // 1pwm
#rh.start(10) #start right motor at 50% duty cycle
# rh.ChangeDutyCycle(0)

#lh = GPIO.PWM(12,120) #grey // 2pwm
#lh.start(10) #start left motor at 50% duty cycle
# lh.ChangeDutyCycle(0)

#set all Motors to False
GPIO.output(23, False)
GPIO.output(24, False)
GPIO.output(27, False)
GPIO.output(22, False)

print ("rouge2 manual")
    
#stop all motors
def Stop():
   #GPIO.output(12, False)
   #GPIO.output(18, False)
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


