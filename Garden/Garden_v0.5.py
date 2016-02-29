#!/usr/bin/python
#Version v0.5

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

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

temp_sensor = '/sys/bus/w1/devices/28-0000060e26f0/w1_slave'

# Open SPI bus
spi = spidev.SpiDev()
spi.open(0,0)

# Initiate gpio's for relay
gpio.setmode(gpio.BCM)
gpio.setup(12, gpio.OUT) # relay 1
gpio.setup(16, gpio.OUT) # relay 2

#GUI window
root = Tk()   
time1 = ''
root.title("Irrigation GUI v0.5")
root.geometry("700x875+300+100")
#Labels
label_font = ('helvetica', 12)
clock = Label(root)
L1 = Label(root, text="Temperature =").grid(row=1,column=0,sticky=W)
L2 = Label(root, text="Humidity =").grid(row=2,column=0,sticky=W)
L3 = Label(root, text="Moisture1 =").grid(row=3,column=0,sticky=W)
LC = Label(root, text="Moisture2 =").grid(row=4,column=0,sticky=W)
LD = Label(root, text="CPU Temp =").grid(row=5,column=0,sticky=W)
LE = Label(root, text="Case Temp =").grid(row=6,column=0,sticky=W)
L4 = Label(root, text ="Watering Times").grid(row=8, column=0, rowspan=1, columnspan=2, sticky=W)
L5 = Label(root, text ="Zone1").grid(row=9, column=0, rowspan=1, columnspan=2, sticky=W)
L6 = Label(root, text ="Manual").grid(row=9, column=1, rowspan=1, columnspan=2, sticky=W)
L7 = Label(root, text ="Zone2").grid(row=11, column=0, rowspan=1, columnspan=2, sticky=W)
L8 = Label(root, text ="Manual").grid(row=11, column=1, rowspan=1, columnspan=2, sticky=W)
LF = Label(root, text ="Cooling").grid(row=14, column=0, rowspan=1, columnspan=2, sticky=W)
LA = Label(root, text ="G/H Fan").grid(row=15, column=0, rowspan=1, columnspan=2, sticky=W)
LB = Label(root, text ="Manual").grid(row=15, column=1, rowspan=1, columnspan=2, sticky=W)
LG = Label(root, text ="Case Fan").grid(row=18, column=0, rowspan=1, columnspan=2, sticky=W)
LH = Label(root, text ="Manual").grid(row=18, column=1, rowspan=1, columnspan=2, sticky=W)
L9 = Label(root, text ="Red = On").grid(row=21, column=0, rowspan=1, columnspan=1, sticky=W)
L11 = Label(root, text ="Yellow = Auto").grid(row=21, column=1, rowspan=1, columnspan=1, sticky=W)
L10 = Label(root, text ="Black = Off").grid(row=22, column=0, rowspan=1, columnspan=1, sticky=W)
LL = Label(root, text ="Timers").grid(row=24, column=0, sticky=W)
L12 = Label(root, text ="Zone1 On:").grid(row=25, column=0, sticky=W)
L13 = Label(root, text ="Zone1 Off:").grid(row=26, column=0, sticky=W)
L14 = Label(root, text ="Zone2 On:").grid(row=27, column=0, sticky=W)
L15 = Label(root, text ="Zone2 Off:").grid(row=28, column=0, sticky=W)
L16 = Label(root, text ="G/H Fan On:").grid(row=29, column=0, sticky=W)
LJ = Label(root, text ="G/H Fan Off:").grid(row=30, column=0, sticky=W)
L16 = Label(root, text ="Case Fan On:").grid(row=31, column=0, sticky=W)
LK = Label(root, text ="Case Fan Off:").grid(row=32, column=0, sticky=W)
L18 = Label(root, text ="Camera 1:").grid(row=0, column=4)
L19 = Label(root, text ="Camera 2:").grid(row=18, column=4)
L20 = Label(root, text ="Shell Output:").grid(row=34, column=0, sticky=W)
clock = StringVar()
temp = StringVar()
hum = StringVar()
moist1 = StringVar()
moist2 = StringVar()
cputemp = StringVar()
casetemp = StringVar()

#Frames
frame1 = Frame(root, borderwidth=5, bg="black", relief="ridge", width=200, height=4)  #Divider1 
frame2 = Frame(root, borderwidth=3, bg="yellow", relief="ridge", width=50, height=25) #Zone1
frame3 = Frame(root, borderwidth=3, bg="Yellow", relief="ridge", width=50, height=25) #Zone2
frame4 = Frame(root, borderwidth=5, bg="black", relief="ridge", width=200, height=4)  #Divider2
frameA = Frame(root, borderwidth=3, bg="Yellow", relief="ridge", width=50, height=25) #G/H Fan
frameB = Frame(root, borderwidth=3, bg="Yellow", relief="ridge", width=50, height=25) #Case Fan
frame5 = Frame(root, borderwidth=5, bg="black", relief="ridge", width=200, height=4)  #Divider3
frameC = Frame(root, borderwidth=5, bg="black", relief="ridge", width=200, height=4)  #Divider4
frame6 = Frame(root, borderwidth=7, relief="ridge", width=350, height=275) #Camera Frame1
frame7 = Frame(root, borderwidth=7, relief="ridge", width=350, height=275) #Camera Frame2
#Frame grids
frame1.grid(row=7, column=0, columnspan=2, rowspan=1, sticky=W)  #Divider1
frame2.grid(row=10, column=0, columnspan=2, rowspan=1, sticky=W) #Zone1
frame3.grid(row=12, column=0, columnspan=2, rowspan=1, sticky=W) #Zone2
frame4.grid(row=13, column=0, columnspan=2, rowspan=1, sticky=W) #Divider2
frameA.grid(row=17, column=0, columnspan=2, rowspan=1, sticky=W) #G/H Fan
frameB.grid(row=19, column=0, columnspan=2, rowspan=1, sticky=W) #Case Fan
frame5.grid(row=23, column=0, columnspan=2, rowspan=1, sticky=W) #Divider3
frameC.grid(row=33, column=0, columnspan=2, rowspan=1, sticky=W) #Divider4
frame6.grid(row=0, column=5, columnspan=2, rowspan=18)           #Camera Frame1
frame7.grid(row=16, column=5, columnspan=2, rowspan=18)          #Camera Frame2

#Text
#Zone1 On
T1 = Text(root, width=10, height=1)
T1.insert("1.0", "0700\n") #Default value
T1.grid(row=25, column=1, sticky=W)
#Zone1 Off
T2 = Text(root, width=10, height=1)
T2.insert("1.0", "0730\n") #Default value
T2.grid(row=26, column=1, sticky=W)
#Zone2 On
T3 = Text(root, width=10, height=1)
T3.insert("1.0", "0700\n") #Default value
T3.grid(row=27, column=1, sticky=W)
#Zone2 Off
T4 = Text(root, width=10, height=1)
T4.insert("1.0", "0730\n") #Default value
T4.grid(row=28, column=1, sticky=W)
#G/H Fan On
T5 = Text(root, width=10, height=1)
T5.insert("1.0", "35\n") #Default value         
T5.grid(row=29, column=1, sticky=W)
#G/H Fan Off
T6 = Text(root, width=10, height=1)
T6.insert("1.0", "25\n") #Default value
T6.grid(row=30, column=1, sticky=W)
#Case Fan On
T7 = Text(root, width=10, height=1)
T7.insert("1.0", "35\n") #Default value
T7.grid(row=31, column=1, sticky=W)
#Case Fan Off
T8 = Text(root, width=10, height=1)
T8.insert("1.0", "25\n") #Default value
T8.grid(row=32, column=1, sticky=W)
#Shell
T9 = Text(root, width=28, height=8)
T9.grid(row=35, column=0, columnspan=2, rowspan=1, sticky=W)

# Get data
T1_get_data = T1.get("1.0",END)
T2_get_data = T2.get("1.0",END)
T3_get_data = T3.get("1.0",END)
T4_get_data = T4.get("1.0",END)
T5_get_data = T5.get("1.0",END)
T6_get_data = T6.get("1.0",END)
T7_get_data = T7.get("1.0",END)
T8_get_data = T8.get("1.0",END)

#Buttons
#Zone 1
def b1_on_off_auto():
    if B1["text"] == "Auto":
        B1["text"] = "On"
        relay_ch1_on()
        frame2["bg"] = "red"
        T7.insert("1.0", "Timer On\n")
        print "Timer On"                
    elif B1["text"] == "On":
         B1["text"] = "Off"
         #relay_ch1_off()
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

#Zone 2
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
B2.grid(row=12, column=1, sticky=W)

#G/H Fan
B3=Button(root, text="Auto", command=b2_on_off_auto, width=4, height=1)
B3.grid(row=17, column=1, sticky=W)

#Case Fan
B4=Button(root, text="Auto", command=b2_on_off_auto, width=4, height=1)
B4.grid(row=19, column=1, sticky=W)

def zone1_start():
    global T1_get_data
    T1_get_data = T1.get("1.0",END)
    T1_data = datetime.strptime(T1_get_data.rstrip('\n'), "%H%M").time()
    T9.insert("1.0", "Zone1 start %s\n" % T1_data)
    
B5=Button(root, text="Enter", command=zone1_start, width=4, height=1)
B5.grid(row=25, column=2, sticky=W)

def zone1_stop():
    global T2_get_data
    T2_get_data = T2.get("1.0",END)
    T2_data = datetime.strptime(T2_get_data.rstrip('\n'), "%H%M").time()
    T9.insert("1.0", "Zone1 stop %s\n" % T2_data)

B6=Button(root, text="Enter", command=zone1_stop, width=4, height=1)
B6.grid(row=26, column=2, sticky=W)

def zone2_start():
    global T3_get_data
    T3_get_data = T3.get("1.0",END)
    T3_data = datetime.strptime(T3_get_data.rstrip('\n'), "%H%M").time()
    T9.insert("1.0", "Zone2 start %s\n" % T3_data)
    
B7=Button(root, text="Enter", command=zone2_start, width=4, height=1)
B7.grid(row=27, column=2, sticky=W)

def zone2_stop():
    global T4_get_data
    T4_get_data = T4.get("1.0",END)
    T4_data = datetime.strptime(T4_get_data.rstrip('\n'), "%H%M").time()
    T9.insert("1.0", "Zone2 stop %s\n" % T4_data)
    
B8=Button(root, text="Enter", command=zone2_stop, width=4, height=1)
B8.grid(row=28, column=2, sticky=W)

def gh_fan_start():
    global T5_get_data
    T5_get_data = T5.get("1.0",END)
    T5_data = T5_get_data.rstrip('\n')
    T9.insert("1.0", "G/H fan start %s\n" % T5_data)
    
B9=Button(root, text="Enter", command=gh_fan_start, width=4, height=1)
B9.grid(row=29, column=2, sticky=W)

def gh_fan_stop():
    global T6_get_data
    T6_get_data = T6.get("1.0",END)
    T6_data = T6_get_data.rstrip('\n')
    T9.insert("1.0", "G/H fan stop %s\n" % T6_data)
    
B10=Button(root, text="Enter", command=gh_fan_stop, width=4, height=1)
B10.grid(row=30, column=2, sticky=W)

def case_fan_start():
    global T7_get_data
    T7_get_data = T5.get("1.0",END)
    T7_data = T7_get_data.rstrip('\n')
    T9.insert("1.0", "Case fan start %s\n" % T7_data)
    
B11=Button(root, text="Enter", command=case_fan_start, width=4, height=1)
B11.grid(row=31, column=2, sticky=W)

def case_fan_stop():
    global T8_get_data
    T8_get_data = T8.get("1.0",END)
    T8_data = T8_get_data.rstrip('\n')
    T9.insert("1.0", "Case fan stop %s\n" % T8_data)
    
B12=Button(root, text="Enter", command=case_fan_stop, width=4, height=1)
B12.grid(row=32, column=2, sticky=W)

def close():
    T6_data = T6.get("1.0",END)
    T7.insert("1.0", "%s" % T6_data)
    print "Close Script"
    
B13=Button(root, text="Close", command=sys.exit, width=4, height=1)
B13.grid(row=36, column=0, sticky=W)

#Timer controlled irrigation relay_ch1 
def Zone1Timer():
    a_time = T1_get_data
    zone1_start = datetime.strptime(a_time.rstrip('\n'), "%H%M").time()
    print zone1_start

    b_time = T2_get_data
    zone1_timer = datetime.strptime(b_time.rstrip('\n'), "%H%M").time()
    print zone1_timer
    
    if datetime.now().time() == zone1_start:
       #and datetime.now().time() <= morning_off:
       #relay_ch1_on()
       countdown1
       frame2["bg"] = "red"
       print "Zone1 On"
    else:
       #relay_ch1_off()
       frame2["bg"] = "yellow"
       print "Zone1 Off"
       
#Timer controlled irrigation relay_ch2
def Zone2Timer():
    c_time = T3_get_data
    zone2_start = datetime.strptime(c_time.rstrip('\n'), "%H%M").time()
    print zone2_start

    d_time = T4_get_data
    zone2_timer = datetime.strptime(d_time.rstrip('\n'), "%H%M").time()
    print zone2_timer
    
    if datetime.now().time() == zone2_start:
       #and datetime.now().time() <= evening_off:
       #relay_ch1_on()
       Zone2countdown()
       frame2["bg"] = "red"
       print "Zone2 On"
    #else:
       #relay_ch1_off()
       #frame2["bg"] = "yellow"
       #print "Zone2 Off"
       
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

# Function to read SPI data from MCP3008 chip
def ReadChannel(channel):
   adc = spi.xfer2([1,(8+channel)<<4,0])
   data = ((adc[1]&3) << 8) + adc[2]
   return data

#Moisture controlled irrigation relay_ch
#def MoistureTimer():
    #Import moisture from moisture sensor // 1 second refresh rate
    #moisture_data = ReadChannel(2)
    #moisture = ('%d' % moisture_data) 
    #d_time = T5_get_data
    #moisture_min = d_time.rstrip('\n')
    #print moisture_min

    #e_time = T6_get_data
    #moisture_max = e_time.rstrip('\n')
    #print moisture_max
    
    #if moisture >= moisture_min and moisture <= moisture_max:
       #relay_ch2_on()
       #frame3["bg"] = "red"
       #print "Moisture on"
    #else:
       #relay_ch2_off()
       #frame3["bg"] = "yellow"
       #print "Moisture off"
       
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

def gui_widgets():
   Label(root, textvariable=clock, font=('Times', 20, 'bold')).grid(row=0,column=0,sticky=W)
   Label(root, textvariable=temp).grid(row=1,column=1,sticky=W)
   Label(root, textvariable=hum).grid(row=2,column=1,sticky=W)
   Label(root, textvariable=moist1).grid(row=3,column=1,sticky=W)
   Label(root, textvariable=moist2).grid(row=4,column=1,sticky=W)
   Label(root, textvariable=cputemp).grid(row=5,column=1,sticky=W)
   Label(root, textvariable=casetemp).grid(row=6,column=1,sticky=W)
   
def updates():
    global clock
    global counter
    global temperature
    global read_temp
    global humidity
    global moisture
           
    #Import Humidity and Temperature from AdafruitDHT // 30 second refresh rate
    if counter % 30 == 0:
        humidity, temperature = Adafruit_DHT.read_retry(22, 26)
    #Import moisture from moisture sensor // 1 second refresh rate
    moisture1 = ReadChannel(2)
    moisture2 = ReadChannel(3)
    
    #Zone 1
    if B1["text"] == "Auto":
       Zone1Timer()
        
    #Zone 2
    if B2["text"] == "Auto":
       Zone2Timer()
              
    #LCD updates  
    lcd.clear()
    lcd.message(datetime.now().time().strftime('%H:%M:%S '))
    lcd.message ('T=%0.1fC\n' % temperature)
    lcd.message ('H=%0.1f%%' % humidity)
    lcd.message ('  M=%d' % moisture1)
    #GUI updates
    clock.set (datetime.now().time().strftime('%H:%M:%S '))
    temp.set ('%0.1fC' % temperature)
    casetemp.set ('%dC' % read_temp())
    hum.set ('%0.1f%%' % humidity)
    moist1.set ('%d' % moisture1)
    moist2.set ('%d' % moisture2)
    counter += 1
    root.after(1000, updates)
           
Zone1Timer()
Zone2Timer()
temp_raw()
read_temp()
gui_widgets()
root.after(1000, updates)   

root.mainloop() 
gpio.cleanup()	

