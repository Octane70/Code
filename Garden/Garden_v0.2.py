#!/usr/bin/python
#Version 0.2

from Adafruit_CharLCD import Adafruit_CharLCD
from subprocess import *
from time import sleep, strftime
from datetime import datetime
import sys
import Adafruit_DHT
import os
import spidev
import RPi.GPIO as gpio

# Open SPI bus
spi = spidev.SpiDev()
spi.open(0,0)

# Initiate gpio's for relay
gpio.setmode(gpio.BCM)
gpio.setup(12, gpio.OUT) # relay 1
gpio.setup(16, gpio.OUT) # relay 2

# Function to read SPI data from MCP3008 chip
def ReadChannel(channel):
   adc = spi.xfer2([1,(8+channel)<<4,0])
   data = ((adc[1]&3) << 8) + adc[2]
   return data

# water relay on and off
def water_relay_on():
    gpio.output(12, True) #Water relay on
def water_relay_off(): 
    gpio.output(12, False) #Water relay off
                
lcd = Adafruit_CharLCD()
lcd.begin(16, 1)
counter = 0

while True:
   
   # Import Humidity and Temperature from AdafruitDHT
    if counter % 30 == 0:
        humidity, temperature = Adafruit_DHT.read_retry(22, 4)
    # Import moisture from moisture sensor
    moisture = ReadChannel(2)
    if moisture >= 300:
       water_relay_off()
    #elif moisture == 750:
       #water_relay_off()
       
    lcd.clear()
    lcd.message(datetime.now().strftime('%H:%M:%S '))
    lcd.message ('T=%0.1fC\n' % temperature)
    lcd.message ('H=%0.1f%%' % humidity)
    lcd.message ('  M=%d' % moisture)
    counter += 1
    sleep(1)
    
#gpio.output(12, False) #purple // 1pwm
    
gpio.cleanup()	
