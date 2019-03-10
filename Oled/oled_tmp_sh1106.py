#!/usr/bin/env python3.2.3

import os
from time import sleep
#from render import canvas
from lib_sh1106 import sh1106
from PIL import ImageFont, ImageDraw, Image
from smbus import SMBus

i2cbus = SMBus(1)
oled = sh1106(i2cbus)

font = ImageFont.load_default()
draw = oled.canvas

os.system('sudo modprobe w1-gpio')
os.system('sudo modprobe w1-therm')

temp_sensor ='/sys/bus/w1/devices/28-00000593ba25/w1_slave'

def temp_raw():
    f = open(temp_sensor, 'r')
    lines = f.readlines() f.close()
    return lines

def read_temp():
    lines = temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        sleep(0.2) lines = temp_raw()
    temp_output = lines[1].find('t=')
    if temp_output != -1:
        temp_string = lines[1].strip()[temp_output+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_c#, temp_f 

# Load default font.
font = ImageFont.load_default()

# Nah, second thoughts ... Alternatively load another TTF font.
font = ImageFont.truetype('FreeSerif.ttf', 15)

while True:
    temperature = read_temp()
    draw.rectangle((0, 0, oled.width-1, oled.height-1), outline=20, fill=0)
    font = ImageFont.truetype('FreeSans.ttf', 32)
    draw.text((40, 20), (str(temperature)[:2])+chr(176) +'C ', font=font,fill=255)
    oled.display()
    print(temperature)
    
    




















