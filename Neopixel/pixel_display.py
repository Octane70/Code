import sys
from tkinter import *
import time
import board
import neopixel
import threading

#Neopixel
pixel_pin = board.D18
num_pixels = 12
ORDER = neopixel.GRB
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2, auto_write=False,
                           pixel_order=ORDER)
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
display.geometry("400x200+350+340")
L1 = Label(display, text="Pixel Loop").grid(row=0,column=0,sticky=W)

L2 = Label(display, text="Pixel Light").grid(row=2,column=0,sticky=W)

L3 = Label(display, text="Pixels Off").grid(row=4,column=0,sticky=W)


def pixel_loop():
   def run():
     while (switch == True):
        pixels[0] = (RED)
        pixels[1] = (BLUE)
        pixels[2] = (RED)
        pixels[3] = (RED)
        pixels[4] = (BLUE)
        pixels[5] = (RED)
        pixels[6] = (RED)
        pixels[7] = (BLUE)
        pixels[8] = (RED)
        pixels[9] = (RED)
        pixels[10] = (BLUE)
        pixels[11] = (RED)
        pixels.show()
        time.sleep(1)

        pixels.fill(OFF)
        pixels.show()
        time.sleep(1)

        pixels[0] = (BLUE)
        pixels[1] = (RED)
        pixels[2] = (BLUE)
        pixels[3] = (BLUE)
        pixels[4] = (RED)
        pixels[5] = (BLUE)
        pixels[6] = (BLUE)
        pixels[7] = (RED)
        pixels[8] = (BLUE)
        pixels[9] = (BLUE)
        pixels[10] = (RED)
        pixels[11] = (BLUE)
        pixels.show()
        time.sleep(1)

        pixels.fill(OFF)
        pixels.show()
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
