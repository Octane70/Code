import RPi.GPIO as gpio
import time
import sys
import Tkinter as tk



def init():
    gpio.setmode(gpio.BCM)
    gpio.setup(17, gpio.OUT) 
    gpio.setup(18, gpio.OUT) 
    gpio.setup(22, gpio.OUT) 
    gpio.setup(23, gpio.OUT) 
    gpio.setup(24, gpio.OUT) 
    gpio.setup(27, gpio.OUT) 
    
 

def forward(tf):
    gpio.output(17, True)
    gpio.output(18, True)
    gpio.output(27, True)   
    gpio.output(22, False)
    gpio.output(24, False)    
    gpio.output(23, True)   
    time.sleep(tf)
    gpio.cleanup()
    
def backwards(tf):
    gpio.output(17, True)
    gpio.output(18, True)
    gpio.output(27, False)    
    gpio.output(22, True)
    gpio.output(24, False)    
    gpio.output(23, True)    
    time.sleep(tf)
    gpio.cleanup()

def key_input(event):
    init()
    print 'Key:', event.char
    key_press = event.char
    sleep_time =0.030

    if key_press.lower() == 'w':
       forward(sleep_time)
    elif key_press.lower() == 's':
       backwards(sleep_time)

    else:
       print"Press W A S D Q E only" 


command = tk.Tk()
command.bind('<KeyPress>', key_input)
command.mainloop()
