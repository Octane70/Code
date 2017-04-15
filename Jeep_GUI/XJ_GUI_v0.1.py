from tkinter import *
import RPi.GPIO as gpio
import sys
import os
import subprocess
import socket
from picamera import PiCamera
from time import sleep

#Initiate gpio's for relay
gpio.setmode(gpio.BCM)
gpio.setup(17, gpio.OUT) # relay 1
gpio.setup(27, gpio.OUT) # relay 2
gpio.setwarnings(False)

#set relay gpio's to false
gpio.output(17, False) # relay 1
gpio.output(27, False) # relay 2

#relay ch1 on and off
def relay_ch1_on():
    gpio.output(17, True) #Relay ch1 on
def relay_ch1_off(): 
    gpio.output(17, False) #Relay ch1 off

#relay ch2 on and off
def relay_ch2_on():
    gpio.output(27, True) #Relay ch2 on
def relay_ch2_off(): 
    gpio.output(27, False) #Relay ch2 off
    
#PiCamera Overlay
camera = PiCamera()
camera.preview_fullscreen = False
camera.resolution = (1920, 1080)
camera.preview_window = (10, -6, 633, 633)

#---Root Window---#
root = Tk()
root.geometry("800x480+0+0")
root.minsize(800,480)
root.maxsize(800,480)
root.title('Jeep XJ GUI v0.1')

#---Window Tabs---#
window1 = Frame(root, borderwidth=5, relief="ridge", width=800, height=424)# Jeep Controls
window1.grid(row=1, column=0, columnspan=800, rowspan=1, sticky=NW) # Jeep Controls (default window)
window2 = Frame(root, borderwidth=5, relief="ridge", width=800, height=424) # Camera
window3 = Frame(root, borderwidth=5, relief="ridge", width=800, height=424) # Jeep Diagnostics
window4 = Frame(root, borderwidth=5, relief="ridge", width=800, height=424) # RPI Zero

window1.grid_propagate(False) # Prevent window1 from resizing
window2.grid_propagate(False) # Prevent window2 from resizing
window3.grid_propagate(False) # Prevent window3 from resizing
window4.grid_propagate(False) # Prevent window4 from resizing

def Window_1():
    camera.stop_preview() 
    window2.grid_remove()
    window3.grid_remove()
    window4.grid_remove()
    window1.grid(row=1, column=0, columnspan=800, rowspan=1, sticky=NW) 
        
B1=Button(root, text=" Jeep Controls", command= Window_1, width=15, height=3)
B1.grid(row=0, column=0, sticky=NW)

def Window_2():
    camera.start_preview()
    window1.grid_remove()
    window3.grid_remove()
    window4.grid_remove()
    window2.grid(row=1, column=0, columnspan=800, rowspan=1, sticky=NW) 

B1=Button(root, text="Camera", command= Window_2, width=15, height=3)
B1.grid(row=0, column=1, sticky=NW)

def Window_3():
    camera.stop_preview() 
    window1.grid_remove()
    window2.grid_remove()
    window4.grid_remove()
    window3.grid(row=1, column=0, columnspan=800, rowspan=2, sticky=NW) 
        
B1=Button(root, text="Jeep Diagnostics", command= Window_3, width=15, height=3)
B1.grid(row=0, column=3, sticky=NW)

def Window_4():
    camera.stop_preview() 
    window1.grid_remove()
    window2.grid_remove()
    window3.grid_remove()
    window4.grid(row=1, column=0, columnspan=800, rowspan=2, sticky=NW) 
    
B1=Button(root, text="RPI Zero", command= Window_4, width=15, height=3)
B1.grid(row=0, column=4, sticky=NW)

#--Window1 Layout--#
#Window1 Labels
W1L1 = Label(window1, text="Door Locks:").grid(row=1, column=0, columnspan=2, sticky=W)
W1L1 = Label(window1, text="Vehicle Start:").grid(row=4, column=0, columnspan=2, sticky=W)

#Window1 Frames
W1F1 = Frame(window1, borderwidth=3, bg="green", relief="ridge", width=65, height=25) # Door lock frame
W1F1.grid(row=2, column=0, columnspan=1, rowspan=1, sticky=W) # Door lock grid
W1F2 = Frame(window1, borderwidth=3, bg="green", relief="ridge", width=65, height=25) # Door unlock frame
W1F2.grid(row=2, column=1, columnspan=1, rowspan=1, sticky=W) # Door unlock grid
W1F3 = Frame(window1, borderwidth=3, bg="green", relief="ridge", width=65, height=25) # Vehicle start frame
W1F3.grid(row=5, column=0, columnspan=1, rowspan=1, sticky=W) # Vehicle start grid
W1F4 = Frame(window1, borderwidth=3, bg="green", relief="ridge", width=65, height=25) # Vehicle stop frame
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
    
W1B1=Button(window1, text="Lock", width=8, height=2)
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
    
W1B2=Button(window1, text="UnLock", width=8, height=2)
W1B2.grid(row=3, column=1, sticky=NW)
W1B2.bind("<ButtonPress>", Door_Unlock_Press)
W1B2.bind("<ButtonRelease>", Door_Unlock_Release)

#Auto Start/Stop
def Car_Start_Press(event):
    W1F3.config(bg = "red")
    print ("Car Start press")

def Car_Start_Release(event):
    W1F3.config(bg = "green")
    print ("Car Start release")    
    
W1B3=Button(window1, text="Start", width=8, height=2)
W1B3.grid(row=6, column=0, sticky=NW)
W1B3.bind("<ButtonPress>", Car_Start_Press)
W1B3.bind("<ButtonRelease>", Car_Start_Release)

def Car_Stop_Press(event):
    W1F4.config(bg = "red")
    print ("Car Stop press")

def Car_Stop_Release(event):
    W1F4.config(bg = "green")
    print ("Car Stop release")    
    
W1B4=Button(window1, text="Stop", width=8, height=2)
W1B4.grid(row=6, column=1, sticky=NW)
W1B4.bind("<ButtonPress>", Car_Stop_Press)
W1B4.bind("<ButtonRelease>", Car_Stop_Release)

#--Window2 Layout--#
#Window2 Frames
W2F1 = Frame(window2, borderwidth=5, relief="ridge", width=640, height=364) # Camera frame
W2F1.grid(row=1, column=0, sticky=NW) # Camera frame grid
W2F1.grid_propagate(False) # Prevent camera frame from resizing
W2F2 = Frame(window2, borderwidth=5, relief="ridge", width=150, height=415) # Button frame
W2F2.grid(row=1, column=1, sticky=NW) # Button frame grid
W2F2.grid_propagate(False) # Prevent button frame from resizing
W2F3 = Frame(W2F2, borderwidth=3, bg="green", relief="ridge", width=69, height=41) # Capture frame
W2F3.grid(row=1, column=2, columnspan=1, rowspan=1, sticky=NW) # Capture frame grid
W2F4 = Frame(W2F2, borderwidth=3, bg="green", relief="ridge", width=138, height=25) # Record frame
W2F4.grid(row=3, column=1, columnspan=150, rowspan=1, sticky=NW) # Record frame grid

#Divider Frames
W2F5 = Frame(W2F2, borderwidth=5, bg="grey", relief="ridge", width=141, height=4) #Divider1
W2F5.grid(row=2, column=0, columnspan=150, rowspan=1, sticky=W)  #Divider1 grid
W2F6 = Frame(W2F2, borderwidth=5, bg="grey", relief="ridge", width=141, height=4) #Divider2
W2F6.grid(row=5, column=0, columnspan=150, rowspan=1, sticky=W)  #Divider2 grid
W2F7 = Frame(W2F2, borderwidth=5, bg="grey", relief="ridge", width=141, height=4) #Divider3
W2F7.grid(row=7, column=0, columnspan=150, rowspan=1, sticky=W)  #Divider3 grid
   
#Window2 Buttons
#Take a Picture
def Capture_Frame_Press(event):
    W2F3.config(bg = "red")
    print ("Capture Press")
    camera.resolution = (1920, 1080)
    camera.framerate = 15
    sleep(2)
    camera.capture('/home/pi/Desktop/max.jpg')


def Capture_Frame_Release(event):
    W2F3.config(bg = "green")
    print ("Capture Release")   
        
W2B1=Button(W2F2, text="Capture", width=5, height=2)
W2B1.grid(row=1, column=1, sticky=NW)
W2B1.bind("<ButtonPress>", Capture_Frame_Press)
W2B1.bind("<ButtonRelease>", Capture_Frame_Release)

#Record Start/Stop
def Record_Start():
    camera.start_recording('/home/pi/video.h264')
    W2F4["bg"] = "red"
    print ("Record")
    
W2B2=Button(W2F2, text="Record", command= Record_Start, width=5, height=2)
W2B2.grid(row=4, column=1, sticky=NW)

def Record_Stop():
    camera.stop_recording()
    W2F4["bg"] = "green"
    print ("Stop Record")
    
W2B3=Button(W2F2, text="Stop", command= Record_Stop, width=5, height=2)
W2B3.grid(row=4, column=2, sticky=NW)

#Forward/Rewind
def Skip_Back():
    print ("Skip Back")
    
W2B4=Button(W2F2, text="Skip.R", command= Skip_Back, width=5, height=2)
W2B4.grid(row=6, column=1, sticky=NW)

def Skip_Forward():
    print ("Skip Forward")
    
W2B5=Button(W2F2, text="Skip.F", command= Skip_Forward, width=5, height=2)
W2B5.grid(row=6, column=2, sticky=NW)

def Open_Folder():
    print ("Open Folder")
    
W2B6=Button(W2F2, text="Open Folder", command= Open_Folder, width=14, height=1)
W2B6.grid(row=8, column=1, columnspan=150, sticky=NW)

#--Window3 Layout--#
#Window3 Labels
W3L1 = Label(window3, text="Jeep Diagnostics").grid(row=1, column=0, sticky=W)

#--Window4 Layout--#
#Window4 Labels
W4_font = ('helvetica', 12, 'bold')
W4L1 = Label(window4, text="CPU Temp:", font=W4_font).grid(row=1, column=0, sticky=W)
W4L2 = Label(window4, text="HostName:", font=W4_font).grid(row=2, column=0, sticky=W)
W4L2 = Label(window4, text="IP Address:", font=W4_font).grid(row=3, column=0, sticky=W)

cputemp = StringVar()

#Zero hostname & IPAddres
host = socket.gethostname()
ipnum = subprocess.check_output(["hostname", "-I"])

def zero_widgets():
    global host
    global ipnum
    W4L3 = Label(window4, textvariable=cputemp, font=W4_font).grid(row=1,column=1,sticky=W)
    W4L3 = Label(window4, text=host, font=W4_font).grid(row=2,column=1,sticky=W)
    W4L3 = Label(window4, text=ipnum, font=W4_font).grid(row=3,column=1,rowspan=8,sticky=W)
    
# RPI CPU Temperature
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

def Zero_Updates():
    global getTempCPU
    CPUTemp = getTempCPU()
    cputemp.set  ('%0.1fC' % CPUTemp)
    root.after(1000, Zero_Updates)
    

zero_widgets()
root.after(1000, Zero_Updates)
root.mainloop()
camera.stop_preview()
gpio.cleanup()	
