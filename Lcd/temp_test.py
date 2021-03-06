#!/usr/bin/python

from Adafruit_CharLCD import Adafruit_CharLCD
from subprocess import *
from time import sleep, strftime
from datetime import datetime
import sys
import Adafruit_DHT
import os
import spidev

# Open SPI bus
spi = spidev.SpiDev()
spi.open(0,0)

# Function to read SPI data from MCP3008 chip
def ReadChannel(channel):
   adc = spi.xfer2([1,(8+channel)<<4,0])
   data = ((adc[1]&3) << 8) + adc[2]
   return data

lcd = Adafruit_CharLCD()
moisture = ReadChannel(2)

lcd.begin(16, 1)

# Import Humidity and Temperature from (DHT22, gpio pin 4)
humidity, temperature = Adafruit_DHT.read_retry(22, 4)

while 1:
    lcd.clear()
    lcd.message(datetime.now().strftime('%H:%M:%S '))
    lcd.message ('T=%0.1fC\n' % temperature)
    lcd.message ('H=%0.1f%%' % humidity)
    lcd.message ('  M=%d' % moisture)
    sleep(1)
