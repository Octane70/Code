import sys
from Tkinter import *
import time

display = Tk()
time1 = ''
display.title("Irrigation Display")
display.geometry("400x200+350+340")
L1 = Label(display, text="Temperature =").grid(row=0,column=0,sticky=W)
L2 = Label(display, text="Humidity =").grid(row=1,column=0,sticky=W)
L3 = Label(display, text="Moisture =").grid(row=2,column=0,sticky=W)
V1 = Label(display, text="25.2C").grid(row=0,column=1,sticky=W)
V2 = Label(display, text="50.5%").grid(row=1,column=1,sticky=W)
V3 = Label(display, text="700").grid(row=2,column=1,sticky=W)
B1 = Button(display, text ="Irrigation On") .grid(row=3,column=0,sticky=W)
B2 = Button(display, text ="Irrigation Off") .grid(row=3,column=1,sticky=W)
clock = Label(display, font=('times', 20, 'bold'), bg='green')
clock.grid(row=4,column=0,sticky=W)

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
