#!/usr/bin/python
#Version v0.6

#0 ~300 : dry soil
#300~700 : humid soil
#700~950 : in water

from Adafruit_CharLCD import Adafruit_CharLCD
import subprocess
from time import sleep, strftime
from datetime import datetime
from Tkinter import *
import sys
import Adafruit_DHT
import os
import spidev
import RPi.GPIO as gpio
import commands
import signal

#16x2 LCD
lcd = Adafruit_CharLCD()
lcd.begin(16, 1)

#Case Temperature Sensor
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

temp_sensor = '/sys/bus/w1/devices/28-0000060e26f0/w1_slave'

#Counter
counter = 0

# Open SPI bus
spi = spidev.SpiDev()
spi.open(0,0)

# Initiate gpio's for relay
gpio.setmode(gpio.BCM)
gpio.setup(5, gpio.OUT) # relay 1
gpio.setup(6, gpio.OUT) # relay 2
gpio.setup(16, gpio.OUT) # relay 3
gpio.setup(26, gpio.OUT) # relay 4

#set relay gpio's to false
gpio.output(5, True) # relay 1
gpio.output(6, True) # relay 2
gpio.output(16, True) # relay 3
gpio.output(26, True) # relay 4

#GUI window
root = Tk()   
time1 = ''
root.title("Irrigation GUI v0.6")
root.geometry("630x424+300+100")

#Window Frames
window1 = Frame(root, borderwidth=5, relief="ridge", width=200, height=300) #Window1
window2 = Frame(root, borderwidth=5, relief="ridge", width=200, height=400) #Window2
window3 = Frame(root, borderwidth=5, relief="ridge", width=200, height=400) #Window3

#Window Frame Grids
window1.grid(row=1, column=0, columnspan=1, rowspan=1, sticky=NW) #Window1
window2.grid(row=1, column=1, columnspan=1, rowspan=1, sticky=NW) #Window2
window3.grid(row=1, column=2, columnspan=1, rowspan=3, sticky=NW) #Window3

#Labels
label_font = ('helvetica', 12)
clock = Label(window1)
L1 = Label(window1, text="Temperature =").grid(row=1, column=0, sticky=W)
L2 = Label(window1, text="Humidity =").grid(row=2, column=0, sticky=W)
L3 = Label(window1, text="Moisture1 =").grid(row=3, column=0, sticky=W)
L4 = Label(window1, text="Moisture2 =").grid(row=4, column=0, sticky=W)
L5 = Label(window1, text="CPU Temp =").grid(row=5, column=0, sticky=W)
L6 = Label(window1, text="Case Temp =").grid(row=6, column=0, sticky=W)
L7 = Label(window2, text ="Watering Times:").grid(row=0, column=0, sticky=W)
L8 = Label(window2, text ="Zone1").grid(row=1, column=0, sticky=W)
L9 = Label(window2, text ="Manual").grid(row=1, column=1, sticky=W)
L10 = Label(window2, text ="Zone2").grid(row=3, column=0, sticky=W)
L11 = Label(window2, text ="Manual").grid(row=3, column=1, sticky=W)
L12 = Label(window2, text ="Cooling:").grid(row=6, column=0, sticky=W)
L13 = Label(window2, text ="G/H Fan").grid(row=7, column=0, sticky=W)
L14 = Label(window2, text ="Manual").grid(row=7, column=1, sticky=W)
L15 = Label(window2, text ="Case Fan").grid(row=9, column=0, sticky=W)
L16 = Label(window2, text ="Manual").grid(row=9, column=1, sticky=W)
L17 = Label(window2, text ="Red = On").grid(row=11, column=0, sticky=W)
L18 = Label(window2, text ="Yellow = Auto").grid(row=11, column=1, sticky=W)
L19 = Label(window2, text ="Black = Off").grid(row=12, column=0, sticky=W)
L20 = Label(window3, text ="Timers:").grid(row=0, column=0, sticky=W)
L21= Label(window3, text ="Zone1 On:").grid(row=1, column=0, sticky=W)
L22 = Label(window3, text ="Zone1 Off:").grid(row=2, column=0, sticky=W)
L23 = Label(window3, text ="Zone2 On:").grid(row=3, column=0, sticky=W)
L24 = Label(window3, text ="Zone2 Off:").grid(row=4, column=0, sticky=W)
L25 = Label(window3, text =" G/H Fan On:").grid(row=5, column=0, sticky=W)
L26 = Label(window3, text =" G/H Fan Off:").grid(row=6, column=0, sticky=W)
L27 = Label(window3, text =" Case Fan On:").grid(row=7, column=0, sticky=W)
L28 = Label(window3, text =" Case Fan Off:").grid(row=8, column=0, sticky=W)
L29 = Label(window1, text ="Camera1 On/Off:").grid(row=8, column=0, sticky=W)
L30 = Label(window1, text ="Close GUI:").grid(row=10, column=0, sticky=W)
L31 = Label(window3, text ="Output Display:").grid(row=10, column=0, sticky=W)

#String Variables
clock = StringVar()
temp = StringVar()
hum = StringVar()
moist1 = StringVar()
moist2 = StringVar()
cputemp = StringVar()
casetemp = StringVar()

#Frames
frame1 = Frame(window1, borderwidth=5, bg="grey", relief="ridge", width=150, height=4)   #Divider1 
frame2 = Frame(window2, borderwidth=3, bg="yellow", relief="ridge", width=50, height=25) #Zone1
frame3 = Frame(window2, borderwidth=3, bg="Yellow", relief="ridge", width=50, height=25) #Zone2
frame4 = Frame(window2, borderwidth=5, bg="grey", relief="ridge", width=195, height=4)   #Divider2
frame5 = Frame(window2, borderwidth=3, bg="Yellow", relief="ridge", width=50, height=25) #G/H Fan
frame6 = Frame(window2, borderwidth=3, bg="Yellow", relief="ridge", width=50, height=25) #Case Fan
frame7 = Frame(window3, borderwidth=5, bg="grey", relief="ridge", width=250, height=4)   #Divider3

#Frame grids
frame1.grid(row=7, column=0, columnspan=2, rowspan=1, sticky=W)  #Divider1
frame2.grid(row=2, column=0, columnspan=1, rowspan=1, sticky=W)  #Zone1
frame3.grid(row=4, column=0, columnspan=1, rowspan=1, sticky=W)  #Zone2
frame4.grid(row=5, column=0, columnspan=2, rowspan=1, sticky=W)  #Divider2
frame5.grid(row=8, column=0, columnspan=1, rowspan=1, sticky=W)  #G/H Fan
frame6.grid(row=10, column=0, columnspan=1, rowspan=1, sticky=W) #Case Fan
frame7.grid(row=9, column=0, columnspan=4, rowspan=1, sticky=W)  #Divider3


#Text
#Zone1 On
T1 = Text(window3, width=10, height=1)
T1.insert("1.0", "0630\n") #Default value
T1.grid(row=1, column=1, sticky=W)
#Zone1 Off
T2 = Text(window3, width=10, height=1)
T2.insert("1.0", "0700\n") #Default value
T2.grid(row=2, column=1, sticky=W)
#Zone2 On
T3 = Text(window3, width=10, height=1)
T3.insert("1.0", "1700\n") #Default value
T3.grid(row=3, column=1, sticky=W)
#Zone2 Off
T4 = Text(window3, width=10, height=1)
T4.insert("1.0", "1730\n") #Default value
T4.grid(row=4, column=1, sticky=W)
#G/H Fan On
T5 = Text(window3, width=10, height=1)
T5.insert("1.0", "25.0\n") #Default value         
T5.grid(row=5, column=1, sticky=W)
#G/H Fan Off
T6 = Text(window3, width=10, height=1)
T6.insert("1.0", "18.0\n") #Default value
T6.grid(row=6, column=1, sticky=W)
#Case Fan On
T7 = Text(window3, width=10, height=1)
T7.insert("1.0", "25.0\n") #Default value
T7.grid(row=7, column=1, sticky=W)
#Case Fan Off
T8 = Text(window3, width=10, height=1)
T8.insert("1.0", "18.0\n") #Default value
T8.grid(row=8, column=1, sticky=W)
#Output Display
T9 = Text(window3, width=35, height=10)
T9.grid(row=11, column=0, columnspan=4, rowspan=1, sticky=W)

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
        T9.insert("1.0", "Zone1 On\n")
        print "Zone1 On"                
    elif B1["text"] == "On":
         B1["text"] = "Off"
         relay_ch1_off()
         frame2["bg"] = "black"
         T9.insert("1.0", "Zone1 Off\n")
         print "Zone1 Off"         
    else:
         B1["text"] = "Auto"
         Zone1Timer()
         frame2["bg"] = "yellow"
         T9.insert("1.0", "Zone1 Auto\n")
         print "Zone1 Auto"
B1=Button(window2, text="Auto", command=b1_on_off_auto, width=4, height=1)
B1.grid(row=2, column=1, sticky=W)

#Zone 2
def b2_on_off_auto():
    if B2["text"] == "Auto":
        B2["text"] = "On"
        relay_ch2_on()
        frame3["bg"] = "red"
        T9.insert("1.0", "Zone2 On\n")
        print "Zone2 On"                
    elif B2["text"] == "On":
         B2["text"] = "Off"
         relay_ch2_off()
         frame3["bg"] = "black"
         T9.insert("1.0", "Zone2 Off\n")
         print "Zone2 Off"         
    else:
         B2["text"] = "Auto"
         Zone2Timer()
         frame3["bg"] = "yellow"
         T9.insert("1.0", "Zone2 Auto\n")
         print "Zone2 Auto"
B2=Button(window2, text="Auto", command=b2_on_off_auto, width=4, height=1)
B2.grid(row=4, column=1, sticky=W)

#G/H Fan
def b3_on_off_auto():
    if B3["text"] == "Auto":
        B3["text"] = "On"
        relay_ch4_on()
        frame5["bg"] = "red"
        T9.insert("1.0", "G/H Fan On\n")
        print "G/H Fan On"                
    elif B3["text"] == "On":
         B3["text"] = "Off"
         relay_ch4_off()
         frame5["bg"] = "black"
         T9.insert("1.0", "G/H Fan Off\n")
         print "G/H Fan Off"                                  
    else:
         B3["text"] = "Auto"
         GH_FanAuto()
         frame5["bg"] = "Yellow"
         T9.insert("1.0", "G/H Fan Auto\n")
         print "G/H Fan Auto"
B3=Button(window2, text="Auto", command=b3_on_off_auto, width=4, height=1)
B3.grid(row=8, column=1, sticky=W)

#Case Fan
def b4_on_off_auto():
    if B4["text"] == "Auto":
        B4["text"] = "On"
        relay_ch3_on()
        frame6["bg"] = "red"
        T9.insert("1.0", "Case Fan On\n")
        print "Case Fan On"                
    elif B4["text"] == "On":
         B4["text"] = "Off"
         relay_ch3_off()
         frame6["bg"] = "black"
         T9.insert("1.0", "Case Fan Off\n")
         print "Case Fan Off"                                  
    else:
         B4["text"] = "Auto"
         CaseFanAuto()
         frame6["bg"] = "Yellow"
         T9.insert("1.0", "Case Fan Auto\n")
         print "Case Fan Auto"
B4=Button(window2, text="Auto", command=b4_on_off_auto, width=4, height=1)
B4.grid(row=10, column=1, sticky=W)

def zone1_start():
    global T1_get_data
    T1_get_data = T1.get("1.0",END)
    T1_data = datetime.strptime(T1_get_data.rstrip('\n'), "%H%M").time()
    T9.insert("1.0", "Zone1 Start %s\n" % T1_data)
    
B5=Button(window3, text="Enter", command=zone1_start, width=4, height=1)
B5.grid(row=1, column=3, sticky=W)

def zone1_stop():
    global T2_get_data
    T2_get_data = T2.get("1.0",END)
    T2_data = datetime.strptime(T2_get_data.rstrip('\n'), "%H%M").time()
    T9.insert("1.0", "Zone1 Stop %s\n" % T2_data)

B6=Button(window3, text="Enter", command=zone1_stop, width=4, height=1)
B6.grid(row=2, column=3, sticky=W)

def zone2_start():
    global T3_get_data
    T3_get_data = T3.get("1.0",END)
    T3_data = datetime.strptime(T3_get_data.rstrip('\n'), "%H%M").time()
    T9.insert("1.0", "Zone2 Start  %s\n" % T3_data)
    
B7=Button(window3, text="Enter", command=zone2_start, width=4, height=1)
B7.grid(row=3, column=3, sticky=W)

def zone2_stop():
    global T4_get_data
    T4_get_data = T4.get("1.0",END)
    T4_data = datetime.strptime(T4_get_data.rstrip('\n'), "%H%M").time()
    T9.insert("1.0", "Zone2 Stop %s\n" % T4_data)
    
B8=Button(window3, text="Enter", command=zone2_stop, width=4, height=1)
B8.grid(row=4, column=3, sticky=W)

def gh_fan_start():
    global T5_get_data
    T5_get_data = T5.get("1.0",END)
    T5_data = T5_get_data.rstrip('\n')
    T9.insert("1.0", "G/H Fan Start %s\n" % T5_data)
    
B9=Button(window3, text="Enter", command=gh_fan_start, width=4, height=1)
B9.grid(row=5, column=3, sticky=W)

def gh_fan_stop():
    global T6_get_data
    T6_get_data = T6.get("1.0",END)
    T6_data = T6_get_data.rstrip('\n')
    T9.insert("1.0", "G/H Fan Stop %s\n" % T6_data)
    
B10=Button(window3, text="Enter", command=gh_fan_stop, width=4, height=1)
B10.grid(row=6, column=3, sticky=W)

def case_fan_start():
    global T7_get_data
    T7_get_data = T7.get("1.0",END)
    T7_data = T7_get_data.rstrip('\n')
    T9.insert("1.0", "Case Fan Start %s\n" % T7_data)
    
B11=Button(window3, text="Enter", command=case_fan_start, width=4, height=1)
B11.grid(row=7, column=3, sticky=W)

def case_fan_stop():
    global T8_get_data
    T8_get_data = T8.get("1.0",END)
    T8_data = T8_get_data.rstrip('\n')
    T9.insert("1.0", "Case Fan Stop %s\n" % T8_data)
    
B12=Button(window3, text="Enter", command=case_fan_stop, width=4, height=1)
B12.grid(row=8, column=3, sticky=W)

def camera1_on_off():
    global proc
    if B13["text"] == "Cam Off":
        B13["text"] = "Cam On"
        command= "python Garden_video.py"
        proc=subprocess.Popen(command, stdout=subprocess.PIPE, shell=True, preexec_fn=os.setsid)
        print "Cam On"                
    elif B13["text"] == "Cam On":
        B13["text"] = "Cam Off"
        os.killpg(os.getpgid(proc.pid), signal.SIGTERM)
        print "Cam Off" 
    else:
        B13["text"] = "Cam Off"     
       
B13=Button(window1, text="Cam Off", command=camera1_on_off, width=4, height=1)
B13.grid(row=9, column=0, sticky=W)

def close():
    global proc
    #set relay gpio's to false
    gpio.output(5, False) # relay 1
    gpio.output(6, False) # relay 2
    gpio.output(16, False) # relay 3
    gpio.output(26, False) # relay 4
    gpio.cleanup()
    if B13["text"] == "Cam On":
       os.killpg(os.getpgid(proc.pid), signal.SIGTERM)  
    quit()
    print "Close Script"
    
B14=Button(window1, text="Close", command=close, width=4, height=1)
B14.grid(row=11, column=0, sticky=W)

#Timer controlled irrigation Zone 1 // relay_ch1 
def Zone1Timer():
    a_time = T1_get_data
    zone1_start = datetime.strptime(a_time.rstrip('\n'), "%H%M").time()
    print zone1_start

    b_time = T2_get_data
    zone1_stop = datetime.strptime(b_time.rstrip('\n'), "%H%M").time()
    print zone1_stop
    
    if datetime.now().time() >= zone1_start and datetime.now().time() <= zone1_stop:
       relay_ch1_on()
       frame2["bg"] = "red"
       print "Zone1 On"
    else:
       relay_ch1_off()
       frame2["bg"] = "yellow"
       print "Zone1 Off"
       
#Timer controlled irrigation Zone 2 // relay_ch2
def Zone2Timer():
    c_time = T3_get_data
    zone2_start = datetime.strptime(c_time.rstrip('\n'), "%H%M").time()
    print zone2_start

    d_time = T4_get_data
    zone2_stop = datetime.strptime(d_time.rstrip('\n'), "%H%M").time()
    print zone2_stop
    
    if datetime.now().time() >= zone2_start and datetime.now().time() <= zone2_stop:
       relay_ch2_on()
       frame3["bg"] = "red"
       print "Zone2 On"
    else:
       relay_ch2_off()
       frame3["bg"] = "yellow"
       print "Zone2 Off"

#Temperature controlled Green House fan // relay_ch4
def GH_FanAuto():
    global temperature
    global gh_fan_temp
    if counter % 30 == 0:
       humidity, temperature = Adafruit_DHT.read_retry(22, 18)
    if temperature is not None:
       gh_fan_temp = ('%1.0f' % temperature)
       print gh_fan_temp
    else:
       print 'GUI Failed to get reading. Try again!'
       
    e_time = T5_get_data
    gh_fan_temp_max = e_time.rstrip('\n')
    print gh_fan_temp_max
    
    f_time = T6_get_data
    gh_fan_temp_min = f_time.rstrip('\n')
    print gh_fan_temp_min
    
    if gh_fan_temp >= gh_fan_temp_max:   
       relay_ch4_on()
       frame5["bg"] = "red"
       print "G/H Fan On"
    elif gh_fan_temp <= gh_fan_temp_min:
       relay_ch4_off()
       frame5["bg"] = "yellow"
       print "G/H Fan Off"
       
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

#Temperature controlled Case fan // relay_ch3
def CaseFanAuto():
    global case_fan_temp
    if counter % 20 == 0:
       case_fan_data = read_temp()
       case_fan_temp = ('%1.0f' % case_fan_data)
       print case_fan_temp
       
    g_time = T7_get_data
    case_fan_temp_max = g_time.rstrip('\n')
    print case_fan_temp_max

    h_time = T8_get_data
    case_fan_temp_min = h_time.rstrip('\n')
    print case_fan_temp_min
    
    if case_fan_temp >= case_fan_temp_max:   
       relay_ch3_on()
       frame6["bg"] = "red"
       print "Case Fan On"
    elif case_fan_temp <= case_fan_temp_min:
       relay_ch3_off()
       frame6["bg"] = "yellow"
       print "Case Fan Off"
   
# RPI CPU Temperature
def getTempCPU():
    temp = commands.getoutput("/opt/vc/bin/vcgencmd measure_temp")
    initTempPos = str(temp).find("=")
    finishTempPos = str(temp).find("'")
    temp = str(temp)[initTempPos+1:finishTempPos]
    try:
        temp_num = float(temp)
        return temp_num
    except:
        print "Unable to transform to float"
       
# Function to read SPI data from MCP3008 chip
def ReadChannel(channel):
   adc = spi.xfer2([1,(8+channel)<<4,0])
   data = ((adc[1]&3) << 8) + adc[2]
   return data
       
# Zone1 relay ch1 on and off
def relay_ch1_on():
    gpio.output(5, False) #Relay ch1 on
def relay_ch1_off(): 
    gpio.output(5, True) #Relay ch1 off

# Zone2 relay ch2 on and off
def relay_ch2_on():
    gpio.output(6, False) #Relay ch2 on
def relay_ch2_off(): 
    gpio.output(6, True) #Relay ch2 off

# G/H fan relay ch3 on and off
def relay_ch3_on():
    gpio.output(16, False) #Relay ch3 on
def relay_ch3_off(): 
    gpio.output(16, True) #Relay ch3 off

# Case fan relay ch4 on and off
def relay_ch4_on():
    gpio.output(26, False) #Relay ch4 on
def relay_ch4_off(): 
    gpio.output(26, True) #Relay ch4 off


def gui_widgets():
   Label(window1, textvariable=clock, font=('Times', 20, 'bold')).grid(row=0,column=0,sticky=W)
   Label(window1, textvariable=temp).grid(row=1,column=1,sticky=W)
   Label(window1, textvariable=hum).grid(row=2,column=1,sticky=W)
   Label(window1, textvariable=moist1).grid(row=3,column=1,sticky=W)
   Label(window1, textvariable=moist2).grid(row=4,column=1,sticky=W)
   Label(window1, textvariable=cputemp).grid(row=5,column=1,sticky=W)
   Label(window1, textvariable=casetemp).grid(row=6,column=1,sticky=W)
   
def updates():
    global clock
    global counter
    global temperature
    global read_temp
    global getTempCPU
    global humidity
    global moisture
    global CPUTemp
    global CaseTemp
           
    #Import Humidity and Temperature from AdafruitDHT // 30 second refresh rate
    if counter % 30 == 0:
       humidity, temperature = Adafruit_DHT.read_retry(22, 18)
    #Import Case Temperature from DS18B20 digital temperature sensor // 20 second refresh rate
    if counter % 20 == 0:
       CaseTemp = read_temp()
    #Import CPU Temperature // 10 second refresh rate    
    if counter % 10 == 0:    
       CPUTemp = getTempCPU()
    #Import moisture from moisture sensors // 1 second refresh rate
    moisture1 = ReadChannel(2)
    moisture2 = ReadChannel(3)
    
    #Zone 1
    if B1["text"] == "Auto":
       Zone1Timer()
        
    #Zone 2
    if B2["text"] == "Auto":
       Zone2Timer()

    #G/H Fan
    if B3["text"] == "Auto":
       GH_FanAuto()    

    #Case Fan
    if B4["text"] == "Auto":
       CaseFanAuto()   
              
    #LCD updates  
    lcd.clear()
    lcd.message(datetime.now().time().strftime('%H:%M:%S '))
    if humidity is not None and temperature is not None:
       lcd.message ('T=%0.1fC\n' % temperature)
       lcd.message ('H=%0.1f%%' % humidity)
    else:
       print 'LCD Failed to get reading. Try again!'
    lcd.message ('  C=%0.1fC' % CaseTemp)  
    #lcd.message ('  M=%d' % moisture1)
    #GUI updates
    clock.set (datetime.now().time().strftime('%H:%M:%S '))
    if humidity is not None and temperature is not None:
       temp.set ('%0.1fC' % temperature)
       hum.set ('%0.1f%%' % humidity)
    else:
       print 'GUI Failed to get reading. Try again!'
    cputemp.set  ('%0.1fC' % CPUTemp)   
    casetemp.set ('%0.1fC' % CaseTemp)
    moist1.set ('%d' % moisture1)
    moist2.set ('%d' % moisture2)
    counter += 1
    root.after(1000, updates)
           
Zone1Timer()
Zone2Timer()
GH_FanAuto()
CaseFanAuto()
gui_widgets()
root.after(1000, updates)

root.mainloop() 
gpio.cleanup()	

