import sys
sys.path.append("/home/pi/code/Maestro/modules")
#import maestro
from Tkinter import *
import time
#import tty
#import termios

#servo = maestro.Controller()

# Add Min, Mid & Max
servoMin = 1000
servoMid = 6000
servoMax = 9500

# Add servo increments
servoPan = 6000
servostepPan = 500

display = Tk()
display.title("Servo Control Display")
display.geometry("650x450+350+340")
L1 = Label(display, text="Tilt").grid(row=0,column=2,sticky=E)
L2 = Label(display, text="Pan").grid(row=3,column=0,sticky=W)
F1 = Frame(display, borderwidth=7, relief="ridge", width=450, height=350)
F1.grid(row=2, column=2, sticky=W)

#Pan using scale
def servo1_pan(self):
  global servoPan
  servoPan += servostepPan
  if servoPan > P1.get():
    servoPan = P1.get()
  #servo.setAccel(0,0)      #set servo 0 acceleration to 0
  #servo.setTarget(0,servoPan)  #set servo to move to center position
  #servo.close
  print P1.get()

P1 = Scale(display, from_="%s" % servoMin, to="%s" % servoMax, orient=HORIZONTAL, command=servo1_pan)
P1.grid(row=3,column=2)  

#Tilt using scale   
def servo2_tilt(self):
  global servoPan
  servoPan += servostepPan
  if servoPan > T1.get():
    servoPan = T1.get()
  #servo.setAccel(1,0)      #set servo 0 acceleration to 0
  #servo.setTarget(1,servoPan)  #set servo to move to center position
  #servo.close
  print T1.get()

T1 = Scale(display, from_="%s" % servoMin, to="%s" % servoMax, command=servo2_tilt)
T1.grid(row=2,column=4)

#Servo buttons
def servo1_left():
  global servoPan
  servoPan += servostepPan
  if servoPan > servoMax:
    servoPan = servoMax
  #servo.setAccel(0,0)      #set servo 0 acceleration to 4
  #servo.setTarget(0,servoPan)  #set servo to move to center position
  #servo.close
  print servoPan
  
B2=Button(display, text="Left", command=servo1_left, width=2, height=1)
B2.grid(row=3, column=2, sticky=W)

def servo1_right():
  global servoPan
  servoPan -= servostepPan
  if servoPan < servoMin:
    servoPan = servoMin
  #servo.setAccel(0,0)      #set servo 0 acceleration to 4
  #servo.setTarget(0,servoPan)  #set servo to move to center position
  #servo.close
  print servoPan

B3=Button(display, text="Right", command=servo1_right, width=2, height=1)
B3.grid(row=3, column=2, columnspan=1, rowspan=1, sticky=E)

def servo2_up():
  global servoPan
  servoPan += servostepPan
  if servoPan > servoMax:
    servoPan = servoMax
  #servo.setAccel(1,0)      #set servo 0 acceleration to 4
  #servo.setTarget(1,servoPan)  #set servo to move to center position
  #servo.close
  print servoPan
  
B4=Button(display, text="Up", command=servo2_up, width=2, height=1)
B4.grid(row=0, column=4, sticky=E)

def servo2_down():
  global servoPan
  servoPan -= servostepPan
  if servoPan < servoMin:
    servoPan = servoMin
  #servo.setAccel(1,0)      #set servo 0 acceleration to 4
  #servo.setTarget(1,servoPan)  #set servo to move to center position
  #servo.close
  print servoPan

B5=Button(display, text="Down", command=servo2_down, width=2, height=1)
B5.grid(row=3, column=4)

#Center servo's
def servo_center(self):
  global servoMid
  #P1.get() = servoMid
  #T1.get() = servoMid
  #servo.setAccel(0,0)         #set servo 0 acceleration to 0
  #servo.setTarget(0,servoMid) #set servo to move to center position
  #servo.setAccel(1,0)         #set servo 0 acceleration to 0
  #servo.setTarget(1,servoMid) #set servo to move to center position
  #servo.close

B1=Button(display, text="Center", command=servo_center, width=4, height=1)
B1.grid(row=0, column=0, sticky=W)
  
display.mainloop() 
