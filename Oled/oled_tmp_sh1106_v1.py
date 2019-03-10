import time
import os
from luma.core.interface.serial import i2c, spi
from luma.core.render import canvas
from luma.oled.device import ssd1306, ssd1309, ssd1325, ssd1331, sh1106

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import subprocess

#spi device
serial = spi(device=0, port=0) 
disp = ssd1306(serial)

# Initialize library.
#disp.begin()

# Clear display.
#disp.clear()
#disp.display()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
image = Image.new('1', (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0,0,width,height), outline=0, fill=0)

os.system('sudo modprobe w1-gpio')
os.system('sudo modprobe w1-therm')

temp_sensor ='/sys/bus/w1/devices/28-0000060e26f0/w1_slave'

def temp_raw():
    f = open(temp_sensor, 'r')
    lines = f.readlines()
    f.close()
    return lines

def read_temp():
    lines = temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        sleep(0.2)
        lines = temp_raw()
    temp_output = lines[1].find('t=')
    if temp_output != -1:
        temp_string = lines[1].strip()[temp_output+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_c#, temp_f 

while True:

    # Draw a black filled box to clear the image.
    draw.rectangle((0,0,width,height), outline=0, fill=0)
    
    temperature = read_temp()
    draw.rectangle((0, 0, disp.width-1, disp.height-1), outline=20, fill=0)
    font = ImageFont.truetype('FreeSans.ttf', 35)
    draw.text((25, 12), (str(temperature)[:2])+chr(176) +'C ', font=font,fill=255)

    # Display image.
    #disp.image(image)
    #disp.display()
    time.sleep(.1)
