from tkinter import *
from datetime import datetime
import time
import os
import sys

#week_day = datetime.now().date().strftime("%A")

#Counter
counter = 0

root = Tk()
root.title("Datetime Test")
root.geometry('340x340+200+200')

date = Label(root)
label_font = ('helvetica', 12)
L1 = Label(root, text="Watering Days:").grid(row=1, column=0, columnspan=2, sticky=W)
L2 = Label(root, text="Zone1 Watering Time:").grid(row=3, column=0, columnspan=2, sticky=W)
L3 = Label(root, text="Zone1 Watering Timer:").grid(row=5, column=0, columnspan=2, sticky=W)
L4 = Label(root, text="Zone2 Watering Time:").grid(row=7, column=0, columnspan=2, sticky=W)
L5 = Label(root, text="Zone2 Watering Timer:").grid(row=9, column=0, columnspan=2, sticky=W)

#String Variables
date = StringVar()
time_str1 = StringVar()
time_str2 = StringVar()

def gui_widgets():
    Label(root, textvariable=date, font=('Times', 20, 'bold')).grid(row=0,column=0, columnspan=2 ,sticky=W)
    Entry(root, textvariable=time_str1, width=6).grid(row=6,column=1,sticky=W)
    Entry(root, textvariable=time_str2, width=6).grid(row=10,column=1,sticky=W)
    
# Watering Days
T1 = Text(root, width=10, height=1)
T1.insert("1.0", "Sunday\n") #Default value
T1.grid(row=2, column=0, sticky=W)

T2 = Text(root, width=10, height=1)
T2.insert("1.0","Wednesday\n") #Default value
T2.grid(row=2, column=1, sticky=W)

T3 = Text(root, width=10, height=1)
T3.insert("1.0", "Friday\n") #Default value
T3.grid(row=2, column=2, sticky=W)

#Zone_1 Watering Times
T4 = Text(root, width=7, height=1)
T4.insert("1.0", "1830\n") #Default value
T4.grid(row=4, column=0, sticky=W)

#Zone_1 Watering Timer
T5 = Text(root, width=7, height=1)
T5.insert("1.0", "120\n") #Default value
T5.grid(row=6, column=0, sticky=W)

#Zone_2 Watering Times
T6 = Text(root, width=7, height=1)
T6.insert("1.0", "1900\n") #Default value
T6.grid(row=8, column=0, sticky=W)

#Zone_2 Watering Timer
T7 = Text(root, width=7, height=1)
T7.insert("1.0", "120\n") #Default value
T7.grid(row=10, column=0, sticky=W)

# Get data
T1_get_data = T1.get("1.0",END)
T2_get_data = T2.get("1.0",END)
T3_get_data = T3.get("1.0",END)
T4_get_data = T4.get("1.0",END)
T5_get_data = T5.get("1.0",END)
T6_get_data = T6.get("1.0",END)
T7_get_data = T7.get("1.0",END)



frame1 = Frame(root, borderwidth=3, bg="yellow", relief="ridge", width=50, height=25) #Zone1
frame1.grid(row=12, column=0, columnspan=1, rowspan=1, sticky=W)  #Zone1



def Zone_1():
    a_day = T1_get_data
    b_day = T2_get_data
    c_day = T3_get_data
    day_1 = a_day.rstrip('\n')
    day_2 = b_day.rstrip('\n')
    day_3 = c_day.rstrip('\n')
    week_day = (datetime.now().date().strftime("%A"))
    
    if day_1 == week_day:
        frame1["bg"] = "red"
        Zone1Timer()
        print (day_1)
    elif day_2 == week_day:
        frame1["bg"] = "red"
        print (day_2)
    elif day_3 == week_day:
        frame1["bg"] = "red"
        print (day_3)        
    else:
        frame1["bg"] = "black"
    
    print (week_day)


b1 = Button(root, text="Test!", command=Zone_1, width=4, height=1)
b1.grid(row=11, column=0, sticky=W)

def Days():
    global T1_get_data
    global T2_get_data
    global T3_get_data
    T1_get_data = T1.get("1.0",END)
    T2_get_data = T2.get("1.0",END)
    T3_get_data = T3.get("1.0",END)
    T1_data = T1_get_data.rstrip('\n')
    T2_data = T2_get_data.rstrip('\n')
    T3_data = T3_get_data.rstrip('\n')
    #T9.insert("1.0", "G/H Fan Start %s\n" % T5_data)

b2 = Button(root, text="Enter", command=Days, width=4, height=1)
b2.grid(row=11, column=1, sticky=W)

def Zone1Timer():
    # start with 2 minutes --> 120 seconds
    for t in range(120, -1, -1):
        # format as 2 digit integers, fills with zero to the left
        # divmod() gives minutes, seconds
        sf = "{:02d}:{:02d}".format(*divmod(t, 60))
        #print(sf)  # test
        time_str1.set(sf)
        root.update()
        # delay one second
        time.sleep(1)
        

def updates():
    global date
    #GUI updates
    #date.set(datetime.now().time().strftime('%H:%M:%S '))
    #date.set (datetime.now().date().strftime("%A %B. %d %Y"))
    #date.set (datetime.now().date().strftime("%A %B, %d"))
    date.set (datetime.now().date().strftime("%A"))

    #Zone 1
    if frame1["bg"] == "red":
       Zone1Timer()
       
    #counter += 1   
    root.after(1000, updates)
    
gui_widgets() 
root.after(1000, updates)
root.mainloop()
