import sys
from tkinter import *
import time
#import board
#import neopixel
import threading

#Neopixel
#pixel_pin = board.D18
#num_pixels = 12
#ORDER = neopixel.GRB
#pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2, auto_write=False,
   #                        pixel_order=ORDER)
#Colors
RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
WHITE = (255, 255, 255)
BLACK = (32, 32, 32)
ORANGE = (204, 102, 0)
OFF = (0, 0, 0)

switch = True

display = Tk()
time1 = ''
display.title("NeoPixel Display")
display.geometry("300x200+200+200")
L1 = Label(display, text="Pixel Loop").grid(row=0,column=0,columnspan=2,sticky=W)
L2 = Label(display, text="Pixel Light").grid(row=2,column=0,columnspan=2,sticky=W)
L3 = Label(display, text="Pixels Off").grid(row=4,column=0,columnspan=2,sticky=W)

window1 = window1 = Frame(display, borderwidth=5, relief="ridge", width=300, height=300) #Window1
window1.grid(row=0, column=3, columnspan=12, rowspan=12, sticky=NW) #Window1

#Pixel Frames
frame1 = Frame(window1, borderwidth=5, bg="red", relief="ridge", width=25, height=25)   #Pixel1 
frame2 = Frame(window1, borderwidth=5, bg="grey", relief="ridge", width=25, height=25) #Pixel2 
frame3 = Frame(window1, borderwidth=5, bg="grey", relief="ridge", width=25, height=25) #Pixel3
frame4 = Frame(window1, borderwidth=5, bg="grey", relief="ridge", width=25, height=25)   #Pixel4
frame5 = Frame(window1, borderwidth=5, bg="grey", relief="ridge", width=25, height=25) #Pixel5
frame6 = Frame(window1, borderwidth=5, bg="grey", relief="ridge", width=25, height=25) #Pixel6
frame7 = Frame(window1, borderwidth=5, bg="grey", relief="ridge", width=25, height=25)   #Pixel7
frame8 = Frame(window1, borderwidth=5, bg="grey", relief="ridge", width=25, height=25)   #Pixel8
frame9 = Frame(window1, borderwidth=5, bg="grey", relief="ridge", width=25, height=25)   #Pixel9
frame10 = Frame(window1, borderwidth=5, bg="grey", relief="ridge", width=25, height=25)  #Pixel10
frame11 = Frame(window1, borderwidth=5, bg="grey", relief="ridge", width=25, height=25)  #Pixel11
frame12 = Frame(window1, borderwidth=5, bg="grey", relief="ridge", width=25, height=25)  #Pixel12

#Pixel Frame Labels
#L1 = Label(frame1, text="1").grid(row=0,column=0,sticky=W)
#L1 = Label(frame2, text="2").grid(row=0,column=0,sticky=W)
#L1 = Label(frame3, text="3").grid(row=0,column=0,sticky=W)
#L1 = Label(frame4, text="4").grid(row=0,column=0,sticky=W)
#L1 = Label(frame5, text="5").grid(row=0,column=0,sticky=W)
#L1 = Label(frame6, text="6").grid(row=0,column=0,sticky=W)
#L1 = Label(frame7, text="7").grid(row=0,column=0,sticky=W)
#L1 = Label(frame8, text="8").grid(row=0,column=0,sticky=W)
#L1 = Label(frame9, text="9").grid(row=0,column=0,sticky=W)
#L1 = Label(frame10, text="10").grid(row=0,column=0,sticky=W)
#L1 = Label(frame11, text="11").grid(row=0,column=0,sticky=W)
#L1 = Label(frame12, text="12").grid(row=0,column=0,sticky=W)

#Frame grids
frame1.grid(row=0, column=3, columnspan=1, rowspan=1, sticky=W)  #Pixel1
frame2.grid(row=1, column=4, columnspan=1, rowspan=1, sticky=W)  #Pixel2
frame3.grid(row=2, column=5, columnspan=1, rowspan=1, sticky=W)  #Pixel3
frame4.grid(row=3, column=5, columnspan=1, rowspan=1, sticky=W)  #Pixel4
frame5.grid(row=4, column=4, columnspan=1, rowspan=1, sticky=W)  #Pixel5
frame6.grid(row=5, column=3, columnspan=1, rowspan=1, sticky=W) #Pixel6
frame7.grid(row=5, column=2, columnspan=1, rowspan=1, sticky=W)  #Pixel7
frame8.grid(row=4, column=1, columnspan=1, rowspan=1, sticky=W)  #Pixel8
frame9.grid(row=3, column=0, columnspan=1, rowspan=1, sticky=W)  #Pixel9
frame10.grid(row=2, column=0, columnspan=1, rowspan=1, sticky=W) #Pixel10
frame11.grid(row=1, column=1, columnspan=1, rowspan=1, sticky=W) #Pixel11
frame12.grid(row=0, column=2, columnspan=1, rowspan=1, sticky=W) #Pixel12

def pixel_loop():
   def run():
     while (switch == True):
        frame1["bg"] = "red"
        frame2["bg"] = "blue"
        frame3["bg"] = "red"
        frame4["bg"] = "red"
        frame5["bg"] = "blue"
        frame6["bg"] = "red"
        frame7["bg"] = "red"
        frame8["bg"] = "blue"
        frame9["bg"] = "red"
        frame10["bg"] = "red"
        frame11["bg"] = "blue"
        frame12["bg"] = "red"
        #pixels.show()
        time.sleep(1)

        frame1["bg"] = "grey"
        frame2["bg"] = "grey"
        frame3["bg"] = "grey"
        frame4["bg"] = "grey"
        frame5["bg"] = "grey"
        frame6["bg"] = "grey"
        frame7["bg"] = "grey"
        frame8["bg"] = "grey"
        frame9["bg"] = "grey"
        frame10["bg"] = "grey"
        frame11["bg"] = "grey"
        frame12["bg"] = "grey"
        #pixels.show()
        time.sleep(1)

        frame1["bg"] = "blue"
        frame2["bg"] = "red"
        frame3["bg"] = "blue"
        frame4["bg"] = "blue"
        frame5["bg"] = "red"
        frame6["bg"] = "blue"
        frame7["bg"] = "blue"
        frame8["bg"] = "red"
        frame9["bg"] = "blue"
        frame10["bg"] = "blue"
        frame11["bg"] = "red"
        frame12["bg"] = "blue"
        #pixels.show()
        time.sleep(1)

        frame1["bg"] = "grey"
        frame2["bg"] = "grey"
        frame3["bg"] = "grey"
        frame4["bg"] = "grey"
        frame5["bg"] = "grey"
        frame6["bg"] = "grey"
        frame7["bg"] = "grey"
        frame8["bg"] = "grey"
        frame9["bg"] = "grey"
        frame10["bg"] = "grey"
        frame11["bg"] = "grey"
        frame12["bg"] = "grey"
        #pixels.show()
        time.sleep(1)

        if switch == False:  
         break
   thread = threading.Thread(target=run)  
   thread.start()

def switchon():    
    global switch  
    switch = True  
    print ('switch on')
    pixel_loop()

B1 = Button(display, text ="On", command = switchon)
B1.grid(row=1,column=0,sticky=W)

def switchoff():    
    print ('switch off' ) 
    global switch  
    switch = False
     
B1 = Button(display, text ="Off", command = switchoff)
B1.grid(row=1,column=1,sticky=W)

def pixel_light():
    pixels.fill(WHITE)
    pixels.show()

B2 = Button(display, text ="On", command = pixel_light)
B2.grid(row=3,column=0,sticky=W)

def pixel_off():
    pixels.fill(OFF)
    pixels.show()

B3 = Button(display, text ="Off", command = pixel_off)
B3.grid(row=5,column=0,sticky=W)
 
display.mainloop()
