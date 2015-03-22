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
    gpio.setwarnings(False)
    
    gpio.output(12, True) #purple // 1pwm
    gpio.output(32, True) #blue // 2pwm
     
    rh = gpio.PWM(12,120) #purple // 1pwm
    rh.start(50) #start right motor at 50% duty cycle
    rh.ChangeDutyCycle(0)
    
    
    lh = gpio.PWM(32,120) #blue // 2pwm
    lh.start(50) #start left motor at 50% duty cycle
    lh.ChangeDutyCycle(0)
       
    pause_time = 5
        
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

def pivot_left(tf):
    gpio.output(16, False)	 
    gpio.output(18, True) 
    gpio.output(11, False)  
    gpio.output(15, True)  
    time.sleep(tf)
    gpio.cleanup()

def pivot_right(tf):
    gpio.output(16, True)	 
    gpio.output(18, False)   
    gpio.output(11, True)  
    gpio.output(15, False)     
    time.sleep(tf)
    gpio.cleanup()

print ("w: for forward")
print ("s: for backward") 
print ("d: for right")
print ("a: for left")
print ("q: pivot right") 
print ("e: pivot left")  

def key_input(event):
    init()
    print 'Key:', event.char
    key_press = event.char
    sleep_time =0.030

    if key_press.lower() == 'w':
	   forward(sleep_time)
	   lh.ChangeDutyCycle(75)
	   rh.ChangeDutyCycle(75)
	           
    elif key_press.lower() == 's':
	   backwards(sleep_time)
	   lh.ChangeDutyCycle(75)
	   rh.ChangeDutyCycle(75)
	           
    elif key_press.lower() == 'a':
	   turn_left(sleep_time)
	   lh.ChangeDutyCycle(75)
	   rh.ChangeDutyCycle(75)
	           
    elif key_press.lower() == 'd':
	   turn_right(sleep_time)
	   lh.ChangeDutyCycle(75)
	   rh.ChangeDutyCycle(75)
	           
    elif key_press.lower() == 'q':
	   pivot_left(sleep_time)
 	   lh.ChangeDutyCycle(0)
	   rh.ChangeDutyCycle(75)
	          
    elif key_press.lower() == 'e':
	   pivot_right(sleep_time)
	   lh.ChangeDutyCycle(75)
	   rh.ChangeDutyCycle(0)
    else:
       print"Press W A S D Q E only" 


command = tk.Tk()
command.bind('<KeyPress>', key_input)
command.mainloop()
