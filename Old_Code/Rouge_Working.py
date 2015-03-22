import RPi.GPIO as gpio
import time
import sys
import Tkinter as tk



def init():
    gpio.setmode(gpio.BOARD)
    gpio.setup(16, gpio.OUT) #brown // 1ina
    gpio.setup(18, gpio.OUT) #Yellow // 1inb
    gpio.setup(32, gpio.OUT) #blue // 1pwm
    gpio.setup(12, gpio.OUT) #purple // 2pwm
    gpio.setup(15, gpio.OUT) #green // 2inb
    gpio.setup(11, gpio.OUT) #orange // 2ina
    
    gpio.output(12, True) #blue // 1pwm
    gpio.output(32, True) #purple // 2pwm

def forward(tf):
    gpio.output(16, False)   
    gpio.output(18, True)
    gpio.output(11, True)    
    gpio.output(15, False)   
    time.sleep(tf)
    gpio.cleanup()
    
def backwards(tf):
    gpio.output(16, True)    
    gpio.output(18, False)   
    gpio.output(11, False)    
    gpio.output(15, True)   
    time.sleep(tf)
    gpio.cleanup()

def turn_left(tf):
    gpio.output(16, False)	 
    gpio.output(18, True)    
    gpio.output(11, False)  
    gpio.output(15, True)       
    time.sleep(tf)
    gpio.cleanup()

def turn_right(tf):
    gpio.output(16, True)	 
    gpio.output(18, False)   
    gpio.output(11, True)  
    gpio.output(15, False)   
    time.sleep(tf)
    gpio.cleanup()

def pevit_left(tf):
    gpio.output(16, False)	 
    gpio.output(18, True) 
    gpio.output(11, False)  
    gpio.output(15, True)  
    time.sleep(tf)
    gpio.cleanup()

def pevit_right(tf):
    gpio.output(16, True)	 
    gpio.output(18, False)   
    gpio.output(11, True)  
    gpio.output(15, False)     
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
