#Python 3.5.3

#---inputs---#
#Version
GUI_Version = 1.0

#CPU Temp min/max in celsius
cpu_fan_min= "45.0"
cpu_fan_max= "50.0"

#---Modules---#
from tkinter import *
from PIL import Image, ImageTk
import numpy as np
import RPi.GPIO as gpio
import sys
import os
import subprocess
#import commands
import socket
#import cv2
#import obd
import tkinter.filedialog
#from omxplayer import OMXPlayer
from time import sleep
import datetime

#Initiate gpio's for relay
gpio.setmode(gpio.BCM)
gpio.setup(17, gpio.OUT) # relay 1
gpio.setup(27, gpio.OUT) # relay 2
gpio.setup(22, gpio.OUT) # relay 3
gpio.setup(23, gpio.OUT) # relay 4
gpio.setwarnings(False)

#set relay gpio's to true
gpio.output(17, True) # relay 1
gpio.output(27, True) # relay 2
gpio.output(22, True) # relay 3
gpio.output(23, True) # relay 4

#relay ch1 on and off
def relay_ch1_on():
    gpio.output(17, False) #Relay ch1 on
def relay_ch1_off(): 
    gpio.output(17, True) #Relay ch1 off

#relay ch2 on and off
def relay_ch2_on():
    gpio.output(27, False) #Relay ch2 on
def relay_ch2_off(): 
    gpio.output(27, True) #Relay ch2 off

#relay ch3 on and off
def relay_ch3_on():
    gpio.output(22, False) #Relay ch3 on
def relay_ch3_off(): 
    gpio.output(22, True) #Relay ch3 off

#relay ch4 on and off
def relay_ch4_on():
    gpio.output(23, False) #Relay ch4 on
def relay_ch4_off(): 
    gpio.output(23, True) #Relay ch4 off
     
#OMXPlayer Wrapper
#file_path = '/home/pi/video.h264'
#player = OMXPlayer(file_path)

#---Root Window---#
root = Tk()
root.geometry("800x450+0+0")
root.minsize(800,450)
root.maxsize(800,450)
#root.overrideredirect(1)
root.title('Jeep XJ GUI')

#---Root Font---#
root_font = (5)

#---Window Tabs---#
window1 = Frame(root, borderwidth=5, relief="ridge", width=800, height=380)# Jeep Controls
window1.grid(row=1, column=0, columnspan=800, rowspan=1, sticky=NW) # Jeep Controls (default window)
window2 = Frame(root, borderwidth=5, relief="ridge", width=800, height=380) # Camera
window3 = Frame(root, borderwidth=5, relief="ridge", width=800, height=380) # Jeep Diagnostics
window4 = Frame(root, borderwidth=5, relief="ridge", width=800, height=380) # Rpi Diagnostics

window1.grid_propagate(False) # Prevent window1 from resizing
window2.grid_propagate(False) # Prevent window2 from resizing
window3.grid_propagate(False) # Prevent window3 from resizing
window4.grid_propagate(False) # Prevent window4 from resizing

#Root Dividers
RF1 = Frame(root, borderwidth=5, bg="grey", relief="ridge", width=7, height=70) #Divider1
RF1.grid(row=0, column=5, sticky=NW)  #Divider1 grid

def Window_1():
    window2.grid_remove()
    window3.grid_remove()
    window4.grid_remove()
    window1.grid(row=1, column=0, columnspan=800, rowspan=1, sticky=NW) 
        
B1=Button(root, text=" Jeep Controls", font= root_font, command= Window_1, width=12, height=3)
B1.grid(row=0, column=0, sticky=NW)

def Window_2():
    window1.grid_remove()
    window3.grid_remove()
    window4.grid_remove()
    window2.grid(row=1, column=0, columnspan=800, rowspan=1, sticky=NW) 

B2=Button(root, text="Camera", font= root_font, command= Window_2, width=12, height=3)
B2.grid(row=0, column=1, sticky=NW)

def Window_3():
    window1.grid_remove()
    window2.grid_remove()
    window4.grid_remove()
    window3.grid(row=1, column=0, columnspan=800, rowspan=2, sticky=NW) 
        
B3=Button(root, text="Jeep Diagnostics", font= root_font, command= Window_3, width=12, height=3)
B3.grid(row=0, column=3, sticky=NW)

def Window_4():
    window1.grid_remove()
    window2.grid_remove()
    window3.grid_remove()
    window4.grid(row=1, column=0, columnspan=800, rowspan=2, sticky=NW) 
    
B4=Button(root, text="Rpi Status", font= root_font, command= Window_4, width=12, height=3)
B4.grid(row=0, column=4, sticky=NW)

def Minimize():
    root.iconify()
    print ("Minimize")
    
B5=Button(root, text="Minimize", font= root_font, command= Minimize, width=7, height=3)
B5.grid(row=0, column=6, sticky=NW)

def Close():
    root.destroy()
    print ("Close")
    
B5=Button(root, text="Close", font= root_font, command= Close, width=7, height=3)
B5.grid(row=0, column=7, sticky=NW)

#---Jeep Controls---Window1 Layout---#
#------------------------------------#

#Window1 Labels
W1_font = ("helvetica", 10, "bold")
W1L1 = Label(window1, text="Door Locks:", font= W1_font).grid(row=1, column=0, columnspan=2, sticky=W)
W1L1 = Label(window1, text="Vehicle Start:", font= W1_font).grid(row=4, column=0, columnspan=2, sticky=W)

#Window1 Frames
W1F1 = Frame(window1, borderwidth=3, bg="green", relief="ridge", width=123, height=25) # Door lock frame
W1F1.grid(row=2, column=0, columnspan=1, rowspan=1, sticky=W) # Door lock grid
W1F2 = Frame(window1, borderwidth=3, bg="green", relief="ridge", width=123, height=25) # Door unlock frame
W1F2.grid(row=2, column=1, columnspan=1, rowspan=1, sticky=W) # Door unlock grid
W1F3 = Frame(window1, borderwidth=3, bg="green", relief="ridge", width=123, height=25) # Vehicle start frame
W1F3.grid(row=5, column=0, columnspan=1, rowspan=1, sticky=W) # Vehicle start grid
W1F4 = Frame(window1, borderwidth=3, bg="green", relief="ridge", width=123, height=25) # Vehicle stop frame
W1F4.grid(row=5, column=1, columnspan=1, rowspan=1, sticky=W) # vehicle stop grid

#Window1 Buttons
#Door Lock/Unlock
def Door_Lock_Press(event):
    relay_ch1_on()
    W1F1.config(bg = "red")
    print ("Door Lock press")
    
def Door_Lock_Release(event):
    relay_ch1_off()
    W1F1.config(bg = "green")
    print ("Door Lock release")
    
W1B1=Button(window1, text="Lock", font= W1_font, width=12, height=3)
W1B1.grid(row=3, column=0, sticky=NW)
W1B1.bind("<ButtonPress>", Door_Lock_Press)
W1B1.bind("<ButtonRelease>", Door_Lock_Release)

def Door_Unlock_Press(event):
    relay_ch2_on()
    W1F2.config(bg = "red")
    print ("Door Unlock press")

def Door_Unlock_Release(event):
    relay_ch2_off()
    W1F2.config(bg = "green")
    print ("Door Unlock release")    
    
W1B2=Button(window1, text="UnLock", font= W1_font, width=12, height=3)
W1B2.grid(row=3, column=1, sticky=NW)
W1B2.bind("<ButtonPress>", Door_Unlock_Press)
W1B2.bind("<ButtonRelease>", Door_Unlock_Release)

#Auto Start/Stop
def Car_Start_Press(event):
    relay_ch3_on()
    W1F3.config(bg = "red")
    print ("Car Start press")

def Car_Start_Release(event):
    relay_ch3_off()
    W1F3.config(bg = "green")
    print ("Car Start release")    
    
W1B3=Button(window1, text="Start", font= W1_font, width=12, height=3)
W1B3.grid(row=6, column=0, sticky=NW)
W1B3.bind("<ButtonPress>", Car_Start_Press)
W1B3.bind("<ButtonRelease>", Car_Start_Release)

def Car_Stop_Press(event):
    relay_ch4_on()
    W1F4.config(bg = "red")
    print ("Car Stop press")

def Car_Stop_Release(event):
    relay_ch4_off()
    W1F4.config(bg = "green")
    print ("Car Stop release")    
    
W1B4=Button(window1, text="Stop", font= W1_font, width=12, height=3)
W1B4.grid(row=6, column=1, sticky=NW)
W1B4.bind("<ButtonPress>", Car_Stop_Press)
W1B4.bind("<ButtonRelease>", Car_Stop_Release)

#---Camera---Window2 Layout---#
#-----------------------------#

#Window2 Frames
CapFrame = Frame(window2, borderwidth=5, relief="ridge", width=642, height=370) # Camera capframe
CapFrame.grid(row=1, column=0, sticky=NW) # Camera capframe grid
W2F2 = Frame(window2, borderwidth=5, relief="ridge", width=151, height=370) # Button frame
W2F2.grid(row=1, column=1, sticky=NW) # Button frame grid
W2F3 = Frame(W2F2, borderwidth=3, bg="green", relief="ridge", width=69, height=41) # Capture frame
W2F3.grid(row=1, column=0, sticky=NW) # Capture frame grid
W2F4 = Frame(W2F2, borderwidth=3, bg="green", relief="ridge", width=69, height=41) # Record frame
W2F4.grid(row=3, column=0, sticky=NW) # Record frame grid

#Prevent frames from resizing
CapFrame.grid_propagate(False) # Prevent camera capframe from resizing
W2F2.grid_propagate(False) # Prevent button frame from resizing

#Divider Frames
W2F5 = Frame(W2F2, borderwidth=5, bg="grey", relief="ridge", width=141, height=4) #Divider1
W2F5.grid(row=2, column=0, columnspan=150, rowspan=1, sticky=W)  #Divider1 grid
W2F6 = Frame(W2F2, borderwidth=5, bg="grey", relief="ridge", width=141, height=4) #Divider2
W2F6.grid(row=5, column=0, columnspan=150, rowspan=1, sticky=W)  #Divider2 grid
W2F7 = Frame(W2F2, borderwidth=5, bg="grey", relief="ridge", width=141, height=4) #Divider3
W2F7.grid(row=7, column=0, columnspan=150, rowspan=1, sticky=W)  #Divider3 grid
W2F8 = Frame(W2F2, borderwidth=5, bg="grey", relief="ridge", width=141, height=4) #Divider4
W2F8.grid(row=9, column=0, columnspan=150, rowspan=1, sticky=W)  #Divider4 grid

#Window2 Labels
W2L1 = Label(W2F2, text="Folders").grid(row=6, column=0, columnspan=2)

#Capture Video Frames
lmain = Label(CapFrame, width=630, height=358)
lmain.grid(row=0, column=0, sticky=NW)
#cap = cv2.VideoCapture(0)

#def show_frame():
    #_, frame = cap.read()
    #frame = cv2.flip(frame, 1)
    #cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    #img = Image.fromarray(cv2image)
    #imgtk = ImageTk.PhotoImage(image=img)
    #lmain.imgtk = imgtk
    #lmain.configure(image=imgtk)
    #lmain.after(10, show_frame)

#img = cv2.imread('max.jpg',1)    
   
#Window2 Buttons
#Take a Picture
def Capture_Frame_Press(event):
    os.chdir ("/home/pi/Pictures")
    ts = datetime.datetime.now()
    filename = "{}.jpg".format(ts.strftime("%Y-%m-%d_%H-%M-%S"))
    W2F3.config(bg = "red")
    print ("Capture Press")
    if W2F3["bg"] == "red":
       _, saveimage= cap.read()
       cv2.imwrite(filename, saveimage)

def Capture_Frame_Release(event):
    W2F3.config(bg = "green")
    print ("Capture Release")   
        
W2B1=Button(W2F2, text="Capture", width=5, height=2)
W2B1.grid(row=1, column=1, sticky=NW)
W2B1.bind("<ButtonPress>", Capture_Frame_Press)
W2B1.bind("<ButtonRelease>", Capture_Frame_Release)

#Record Start/Stop
def Record_Start():
    #camera.start_recording('/home/pi/video.h264')
    W2F4["bg"] = "red"
    print ("Record")
    
W2B2=Button(W2F2, text="Record", command= Record_Start, width=5, height=2)
W2B2.grid(row=3, column=1, sticky=NW)

def Record_Stop():
    #camera.stop_recording()
    W2F4["bg"] = "green"
    print ("Stop Record")
    
W2B3=Button(W2F2, text="Stop", command= Record_Stop, width=5, height=2)
W2B3.grid(row=4, column=1, sticky=NW)

#Folders
def Picture_Folder():
    tkinter.filedialog.askopenfilename(initialdir='/home/pi/Pictures')
    print ("Picture folder")
    
W2B4=Button(W2F2, text="Pictures", command= Picture_Folder, width=5, height=2)
W2B4.grid(row=8, column=0, sticky=NW)

def Video_Folder():
    tkinter.filedialog.askopenfilename(initialdir='/home/pi/Videos')
    print ("Video Folder")
    
W2B5=Button(W2F2, text="Videos", command= Video_Folder, width=5, height=2)
W2B5.grid(row=8, column=1, sticky=NW)

#---Jeep Diagnostics---Window3 Layout---#
#---------------------------------------#

#Window3 Labels
W3_font = ('helvetica', 12, 'bold')
W3L1 = Label(window3, text="Perameters", font=W3_font).grid(row=1, column=0, sticky=W)
W3L2 = Label(window3, text="RPM= 2000", font=W3_font).grid(row=3, column=0, sticky=W)
W3L2 = Label(window3, text="Coolant Temp= 100", font=W3_font).grid(row=4, column=0, sticky=W)
W3L4 = Label(window3, text="Intake Press= 20", font=W3_font).grid(row=5, column=0, sticky=W)
W3L4 = Label(window3, text="Intake Temp= 40", font=W3_font).grid(row=6, column=0, sticky=W)

#Window3 Dividers
W3F1 = Frame(window3, borderwidth=5, bg="grey", relief="ridge", width=141, height=4) #Divider1
W3F1.grid(row=2, column=0, columnspan=100, rowspan=1, sticky=W)  #Divider1 grid

#---Rpi Status---Window4 Layout---#
#-------------------------------#

#Window4 Labels
W4_font = ('helvetica', 12, 'bold')
W4L1 = Label(window4, text="Hostname:", font=W4_font).grid(row=1, column=0, sticky=W)
W4L2 = Label(window4, text="GUI Version:", font=W4_font).grid(row=2, column=0, sticky=W)
W4L3 = Label(window4, text="IP Address:", font=W4_font).grid(row=3, column=0, sticky=W)
W4L4 = Label(window4, text="CPU Temp:", font=W4_font).grid(row=4, column=0, sticky=W)
W4L5 = Label(window4, text="CPU Fan Status:", font=W4_font).grid(row=5, column=0, sticky=W)

#Window4 Variables
cputemp = StringVar()

#Rpi3 hostname & IP Address
host = socket.gethostname()
ipnum = subprocess.check_output(["hostname", "-I"]).split()[0]

def rpi_widgets():
    global host
    global ipnum
    global GUI_Version
    global cpu_fan_default
    W4L6 = Label(window4, text=host, font=W4_font).grid(row=1,column=1,sticky=W)
    W4L7 = Label(window4, text=GUI_Version, font=W4_font).grid(row=2,column=1,sticky=W)
    W4L8 = Label(window4, text=ipnum, font=W4_font).grid(row=3,column=1,sticky=W)
    W4L9 = Label(window4, textvariable=cputemp, font=W4_font).grid(row=4,column=1,sticky=W)

W4L10 = Label(window4, text="Fan Off", font=W4_font)
W4L10.grid(row=5,column=1,sticky=W)
    
# Rpi3 CPU Temperature
def getTempCPU():
    temp = subprocess.getoutput("/opt/vc/bin/vcgencmd measure_temp")
    initTempPos = str(temp).find("=")
    finishTempPos = str(temp).find("'")
    temp = str(temp)[initTempPos+1:finishTempPos]
    try:
        temp_num = float(temp)
        return temp_num
    except:
        print ("Unable to transform to float")

# CPU Fan on/off
def cpu_fan():
    global cpu_fan_min
    global cpu_fan_max
    global getTempCPU
    cpu_fan_data = getTempCPU()
    cpu_fan_temp = ('%1.0f' % cpu_fan_data)
    if cpu_fan_temp >= cpu_fan_max:   
       #relay_ch3_on()
       if W4L10["text"] == "Fan Off":
          W4L10["text"] = "Fan On"
          print ("Case Fan On")
    elif cpu_fan_temp <= cpu_fan_min:
       #relay_ch3_off()
        if W4L10["text"] == "Fan On":
           W4L10["text"] = "Fan Off"
           print ("Case Fan Off")

def rpi_updates():
    global getTempCPU
    CPUTemp = getTempCPU()
    cputemp.set  ('%0.1fC' % CPUTemp)
    root.after(1000, rpi_updates)
    
#show_frame() 
rpi_widgets()
cpu_fan()
root.after(1000, rpi_updates)
root.mainloop()
gpio.cleanup()	
