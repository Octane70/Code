import RPi.GPIO as GPIO
import sys
import time
import subprocess

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(12, GPIO.OUT) # white // 1pwm
GPIO.setup(13, GPIO.OUT) # grey // 2pwm

lh = GPIO.PWM(12,120) #white // 1pwm
lh.start(0) #start left motor at 0% duty cycle

rh = GPIO.PWM(13,120) #grey // 2pwm
rh.start(0) #start right motor at 0% duty cycle

#set all pwm to False
GPIO.output(12, False)
GPIO.output(13, False)

pwm_lm = 100
pwm_rm = 100

#pwm control
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
    


