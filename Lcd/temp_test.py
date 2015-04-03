#!/usr/bin/python

from Adafruit_CharLCD import Adafruit_CharLCD
from subprocess import *
from time import sleep, strftime
from datetime import datetime
import sys
import Adafruit_DHT

lcd = Adafruit_CharLCD()

lcd.begin(16, 1)

# Import Humidity and Temperature from (DHT22, gpio pin 4)
humidity, temperature = Adafruit_DHT.read_retry(22, 4)

while 1:
    lcd.clear()
    lcd.message(datetime.now().strftime('%H:%M:%S '))
    lcd.message ('T=%0.1fC\n' % temperature)
    lcd.message ('H=%0.1f%%' % humidity)
    sleep(1)
