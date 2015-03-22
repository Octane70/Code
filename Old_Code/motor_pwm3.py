import RPi.GPIO as gpio
import time
import sys
import Tkinter as tk



def init():
    gpio.setmode(gpio.BOARD)
    gpio.setup(11, gpio.OUT) 
    gpio.setup(12, gpio.OUT) 
    gpio.setup(13, gpio.OUT) 
    gpio.setup(15, gpio.OUT) 
    gpio.setup(16, gpio.OUT) 
    gpio.setup(18, gpio.OUT) 
    
    gpio.output(11, True)
    gpio.output(12, True) 

def forward(tf):
    gpio.output(13, False)   
    gpio.output(15, True)
    gpio.output(18, True)    
    gpio.output(16, False)   
    time.sleep(tf)
    gpio.cleanup()
    
def backwards(tf):
    gpio.output(13, True)    
    gpio.output(15, False)   
    gpio.output(18, False)    
    gpio.output(16, True)   
    time.sleep(tf)
    gpio.cleanup()

def turn_left(tf):
    gpio.output(13, False)	 
    gpio.output(15, True)    
    gpio.output(18, False)  
    gpio.output(16, True)       
    time.sleep(tf)
    gpio.cleanup()

def turn_right(tf):
    gpio.output(13, True)	 
    gpio.output(15, False)   
    gpio.output(18, True)  
    gpio.output(16, False)   
    time.sleep(tf)
    gpio.cleanup()

def pevit_left(tf):
    gpio.output(13, False)	 
    gpio.output(15, True) 
    gpio.output(18, False)  
    gpio.output(16, True)  
    time.sleep(tf)
    gpio.cleanup()

def pevit_right(tf):
    gpio.output(13, True)	 
    gpio.output(15, False)   
    gpio.output(18, False)  
    gpio.output(16, True)     
    time.sleep(tf)
    gpio.cleanup()

   

def key_input(event):
    init()
    print 'Key:', event.char
    key_press = event.char
    sleep_time =0.020

    if key_press.lower() == 'w':
       forward(sleep_time)
    elif key_press.lower() == 's':
       backwards(sleep_time)
    elif key_press.lower() == 'a':
       turn_left(sleep_time)
    elif key_press.lower() == 'd':
       turn_right(sleep_time)
    elif key_press.lower() == 'q':
       pevit_left(sleep_time)
    elif key_press.lower() == 'e':
       pevit_right(sleep_time)
    else:
       print"Press W A S D Q E only" 


command = tk.Tk()
command.bind('<KeyPress>', key_input)
command.mainloop()
