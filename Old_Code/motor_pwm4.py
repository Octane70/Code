import RPi.GPIO as gpio
import time
import sys
import Tkinter as tk



def init():
    gpio.setmode(gpio.BOARD)
    gpio.setup(19, gpio.OUT) 
    gpio.setup(21, gpio.OUT) 
    gpio.setup(22, gpio.OUT) 
    gpio.setup(23, gpio.OUT) 
    gpio.setup(24, gpio.OUT) 
    gpio.setup(26, gpio.OUT) 

    gpio.output(19, True)	 
    gpio.output(22, True)
    
def reset_all():
	#set all GPIOs to low
	gpio.output(21, gpio.False)
	gpio.output(23, gpio.False)
	gpio.output(24, gpio.False)
	gpio.output(26, gpio.False)    


def forward(tf):
    gpio.output(23, True)   
    gpio.output(21, False)    
    gpio.output(26, True)   
    gpio.output(24, False)    
    time.sleep(tf)
    gpio.cleanup()

def backwards(tf):
    gpio.output(23, False)    
    gpio.output(21, True)   
    gpio.output(26, False)    
    gpio.output(24, True)   
    time.sleep(tf)
    gpio.cleanup()

def turn_left(tf): 
    gpio.output(23, False)   
    gpio.output(21, True)
    gpio.output(26, True)    
    gpio.output(24, False)   
    time.sleep(tf)
    gpio.cleanup()

def turn_right(tf):
    gpio.output(23, True)   
    gpio.output(21, False)	
    gpio.output(26, False)   
    gpio.output(24, True)
    time.sleep(tf)
    gpio.cleanup()

def pevit_left(tf):
    gpio.output(23, False)  
    gpio.output(21, True)  
    gpio.output(26, False)  
    gpio.output(24, True)  
    time.sleep(tf)
    gpio.cleanup()

def pevit_right(tf):
    gpio.output(23, True)   
    gpio.output(21, False)  
    gpio.output(26, True)   
    gpio.output(24, False)  
    time.sleep(tf)
    gpio.cleanup()

   

def key_input(event):
    init()
    print 'Key:', event.char
    key_press = event.char
    sleep_time =0.090

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
