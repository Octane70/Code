#!/usr/bin/python
#Version 0.2

#0 ~300 : dry soil
#300~700 : humid soil
#700~950 : in water

from Adafruit_CharLCD import Adafruit_CharLCD
from subprocess import *
from time import sleep, strftime, time
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

#Moisture sensor min and max
moisture_min = 400
moisture_max = 600

#Watering times
a = datetime.datetime(100,1,1,7,00,00) #7:00:00
morning_on = a.time()

b = datetime.datetime(100,1,1,7,30,00) #7:30:00
morning_off = b.time()

c = datetime.datetime(100,1,1,19,00,00) #19:00:00
evening_on = c.time()

d = datetime.datetime(100,1,1,19,30,00) #19:30:00
evening_off = d.time()

# Function to read SPI data from MCP3008 chip
def ReadChannel(channel):
   adc = spi.xfer2([1,(8+channel)<<4,0])
   data = ((adc[1]&3) << 8) + adc[2]
   return data

# Irrigation relay ch1 on and off
def relay_ch1_on():
    gpio.output(12, True) #Relay ch1 on
def relay_ch1_off(): 
    gpio.output(12, False) #Relay ch1 off

# Irrigation relay ch2 on and off
def relay_ch2_on():
    gpio.output(16, True) #Relay ch2 on
def relay_ch2_off(): 
    gpio.output(16, False) #Relay ch2 off    
                
lcd = Adafruit_CharLCD()
lcd.begin(16, 1)
counter = 0

while True:
   
    #Import Humidity and Temperature from AdafruitDHT // 30 second refresh rate
    if counter % 30 == 0:
        humidity, temperature = Adafruit_DHT.read_retry(22, 4)
    #Import moisture from moisture sensor // 1 second refresh rate
    moisture = ReadChannel(2)
    #moisture controlled irrigation relay_ch1 
    if moisture >= moisture_min and moisture <= moisture_max:
       relay_ch1_on()
    else:
       relay_ch1_off()
    #Time controlled irrigation relay_ch2
    #Daytime and evening irrigation time
    if datetime.now >= morning_on and datetime.now <= morning_off:
       relay_ch2_on()
    elif datetime.now >= evening_on and datetime.now <= evening_off:
       relay_ch2_on()
    else:
       relay_ch2_off()
              
    lcd.clear()
    lcd.message(datetime.now().strftime('%H:%M:%S '))
    lcd.message ('T=%0.1fC\n' % temperature)
    lcd.message ('H=%0.1f%%' % humidity)
    lcd.message ('  M=%d' % moisture)
    counter += 1
    sleep(1)
    
#gpio.output(12, False) #purple // 1pwm
    
gpio.cleanup()	
