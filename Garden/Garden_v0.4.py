#!/usr/bin/python
#Version v0.3

#0 ~300 : dry soil
#300~700 : humid soil
#700~950 : in water

from Adafruit_CharLCD import Adafruit_CharLCD
from subprocess import *
from time import sleep, strftime
from datetime import datetime
from Tkinter import *
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
moisture_min = 650
moisture_max = 700

print ('Watering times:')
a = datetime(100,1,1,7,00,00) #7:00:00
morning_on = a.time()
print a.time()

b = datetime(100,1,1,7,30,00) #7:30:00
morning_off = b.time()
print b.time()

c = datetime(100,1,1,21,23,00) #19:00:00
evening_on = c.time()
print c.time()

d = datetime(100,1,1,21,24,00) #19:30:00
evening_off = d.time()
print d.time()

#GUI window
root = Tk()   
time1 = ''
root.title("Irrigation GUI")
root.geometry("800x650+350+350")
#Labels
clock = Label(root)
L1 = Label(root, text="Temperature =").grid(row=1,column=0,sticky=W)
L2 = Label(root, text="Humidity =").grid(row=2,column=0,sticky=W)
L3 = Label(root, text="Moisture =").grid(row=3,column=0,sticky=W)
L4 = Label(root, text ="Watering Times").grid(row=5, column=0, rowspan=1, columnspan=2)
L5 = Label(root, text ="Red = On/ Black = Off/ Yellow = Auto").grid(row=6, column=0, rowspan=1, columnspan=2)
L6 = Label(root, text ="Timer").grid(row=7, column=0, sticky=W)
L7 = Label(root, text ="Manual").grid(row=7, column=1, sticky=W)
L8 = Label(root, text ="Moisture").grid(row=11, column=0, sticky=W)
L9 = Label(root, text ="Manual").grid(row=11, column=1, sticky=W)
L10 = Label(root, text ="Morning Start").grid(row=15, column=0, sticky=W)
L11 = Label(root, text ="Morning Stop").grid(row=16, column=0, sticky=W)
L12 = Label(root, text ="Evening Start").grid(row=17, column=0, sticky=W)
L13 = Label(root, text ="Evening Stop").grid(row=18, column=0, sticky=W)
L14 = Label(root, text ="Moisture Min").grid(row=19, column=0, sticky=W)
L15 = Label(root, text ="Moisture Max").grid(row=20, column=0, sticky=W)
L16 = Label(root, text ="Camera 1:").grid(row=0, column=23, sticky=W)
L17 = Label(root, text ="Camera 2:").grid(row=18, column=23, sticky=W)
L18 = Label(root, text ="Shell Output:").grid(row=22, column=0, sticky=W)
clock = StringVar()
temp = StringVar()
hum = StringVar()
moist = StringVar()

#Text
T1 = Text(root, width=10, height=1)
T1.insert("1.0", "07:00\n")
T1.grid(row=15, column=1, sticky=W)

T2 = Text(root, width=10, height=1)
T2.insert("1.0", "07:30\n")
T2.grid(row=16, column=1, sticky=W)

T3 = Text(root, width=10, height=1)
T3.insert("1.0", "19:00\n")
T3.grid(row=17, column=1, sticky=W)

T4 = Text(root, width=10, height=1)
T4.insert("1.0", "19:30\n")
T4.grid(row=18, column=1, sticky=W)

T5 = Text(root, width=10, height=1)
T5.insert("1.0", "400\n")          
T5.grid(row=19, column=1, sticky=W)

T6 = Text(root, width=10, height=1)
T6.insert("1.0", "600\n")
T6.grid(row=20, column=1, sticky=W)

T7 = Text(root, width=28, height=10)
T7.grid(row=23, column=0, columnspan=2, rowspan=1, sticky=W)

#Buttons
#Timer button
def b1_on_off_auto():
    if B1["text"] == "Auto":
        B1["text"] = "On"
        relay_ch1_on()
        frame2["bg"] = "red"
        T7.insert("1.0", "Timer On\n")
        print "Timer On"                
    elif B1["text"] == "On":
         B1["text"] = "Off"
         relay_ch1_off()
         frame2["bg"] = "black"
         T7.insert("1.0", "Timer Off\n")
         print "Timer Off"                                  
    else:
         B1["text"] = "Auto"
         DayTimer()
         frame2["bg"] = "Yellow"
         T7.insert("1.0", "Timer Auto\n")
         print "Timer Auto"
B1=Button(root, text="Auto", command=b1_on_off_auto, width=4, height=1)
B1.grid(row=10, column=1, sticky=W)

#Moisture button
def b2_on_off_auto():
    if B2["text"] == "Auto":
        B2["text"] = "On"
        relay_ch2_on()
        frame3["bg"] = "red"
        T7.insert("1.0", "Moisture On\n")
        print "Moisture On"                
    elif B2["text"] == "On":
         B2["text"] = "Off"
         relay_ch2_off()
         frame3["bg"] = "black"
         T7.insert("1.0", "Moisture Off\n")
         print "Moisture Off"         
    else:
         B2["text"] = "Auto"
         MoistureTimer()
         frame3["bg"] = "yellow"
         T7.insert("1.0", "Moisture Auto\n")
         print "Moisture Auto"                  
B2=Button(root, text="Auto", command=b2_on_off_auto, width=4, height=1)
B2.grid(row=13, column=1, sticky=W)

def morning_start():
    T1_data = T1.get("1.0",END)
    T7.insert("1.0", "%s" % T1_data)
    print T1_data
B3=Button(root, text="Enter", command=morning_start, width=4, height=1)
B3.grid(row=15, column=3, sticky=W)

def morning_stop():
    T2_data = T2.get("1.0",END)
    T7.insert("1.0", "%s" % T2_data)
    print T2_data
B4=Button(root, text="Enter", command=morning_stop, width=4, height=1)
B4.grid(row=16, column=3, sticky=W)

def evening_start():
    T3_data = T3.get("1.0", END)
    T7.insert("1.0", "%s" % T3_data)
    print T3_data
B5=Button(root, text="Enter", command=evening_start, width=4, height=1)
B5.grid(row=17, column=3, sticky=W)

def evening_stop():
    T4_data = T4.get("1.0",END)
    T7.insert("1.0", "%s" % T4_data)
    print T4_data
B6=Button(root, text="Enter", command=evening_stop, width=4, height=1)
B6.grid(row=18, column=3, sticky=W)

def moisture_min():
    T5_data = T5.get("1.0",END)
    T7.insert("1.0", "%s" % T5_data)
    print T5_data
B7=Button(root, text="Enter", command=moisture_min, width=4, height=1)
B7.grid(row=19, column=3, sticky=W)

def moisture_max():
    T6_data = T6.get("1.0",END)
    T7.insert("1.0", "%s" % T6_data)
    print T6_data
B8=Button(root, text="Enter", command=moisture_max, width=4, height=1)
B8.grid(row=20, column=3, sticky=W)

def close():
    T6_data = T6.get("1.0",END)
    T7.insert("1.0", "%s" % T6_data)
    print "Close Script"
B10=Button(root, text="Close", command=sys.exit, width=4, height=1)
B10.grid(row=24, column=0, sticky=W)

#Frames
frame1 = Frame(root, borderwidth=5, bg="black", relief="ridge", width=180, height=4)
frame2 = Frame(root, borderwidth=3, bg="yellow", relief="ridge", width=50, height=25)
frame3 = Frame(root, borderwidth=3, bg="Yellow", relief="ridge", width=50, height=25)
frame4 = Frame(root, borderwidth=5, bg="black", relief="ridge", width=200, height=4)
frame5 = Frame(root, borderwidth=5, bg="black", relief="ridge", width=200, height=4)
frame6 = Frame(root, borderwidth=7, relief="ridge", width=350, height=275)
frame7 = Frame(root, borderwidth=7, relief="ridge", width=350, height=275)
#Frame grids
frame1.grid(row=4, column=0, columnspan=2, rowspan=1, sticky=W)
frame2.grid(row=10, column=0, columnspan=2, rowspan=1, sticky=W)
frame3.grid(row=13, column=0, columnspan=2, rowspan=1, sticky=W)
frame4.grid(row=14, column=0, columnspan=2, rowspan=1, sticky=W)
frame5.grid(row=21, column=0, columnspan=2, rowspan=1, sticky=W)
frame6.grid(row=0, column=24, columnspan=2, rowspan=18, sticky=E)
frame7.grid(row=19, column=24, columnspan=2, rowspan=18, sticky=W)


def gui_widgets():
   Label(root, textvariable=clock, font=('Times', 20, 'bold')).grid(row=0,column=0,sticky=W)
   Label(root, textvariable=temp).grid(row=1,column=1,sticky=W)
   Label(root, textvariable=hum).grid(row=2,column=1,sticky=W)
   Label(root, textvariable=moist).grid(row=3,column=1,sticky=W)

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

#Time controlled irrigation relay_ch1
#Daytime and evening irrigation time
def DayTimer():
    if datetime.now().time() >= morning_on and datetime.now().time() <= morning_off:
       relay_ch1_on()
    elif datetime.now().time() >= evening_on and datetime.now().time() <= evening_off:
       relay_ch1_on()
       frame2["bg"] = "red"
    else:
       relay_ch1_off()
       frame2["bg"] = "yellow"

#Moisture controlled irrigation relay_ch2
def MoistureTimer():
    #global moisture
    if moisture >= moisture_min and moisture <= moisture_max:
       relay_ch2_on()
       frame3["bg"] = "red"
    else:
       relay_ch2_off()
       frame3["bg"] = "yellow"
       
lcd = Adafruit_CharLCD()
lcd.begin(16, 1)
counter = 0

def updates():
    global clock
    global counter
    global temperature
    global humidity
    #global moisture
       
    #Import Humidity and Temperature from AdafruitDHT // 30 second refresh rate
    if counter % 30 == 0:
        humidity, temperature = Adafruit_DHT.read_retry(22, 4)
    #Import moisture from moisture sensor // 1 second refresh rate
    moisture = ReadChannel(2)
    
    #Irrigaation timer
    if B1["text"] == "Auto":
       DayTimer()
        
    #Moisture timer
    if B2["text"] == "Auto":
       MoistureTimer()
        
    #LCD updates  
    lcd.clear()
    lcd.message(datetime.now().time().strftime('%H:%M:%S '))
    lcd.message ('T=%0.1fC\n' % temperature)
    lcd.message ('H=%0.1f%%' % humidity)
    lcd.message ('  M=%d' % moisture)
    #GUI updates
    clock.set (datetime.now().time().strftime('%H:%M:%S '))
    temp.set ('%0.1fC' % temperature)
    hum.set ('%0.1f%%' % humidity)
    moist.set ('%d' % moisture)       
    counter += 1
    root.after(1000, updates)
    
DayTimer()
MoistureTimer()
gui_widgets()
root.after(1000, updates)   

root.mainloop() 
gpio.cleanup()	
