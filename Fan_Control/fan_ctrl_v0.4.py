#!/usr/bin/env python3

import os
from time import sleep
import signal
import sys
import RPi.GPIO as GPIO
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import subprocess

fan_pin = 18      # The pin ID, edit here to change it
maxTMP = 25   # The maximum temperature in Celsius to turn on the fan
minTMP = 30   # The minimum temperature in Celsius to turn off the fan
fanSPD = 100   # Speed of Fan
PWM_Freq = 25 # [Hz] Change this value if fan has strange behavior

# Raspberry Pi pin configuration:
RST = 25     # on the PiOLED this pin isnt used
# Note the following are only used with SPI:
DC = 24
SPI_PORT = 0
SPI_DEVICE = 0

# 128x64 display with hardware SPI:
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, dc=DC, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=8000000))

# Initialize library.
disp.begin()

# Clear display.
disp.clear()
disp.display()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
image = Image.new('1', (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0,0,width,height), outline=0, fill=0)

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
        # Draw a black filled box to clear the image.
        draw.rectangle((0,0,width,height), outline=0, fill=0)
        getTEMP()
        temperature = read_temp()
        draw.rectangle((0, 0, disp.width-1, disp.height-1), outline=20, fill=0)
        font = ImageFont.truetype('FreeSans.ttf', 35)
        draw.text((25, 12), (str(temperature)[:2])+chr(176) +'C ', font=font,fill=255)
        print(read_temp())
        # Display image.
        disp.image(image)
        disp.display()   
        sleep(.1)
      
except KeyboardInterrupt: # trap a CTRL+C keyboard interrupt
    print("Kill Script")
    GPIO.cleanup() # resets all GPIO ports used by this program
    sys.exit()
