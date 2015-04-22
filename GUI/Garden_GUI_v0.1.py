#Garden_GUI_v0.1
import sys
from Tkinter import *
import time

display = Tk()
time1 = ''
display.title("Irrigation Display")
display.geometry("500x500+350+340")
clock = Label(display, font=('times', 20, 'bold'))
clock.grid(row=0,column=0,sticky=W)
#Labels
L1=Label(display, text="Temperature =").grid(row=1,column=0,sticky=W)
L2=Label(display, text="Humidity =").grid(row=2,column=0,sticky=W)
L3=Label(display, text="Moisture =").grid(row=3,column=0,sticky=W)
L4=Label(display, text="25.2C").grid(row=1,column=1,sticky=W)
L5=Label(display, text="50.5%").grid(row=2,column=1,sticky=W)
L6=Label(display, text="700").grid(row=3,column=1,sticky=W)
L7=Label(display, text ="Watering Times").grid(row=5, column=0, rowspan=1, columnspan=2)
L8=Label(display, text ="Red is on & Black is off").grid(row=6, column=0, rowspan=1, columnspan=2)
L9=Label(display, text ="Timer").grid(row=7, column=0, sticky=W)
L10=Label(display, text ="Moisture").grid(row=7, column=1, sticky=W)
L11=Label(display, text ="Morning Start").grid(row=12, column=0, sticky=W)
L11=Label(display, text ="Morning Stop").grid(row=13, column=0, sticky=W)
L12=Label(display, text ="Evening Start").grid(row=14, column=0, sticky=W)
L13=Label(display, text ="Evening Stop").grid(row=15, column=0, sticky=W)
L14=Label(display, text ="Moisture Min").grid(row=16, column=0, sticky=W)
L15=Label(display, text ="Moisture Max").grid(row=17, column=0, sticky=W)

#T1=Text(display, text="7:00").grid(row=12, column=1, sticky=W)

#Frames
frame1 = Frame(display, borderwidth=5, bg="black", relief="ridge", width=160, height=4)
frame2 = Frame(display, borderwidth=3, bg="red", relief="ridge", width=50, height=25)
frame3 = Frame(display, borderwidth=3, bg="red", relief="ridge", width=50, height=25)
frame4 = Frame(display, borderwidth=5, bg="black", relief="ridge", width=160, height=4)
#frame grids
frame1.grid(row=4, column=0, columnspan=2, rowspan=1, sticky=W)
frame2.grid(row=10, column=0, columnspan=2, rowspan=1, sticky=W)
frame3.grid(row=10, column=1, columnspan=2, rowspan=1, sticky=W)
frame4.grid(row=11, column=0, columnspan=2, rowspan=1, sticky=W)

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
