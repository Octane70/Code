from bluedot import BlueDot
import RPi.GPIO as GPIO
from signal import pause
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

def dpad(pos):
    if pos.top:
        GPIO.output(23, True) #Left Motor // 1ina 
        GPIO.output(24, False)  #Left Motor // 1inb
        GPIO.output(27, False)  #Right Motor // 2ina  
        GPIO.output(22, True) #Right Motor // 2inb
        print("forward")
    elif pos.bottom:
        GPIO.output(23, False)  #Left Motor // 1ina  
        GPIO.output(24, True) #Left Motor // 1inb
        GPIO.output(27, True) #Right Motor // 2ina   
        GPIO.output(22, False)  #Right Motor // 2inb
        print("reverse")
    elif pos.left:
        GPIO.output(23, False)  #Left Motor // 1ina  
        GPIO.output(24, True) #Left Motor // 1inb
        GPIO.output(27, False)  #Right Motor // 2ina  
        GPIO.output(22, True) #Right Motor // 2inb	
        print("left")
    elif pos.right:
        GPIO.output(23, True) #Left Motor // 1ina 
        GPIO.output(24, False)  #Left Motor // 1inb
        GPIO.output(27, True) #Right Motor // 2ina   
        GPIO.output(22, False)  #Right Motor // 2inb
        print("right")

def stop(pos):
       #turn off the motors
       #GPIO.output(12, False)
       #GPIO.output(18, False)
       GPIO.output(23, False)
       GPIO.output(24, False)
       GPIO.output(27, False)
       GPIO.output(22, False)
       
bd = BlueDot()
bd.when_pressed = dpad
bd.when_moved = dpad
bd.when_released = stop

pause()

GPIO.cleanup()
