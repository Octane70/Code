#!/usr/bin/env python3

import os
from time import sleep
import signal
import sys
import RPi.GPIO as GPIO

pin = 18 # The pin ID, edit here to change it
maxTMP = 30 # The maximum temperature in Celsius after which we trigger the fan

#Case Temperature Sensor
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

temp_sensor = '/sys/bus/w1/devices/28-0000060e26f0/w1_slave'

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.setwarnings(False)
    return()

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

def fanON():
    setPin(True)
    return()

def fanOFF():
    setPin(False)
    return()

def getTEMP():
    CPU_temp = float(read_temp())
    if CPU_temp>maxTMP:
        fanON()
    else:
        fanOFF()
    return()

def setPin(mode): # A little redundant function but useful if you want to add logging
    GPIO.output(pin, mode)
    return()

try:
    setup() 
    while True:
        getTEMP()
        print('Temp= %0.1fC' % read_temp())    
    sleep(5) # Read the temperature every 5 sec, increase or decrease this limit if you want
    
    
except KeyboardInterrupt: # trap a CTRL+C keyboard interrupt 
    GPIO.cleanup() # resets all GPIO ports used by this program
