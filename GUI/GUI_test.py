import sys
from Tkinter import *

display = Tk()
display.title("Irrigation Display")
display.geometry("400x200+350+340")
L1 = Label(display, text="Temperature=").grid(row=0,column=0,sticky=W)
L2 = Label(display, text="Humidity=").grid(row=1,column=0,sticky=W)
L3 = Label(display, text="Moisture=").grid(row=2,column=0,sticky=W)
#L1.pack( side = LEFT)
#L2.pack( side = LEFT)
V1 = Label(display, text="25.2C", bd =5).grid(row=0,column=1,sticky=W)
V2 = Label(display, text="50.5%", bd =5).grid(row=1,column=1,sticky=W)
V3 = Label(display, text="700", bd =5).grid(row=2,column=1,sticky=W)
#E2 = Entry(top, bd =5)

#E1.pack(side = RIGHT)
#E2.pack(side = RIGHT)

display.mainloop()
