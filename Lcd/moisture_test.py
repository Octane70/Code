#!/usr/bin/python

# Monitor two soil sensors on MCP3008, ch 2 and 3
# (pin 3 and 4)

import spidev
import time
import os

# Open SPI bus
spi = spidev.SpiDev()
spi.open(0,0)

# Function to read SPI data from MCP3008 chip
def ReadChannel(channel):
   adc = spi.xfer2([1,(8+channel)<<4,0])
   data = ((adc[1]&3) << 8) + adc[2]
   return data


# Main loop - read raw data and display
while True:
   soilOne = ReadChannel(2)
   #soilTwo = ReadChannel(3)
   
   # Output
   #print "Soil1=",soilOne," : Soil2=",soilTwo
   print "Soil1=",soilOne,
   
   time.sleep(0.01)
