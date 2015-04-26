#Garden_GUI_v0.1
import sys
from Tkinter import *
import time
import os

display = Tk()
time1 = ''
display.title("Irrigation Display")
display.geometry("800x650+350+350")
clock = Label(display, font=('times', 20, 'bold'))
clock.grid(row=0,column=0,sticky=W)
#Labels
L1 = Label(display, text="Temperature =").grid(row=1,column=0,sticky=W)
L2 = Label(display, text="Humidity =").grid(row=2,column=0,sticky=W)
L3 = Label(display, text="Moisture =").grid(row=3,column=0,sticky=W)
L4 = Label(display, text="25.2C").grid(row=1,column=1,sticky=W)
L5 = Label(display, text="50.5%").grid(row=2,column=1,sticky=W)
L6 = Label(display, text="700").grid(row=3,column=1,sticky=W)
L7 = Label(display, text ="Watering Times").grid(row=5, column=0, rowspan=1, columnspan=2)
L8 = Label(display, text ="Red is on & Black is off").grid(row=6, column=0, rowspan=1, columnspan=2)
L9 = Label(display, text ="Timer").grid(row=7, column=0, sticky=W)
L10 = Label(display, text ="Manual").grid(row=7, column=1, sticky=W)
L11 = Label(display, text ="Moisture").grid(row=11, column=0, sticky=W)
L12 = Label(display, text ="Manual").grid(row=11, column=1, sticky=W)
L13 = Label(display, text ="Morning Start").grid(row=15, column=0, sticky=W)
L12 = Label(display, text ="Morning Stop").grid(row=16, column=0, sticky=W)
L13 = Label(display, text ="Evening Start").grid(row=17, column=0, sticky=W)
L14 = Label(display, text ="Evening Stop").grid(row=18, column=0, sticky=W)
L15 = Label(display, text ="Moisture Min").grid(row=19, column=0, sticky=W)
L16 = Label(display, text ="Moisture Max").grid(row=20, column=0, sticky=W)
L17 = Label(display, text ="Camera 1:").grid(row=0, column=23, sticky=W)
L18 = Label(display, text ="Camera 2:").grid(row=18, column=23, sticky=W)
L19 = Label(display, text ="Shell Output:").grid(row=22, column=0, sticky=W)

#Text
T1 = Text(display, width=10, height=1)
T1.insert("1.0", "07:00\n")
T1.grid(row=15, column=1, sticky=W)

T2 = Text(display, width=10, height=1)
T2.insert("1.0", "07:30\n")
T2.grid(row=16, column=1, sticky=W)

T3 = Text(display, width=10, height=1)
T3.insert("1.0", "19:00\n")
T3.grid(row=17, column=1, sticky=W)

T4 = Text(display, width=10, height=1)
T4.insert("1.0", "19:30\n")
T4.grid(row=18, column=1, sticky=W)

T5 = Text(display, width=10, height=1)
T5.insert("1.0", "400\n")          
T5.grid(row=19, column=1, sticky=W)

T6 = Text(display, width=10, height=1)
T6.insert("1.0", "600\n")
T6.grid(row=20, column=1, sticky=W)

T7 = Text(display, width=28, height=10)
T7.grid(row=23, column=0, columnspan=2, rowspan=1, sticky=W)
 
#Buttons
def b1_on_off():
    if B1["text"] == "Off":
        B1["text"] = "On"
        print "Timer On"
        T7.insert("1.0", "Timer On\n")
    if frame2["bg"] == "black":
        frame2["bg"] = "red"
    else:
         B1["text"] = "Off"
         frame2["bg"] = "black"
         print "timer Off"
         T7.insert("1.0", "Timer Off\n")
B1=Button(display, text="Off", command=b1_on_off, width=4, height=1)
B1.grid(row=10, column=1, sticky=W)

def b2_on_off():
    if B2["text"] == "Off":
        B2["text"] = "On"
        print "Moisture On"
        T7.insert("1.0", "Moisture On\n")
    if frame3["bg"] == "black":
        frame3["bg"] = "red"
    else:
         B2["text"] = "Off"     
         frame3["bg"] = "black"
         print "Moisture Off"
         T7.insert("1.0", "Moisture Off\n")
B2=Button(display, text="Off", command=b2_on_off, width=4, height=1)
B2.grid(row=13, column=1, sticky=W)

def morning_start():
    T1_data = T1.get("1.0",END)
    T7.insert("1.0", "%s" % T1_data)
    print T1_data
B3=Button(display, text="Enter", command=morning_start, width=4, height=1)
B3.grid(row=15, column=3, sticky=W)

def morning_stop():
    T2_data = T2.get("1.0",END)
    T7.insert("1.0", "%s" % T2_data)
    print T2_data
B4=Button(display, text="Enter", command=morning_stop, width=4, height=1)
B4.grid(row=16, column=3, sticky=W)

def evening_start():
    T3_data = T3.get("1.0", END)
    T7.insert("1.0", "%s" % T3_data)
    print T3_data
B5=Button(display, text="Enter", command=evening_start, width=4, height=1)
B5.grid(row=17, column=3, sticky=W)

def evening_stop():
    T4_data = T4.get("1.0",END)
    T7.insert("1.0", "%s" % T4_data)
    print T4_data
B6=Button(display, text="Enter", command=evening_stop, width=4, height=1)
B6.grid(row=18, column=3, sticky=W)

def moisture_min():
    T5_data = T5.get("1.0",END)
    T7.insert("1.0", "%s" % T5_data)
    print T5_data
B7=Button(display, text="Enter", command=moisture_min, width=4, height=1)
B7.grid(row=19, column=3, sticky=W)

def moisture_max():
    T6_data = T6.get("1.0",END)
    T7.insert("1.0", "%s" % T6_data)
    print T6_data
B8=Button(display, text="Enter", command=moisture_max, width=4, height=1)
B8.grid(row=20, column=3, sticky=W)

#Frames
frame1 = Frame(display, borderwidth=5, bg="black", relief="ridge", width=180, height=4)
frame2 = Frame(display, borderwidth=3, bg="black", relief="ridge", width=50, height=25)
frame3 = Frame(display, borderwidth=3, bg="black", relief="ridge", width=50, height=25)
frame4 = Frame(display, borderwidth=5, bg="black", relief="ridge", width=200, height=4)
frame5 = Frame(display, borderwidth=5, bg="black", relief="ridge", width=200, height=4)
frame6 = Frame(display, borderwidth=7, relief="ridge", width=350, height=275)
frame7 = Frame(display, borderwidth=7, relief="ridge", width=350, height=275)
#Frame grids
frame1.grid(row=4, column=0, columnspan=2, rowspan=1, sticky=W)
frame2.grid(row=10, column=0, columnspan=2, rowspan=1, sticky=W)
frame3.grid(row=13, column=0, columnspan=2, rowspan=1, sticky=W)
frame4.grid(row=14, column=0, columnspan=2, rowspan=1, sticky=W)
frame5.grid(row=21, column=0, columnspan=2, rowspan=1, sticky=W)
frame6.grid(row=0, column=24, columnspan=2, rowspan=18, sticky=E)
frame7.grid(row=19, column=24, columnspan=2, rowspan=18, sticky=W)

def tick():
    global time1
    # get the current local time from the PC
    time2 = time.strftime('%H:%M:%S')
    # if time string has changed, update it
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)
    # calls itself every 200 milliseconds
    # to update the time display as needed
    # could use >200 ms, but display gets jerky
    clock.after(1, tick)
    
tick()
display.mainloop()
