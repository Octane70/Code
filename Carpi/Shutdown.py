#Python 3.5.3

import sys
from tkinter import *

halt = Tk()
#halt.attributes(True)
#halt.overrideredirect(True)
halt.title("Shutdown?")
halt.geometry("250x50+200+200")
halt.resizable(width=FALSE, height=FALSE)

#Fonts
button_font = ('helvetica', 12, 'bold')

def shutdown_yes():
    halt.destroy()
    #root.destroy()
    #os.system("sudo shutdown -h now")
    print ("Shutdown")

#Buttons
B1 = Button(halt, text="YES", command=shutdown_yes,width=5, height=2)
B1.grid(row=1, column=0, sticky=NW)

B2 = Button(halt, text="NO", command=halt.destroy, width=5, height=2)
B2.grid(row=1, column=1, sticky=NE)

halt.mainloop()
