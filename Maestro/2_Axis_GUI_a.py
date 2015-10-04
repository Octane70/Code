import sys
sys.path.append("/home/pi/code/Maestro/modules")
import maestro
from Tkinter import *
import time
import tty
import termios

servo = maestro.Controller()

# Add Min, Mid & Max
servoMin = 1000
servoMid = 6000
servoMax = 9500

# Add servo increments
servoPan = 6000
servostepPan = 500

display = Tk()
display.title("Servo Control Display")
display.geometry("400x200+350+340")
L1 = Label(display, text="Tilt").grid(row=1,column=0,sticky=W)
L2 = Label(display, text="Pan").grid(row=2,column=0,sticky=W)
P1 = Scale(display, from_="%s" % servoMin, to="%s" % servoMax, orient=HORIZONTAL)
P1.grid(row=3,column=0,sticky=W)
T1 = Scale(display, from_="%s" % servoMin, to="%s" % servoMax)
T1.grid(row=3,column=2,sticky=W)

def servo_return():
  #servoPan = servoMid
  servo.setAccel(0,0)      #set servo 0 acceleration to 0
  servo.setTarget(0,6000)  #set servo to move to center position
  servo.setAccel(1,0)      #set servo 0 acceleration to 0
  servo.setTarget(1,6000)  #set servo to move to center position
  servo.close

def updates():
    global servoPan

    #servo1_left
    servoPan += servostepPan
    if servoPan > P1.get():
      servoPan = P1.get()
    servo.setAccel(0,0)      #set servo 0 acceleration to 0
    servo.setTarget(0,servoPan)  #set servo to move to center position
    servo.close
    print P1.get()
  
    #servo1_right
    servoPan -= servostepPan
    if servoPan < P1.get():
      servoPan = P1.get()
    servo.setAccel(0,0)      #set servo 0 acceleration to 0
    servo.setTarget(0,servoPan)  #set servo to move to center position
    servo.close
    print P1.get()
 
    #servo2_up
    servoPan += servostepPan
    if servoPan > T1.get():
      servoPan = T1.get()
    servo.setAccel(1,0)      #set servo 0 acceleration to 0
    servo.setTarget(1,servoPan)  #set servo to move to center position
    servo.close
    print T1.get()
    
    #servo2_down
    servoPan -= servostepPan
    if servoPan < T1.get():
      servoPan = T1.get()
    servo.setAccel(1,0)      #set servo 0 acceleration to 0
    servo.setTarget(1,servoPan)  #set servo to move to center position
    servo.close
    print T1.get()

    display.after(1000, updates)  
  

display.after(1000, updates) 
display.mainloop() 
