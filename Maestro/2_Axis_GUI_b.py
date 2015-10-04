import sys
sys.path.append("/home/pi/code/Maestro/modules")
<<<<<<< HEAD
#import maestro
from Tkinter import *
import time
#import tty
#import termios

#servo = maestro.Controller()
=======
import maestro
from Tkinter import *
import time
import tty
import termios

servo = maestro.Controller()
>>>>>>> a2c5f31ce77cdc38ae2ea20ef7b208667420489b

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
<<<<<<< HEAD

def servo1_pan(self):
=======
P1 = Scale(display, from_="%s" % servoMin, to="%s" % servoMax, orient=HORIZONTAL, command=servo1_left)
P1.grid(row=3,column=0,sticky=W)
T1 = Scale(display, from_="%s" % servoMin, to="%s" % servoMax, command=servo2_up)
T1.grid(row=3,column=2,sticky=W)

def servo1_left():
>>>>>>> a2c5f31ce77cdc38ae2ea20ef7b208667420489b
  global servoPan
  servoPan += servostepPan
  if servoPan > P1.get():
    servoPan = P1.get()
<<<<<<< HEAD
  #servo.setAccel(0,0)      #set servo 0 acceleration to 0
  #servo.setTarget(0,servoPan)  #set servo to move to center position
  #servo.close
  print P1.get()

P1 = Scale(display, from_="%s" % servoMin, to="%s" % servoMax, orient=HORIZONTAL, command=servo1_pan)
P1.grid(row=3,column=0,sticky=W)  
  
#def servo1_right():
  #global servoPan
  #servoPan -= servostepPan
  #if servoPan < P1.get():
    #servoPan = P1.get()
  #servo.setAccel(0,0)      #set servo 0 acceleration to 0
  #servo.setTarget(0,servoPan)  #set servo to move to center position
  #servo.close
  #print P1.get()
 
def servo2_tilt(self):
=======
  servo.setAccel(0,0)      #set servo 0 acceleration to 0
  servo.setTarget(0,servoPan)  #set servo to move to center position
  servo.close
  print P1.get()
  
def servo1_right():
  global servoPan
  servoPan -= servostepPan
  if servoPan < P1.get():
    servoPan = P1.get()
  servo.setAccel(0,0)      #set servo 0 acceleration to 0
  servo.setTarget(0,servoPan)  #set servo to move to center position
  servo.close
  print P1.get()
 
def servo2_up():
>>>>>>> a2c5f31ce77cdc38ae2ea20ef7b208667420489b
  global servoPan
  servoPan += servostepPan
  if servoPan > T1.get():
    servoPan = T1.get()
<<<<<<< HEAD
  #servo.setAccel(1,0)      #set servo 0 acceleration to 0
  #servo.setTarget(1,servoPan)  #set servo to move to center position
  #servo.close
  print T1.get()

T1 = Scale(display, from_="%s" % servoMin, to="%s" % servoMax, command=servo2_tilt)
T1.grid(row=3,column=2,sticky=W)

#def servo2_down():
  #global servoPan
  #servoPan -= servostepPan
  #if servoPan < T1.get():
    #servoPan = T1.get()
  #servo.setAccel(1,0)      #set servo 0 acceleration to 0
  #servo.setTarget(1,servoPan)  #set servo to move to center position
  #servo.close
  #print T1.get()

def servo_return():
  global servoMid
  servo.setAccel(0,0)         #set servo 0 acceleration to 0
  servo.setTarget(0,servoMid) #set servo to move to center position
  servo.setAccel(1,0)         #set servo 0 acceleration to 0
  servo.setTarget(1,servoMid) #set servo to move to center position
  servo.close
  print servoMid
=======
  servo.setAccel(1,0)      #set servo 0 acceleration to 0
  servo.setTarget(1,servoPan)  #set servo to move to center position
  servo.close
  print T1.get()
    
def servo2_down():
  global servoPan
  servoPan -= servostepPan
  if servoPan < T1.get():
    servoPan = T1.get()
  servo.setAccel(1,0)      #set servo 0 acceleration to 0
  servo.setTarget(1,servoPan)  #set servo to move to center position
  servo.close
  print T1.get()

def servo_return():
  #servoPan = servoMid
  servo.setAccel(0,0)      #set servo 0 acceleration to 0
  servo.setTarget(0,6000)  #set servo to move to center position
  servo.setAccel(1,0)      #set servo 0 acceleration to 0
  servo.setTarget(1,6000)  #set servo to move to center position
  servo.close
>>>>>>> a2c5f31ce77cdc38ae2ea20ef7b208667420489b
  

 
display.mainloop() 
