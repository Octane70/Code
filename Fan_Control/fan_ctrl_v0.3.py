#!/usr/bin/env python3

import os
from time import sleep
import signal
import sys
import RPi.GPIO as GPIO

fan_pin = 18      # The pin ID, edit here to change it
maxTMP = 25   # The maximum temperature in Celsius to turn on the fan
minTMP = 30   # The minimum temperature in Celsius to turn off the fan
fanSPD = 75   # Speed of Fan
PWM_Freq = 25 # [Hz] Change this value if fan has strange behavior

#Case Temperature Sensor
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

temp_sensor = '/sys/bus/w1/devices/28-0000060e26f0/w1_slave'

GPIO.setmode(GPIO.BCM)
GPIO.setup(fan_pin, GPIO.OUT)
GPIO.setwarnings(False)
fan=GPIO.PWM(fan_pin,PWM_Freq)
fan.start(0)

# Functions for Case temp sensor
def temp_raw():
    f = open(temp_sensor, 'r')
    lines = f.readlines()
    f.close()
    return lines

def read_temp():
    lines = temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = temp_raw()
    temp_output = lines[1].find('t=')
    if temp_output != -1:
        temp_string = lines[1].strip()[temp_output+2:]
        temp_c = float(temp_string) / 1000.0
        return temp_c 

def getTEMP():
    CPU_temp = float(read_temp())
    if CPU_temp>maxTMP:
        fan.ChangeDutyCycle(fanSPD)
    else:
        fan.ChangeDutyCycle(0)
    return()

try:
    while True:
        getTEMP()
        print('Temp= %0.1fC' % read_temp())    
    sleep(5) # Read the temperature every 5 sec, increase or decrease this limit if you want
      
except KeyboardInterrupt: # trap a CTRL+C keyboard interrupt
    print("Kill Script")
    GPIO.cleanup() # resets all GPIO ports used by this program
    sys.exit()
