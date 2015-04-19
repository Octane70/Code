import sys
from Tkinter import *

display = Tk()
display.title("Irrigation Display")
display.geometry("400x200+350+340")
L1 = Label(display, text="Temperature=").grid(row=0,column=0,sticky=W)
L2 = Label(display, text="Humidity=").grid(row=1,column=0,sticky=W)
L3 = Label(display, text="Moisture=").grid(row=2,column=0,sticky=W)
V1 = Label(display, text="25.2C").grid(row=0,column=1,sticky=W)
V2 = Label(display, text="50.5%").grid(row=1,column=1,sticky=W)
V3 = Label(display, text="700").grid(row=2,column=1,sticky=W)


display.mainloop()
