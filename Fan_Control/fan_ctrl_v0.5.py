#!/usr/bin/env python3

import os
from time import sleep
import signal
import sys
import subprocess
import RPi.GPIO as GPIO
from tkinter import *
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

fan_pin = 18   # Fan Pin
maxTMP = 29  # Maximum Temp in Celicius to turn the fan on
minTMP = 22    # Minimum Temp in Celsius to turn the fan off
fanSPD = 100   # Fan Speed
PWM_Freq = 25  # [Hz]

#Oled Configuration
RST = 25
DC = 24
SPI_PORT = 0
SPI_DEVICE = 0
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, dc=DC, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=8000000))
disp.begin()
disp.clear()
disp.display()
width = disp.width
height = disp.height
image = Image.new('1', (width, height))
draw = ImageDraw.Draw(image)
draw.rectangle((0,0,width,height), outline=0, fill=0)

#Temperature Sensor
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

temp_sensor = '/sys/bus/w1/devices/28-0000060e26f0/w1_slave'

GPIO.setmode(GPIO.BCM)
GPIO.setup(fan_pin, GPIO.OUT)
GPIO.setwarnings(False)
fan=GPIO.PWM(fan_pin,PWM_Freq)
fan.start(0)

#GUI WIndow
root = Tk()
time1 = ''
root.title("Fan")
root.geometry("230x100+0+0")
root.resizable(width=FALSE, height=FALSE)
label_font = ('helvetica', 10)

#Window Frames
window1 = Frame(root, borderwidth=5, relief="ridge", width=125, height=100) #Window1
window2 = Frame(root, borderwidth=5, relief="ridge", width=100, height=100) #Window2

#Window Frame Grid
window1.grid(row=1, column=0, columnspan=1, rowspan=1, sticky=NW) #Window1
window2.grid(row=1, column=1, columnspan=1, rowspan=1, sticky=NW) #Window2
window1.grid_propagate(False) # Prevent window1 from resizing
window2.grid_propagate(False) # Prevent window2 from resizing

#Window 1
W1L1 = Label(window1, text="Temperature:" , font=(label_font)).grid(row=0,column=0,sticky=W)

#Window 2
W2L1 = Label(window2, text="Fan Status", font=(label_font)).grid(row=0,column=0,sticky=W)
W2F1 = Frame(window2, borderwidth=3, bg="yellow", relief="ridge", width=75, height=25)
W2F1.grid(row=1, column=0, columnspan=1, rowspan=1, sticky=W)
W2L2 = Label(window2, text="Fan Overide", font=(label_font)).grid(row=2,column=0,sticky=W)

def W2B1_on_auto():               
    if W2B1["text"] == "Fan Auto":
         W2B1["text"] = "Fan On"
         Fan_On()
         W2F1["bg"] = "green"
         print ("Case Fan On")         
    elif W2B1["text"] == "Fan On":
         W2B1["text"] = "Fan Auto"
         Fan_Auto()
         W2F1["bg"] = "Yellow"
         print ("Case Fan Auto")
    else:
         W2B1["text"] = "Fan Auto"
         Fan_Auto()
         W2F1["bg"] = "Yellow"
         print ("Case Fan Auto")
        
W2B1 = Button(window2, text="Fan Auto", command=W2B1_on_auto, width=5, height=1)
W2B1.grid(row=3,column=0,sticky=W)

#String Variables
roomtemp = StringVar()

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

def Fan_On():
    fan.ChangeDutyCycle(fanSPD)

def Fan_Off():
    fan.ChangeDutyCycle(0)
    
def Fan_Auto():
    room_temp = float(read_temp())
    if room_temp>=maxTMP:
        Fan_On()
        W2F1["bg"] = "green"
    elif room_temp<=minTMP:
        Fan_Off()
        W2F1["bg"] = "yellow"

def gui_vars():
    W1V1 = Label(window1, textvariable=roomtemp, font=('times', 30, 'bold')).grid(row=1,column=0,sticky=W)

def loops():
    global roomtemp
    if W2B1["text"] == "Fan Auto":
        Fan_Auto()
    temperature = read_temp()
    # Draw a black filled box to clear the image.
    draw.rectangle((0,0,width,height), outline=0, fill=0)
    draw.rectangle((0, 0, disp.width-1, disp.height-1), outline=20, fill=0)
    font = ImageFont.truetype('FreeSans.ttf', 35)
    draw.text((25, 12), (str(temperature)[:2])+chr(176) +'C ', font=font,fill=255)
    print(read_temp())
    # Display image.
    disp.image(image)
    disp.display()
    #GUI loops
    roomtemp.set ('%0.1fC' % temperature)
    root.after(1000, loops)
    
Fan_Auto   
gui_vars()   
loops()
root.mainloop()       
      
