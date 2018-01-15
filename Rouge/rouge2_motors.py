import RPi.GPIO as GPIO
import sys
import time
import subprocess

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(23, GPIO.OUT) # purple // 1in
GPIO.setup(24, GPIO.OUT) # blue // 2in
GPIO.setup(12, GPIO.OUT) # white // 1pwm
GPIO.setup(13, GPIO.OUT) # grey // 2pwm
GPIO.setup(22, GPIO.OUT) # green // 3in
GPIO.setup(27, GPIO.OUT) # yellow // 4in

lh = GPIO.PWM(12,120) #white // 1pwm
lh.start(0) #start left motor at 0% duty cycle

rh = GPIO.PWM(13,120) #grey // 2pwm
rh.start(0) #start right motor at 0% duty cycle

#set all Motors to False
GPIO.output(23, False)
GPIO.output(24, False)
GPIO.output(12, False)
GPIO.output(13, False)
GPIO.output(27, False)
GPIO.output(22, False)

print ("rouge2 motors")

pwm_lm = 100
pwm_rm = 100

#Motor speed control
def lm_pwm(command):
    global pwm_lm
    lh.ChangeDutyCycle(pwm_lm)
    if command == "13":
       if (pwm_lm < 100):
           pwm_lm = pwm_lm + 1
           print (pwm_lm)
       else:
            return	
    elif command == "14":
       if (pwm_lm > 0):
           pwm_lm = pwm_lm - 1
           print (pwm_lm)
       else:
            return

def rm_pwm(command):
    global pwm_rm
    rh.ChangeDutyCycle(pwm_rm)
    if command == "15":
       if (pwm_rm < 100):
           pwm_rm = pwm_rm + 1
           print (pwm_rm)
       else:
            return
    elif command == "16":
       if (pwm_rm > 0):
           pwm_rm = pwm_rm - 1
           print (pwm_rm)
       else:
            return

#stop all motors
def Stop():
   #GPIO.output(12, False)
   #GPIO.output(13, False)
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


